from minio import Minio
import os
import hashlib

from .file_access_repository import FileAccessRepository


class MinIOFileAccessRepository(FileAccessRepository):
    """
    Implementation of FileAccessRepository for MinIO storage.
    """

    def __init__(
        self,
        access_key: str,
        secret_key: str,
        endpoint: str,
        secure: bool,
        cert_check: bool,
    ):
        """
        Initialize the MinIO file access repository.

        Args:
            access_key: MinIO access key
            secret_key: MinIO secret key
            endpoint: MinIO endpoint
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.endpoint = endpoint
        self.secure = secure
        self.cert_check = cert_check

        self.client = Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            secure=secure,
            cert_check=cert_check,
        )

    def get_file(self, file_type: str, file_name: str, to_path: str) -> None:
        """
        Retrieves a file from S3 and saves it to the specified path.
        If the local file already exists and matches the remote file, no download occurs.

        Args:
            file_type: The type or category of the file
            file_name: Name of the file to retrieve
            to_path: Local path where the retrieved file should be saved

        Returns:
            None

        Raises:
            FileNotFoundError: If the file does not exist in S3
            IOError: If there is an error reading the file from S3
        """
        try:
            # Check if the local file already exists
            if os.path.exists(to_path):
                # Get remote file stats
                try:
                    remote_stat = self.client.stat_object(file_type, file_name)
                    remote_size = remote_stat.size
                    remote_etag = remote_stat.etag
                    
                    # Get local file size
                    local_size = os.path.getsize(to_path)
                    
                    # If sizes match, check etag/md5
                    if local_size == remote_size:
                        # Calculate MD5 of local file
                        with open(to_path, 'rb') as file_data:
                            local_md5 = hashlib.md5(file_data.read()).hexdigest()
                        
                        # MinIO etags are typically md5 hashes in quotes
                        remote_md5 = remote_etag.strip('"')
                        
                        if local_md5 == remote_md5:
                            print(
                                f"File {to_path} already exists and is identical to {file_type}/{file_name}. Skipping download."
                            )
                            return
                except Exception as e:
                    # If any error occurs during verification, proceed with download
                    print(f"Error verifying file, will download: {str(e)}")
            
            # If we get here, either the file doesn't exist locally or is different
            self.client.fget_object(
                file_type,
                file_name,
                to_path,
            )
            print(
                "Object",
                file_name,
                "successfully downloaded from bucket",
                file_type,
                "to local file",
                to_path,
            )
        except Exception as e:
            raise IOError(
                f"Error downloading file from S3 {file_type}/{file_name}: {str(e)}"
            )

    def put_file(self, file_type: str, file_name: str, from_path: str) -> None:
        """
        Stores a file in S3.

        Args:
            file_type: The type or category of the file
            file_name: Name of the file to store
            from_path: Local path of the file to store

        Returns:
            None

        Raises:
            IOError: If there is an error writing the file to S3
        """

        try:
            # Make the bucket if it doesn't exist.
            print("Making bucket", file_type)
            found = self.client.bucket_exists(file_type)
            if not found:
                self.client.make_bucket(file_type)
                print("Created bucket", file_type)
            else:
                print("Bucket", file_type, "already exists")

            # Upload the file, renaming it in the process
            self.client.fput_object(
                file_type,
                file_name,
                from_path,
            )
            print(
                from_path,
                "successfully uploaded as object",
                file_name,
                "to bucket",
                file_type,
            )
        except Exception as e:
            raise IOError(
                f"Error uploading file from {from_path} to S3 {file_type}/{file_name}: {str(e)}"
            )

    def delete_file(self, file_type: str, file_name: str) -> None:
        """
        Deletes a file from MinIO storage.

        Args:
            file_type: The type or category of the file (bucket name)
            file_name: Name of the file to delete (object name)

        Returns:
            None

        Raises:
            FileNotFoundError: If the file does not exist
            IOError: If there is an error deleting the file
        """
        try:
            # Check if bucket exists
            found = self.client.bucket_exists(file_type)
            if not found:
                raise FileNotFoundError(f"Bucket {file_type} does not exist")

            # Delete the object
            self.client.remove_object(file_type, file_name)
            print(
                "Object",
                file_name,
                "successfully deleted from bucket",
                file_type,
            )
        except FileNotFoundError:
            raise
        except Exception as e:
            raise IOError(
                f"Error deleting file from S3 {file_type}/{file_name}: {str(e)}"
            )
