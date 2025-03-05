import os

from .file_access_repository import FileAccessRepository
from .local_file_access_repository import LocalFileAccessRepository
from .minio_file_access_repository import MinIOFileAccessRepository


class FileAccessRepositoryFactory:
    """Factory class for creating FileAccessRepository instances."""

    @staticmethod
    def create(storage_type=None) -> FileAccessRepository:
        """
        Create the appropriate FileAccessRepository based on storage type.

        Args:
            storage_type: The type of storage to use. If None, will be read from environment.

        Returns:
            An implementation of FileAccessRepository

        Raises:
            ValueError: If the storage type is invalid
        """
        # If storage_type not provided, get from environment
        if storage_type is None:
            storage_type = os.environ.get("STORAGE_TYPE", "local").lower()

        if storage_type == "minio":
            print("Using MinIO storage")
            # Create MinIO repository
            return MinIOFileAccessRepository(
                access_key=os.environ.get("MINIO_ACCESS_KEY"),
                secret_key=os.environ.get("MINIO_SECRET_KEY"),
                endpoint=os.environ.get("MINIO_ENDPOINT"),
                secure=os.environ.get("MINIO_SECURE", "false").lower() == "true",
                cert_check=os.environ.get("MINIO_CERT_CHECK", "false").lower()
                == "true",
            )
        elif storage_type == "local":
            print("Using local storage")
            # Create local repository
            return LocalFileAccessRepository()
        else:
            raise ValueError(f"Invalid storage type: {storage_type}")
