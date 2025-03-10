from .file_access_repository import FileAccessRepository


class LocalFileAccessRepository(FileAccessRepository):
    """
    Implementation of FileAccessRepository for local file system access.
    This implementation assumes files are already in the local filesystem,
    so no actual file transfer operations are needed.
    """

    def get_file(self, file_type: str, file_name: str, to_path: str) -> None:
        """
        Since file is already at the destination path in the local filesystem,
        this implementation doesn't need to perform any operations.

        Args:
            file_type: The type or category of the file
            file_name: Name of the file to retrieve
            to_path: Local path where the retrieved file should be saved

        Returns:
            None

        Raises:
            None
        """

    def put_file(self, file_type: str, file_name: str, from_path: str) -> None:
        """
        Since file is already at the destination path in the local filesystem,
        this implementation doesn't need to perform any operations.

        Args:
            file_type: The type or category of the file
            file_name: Name of the file to store
            from_path: Local path of the file to store

        Returns:
            None

        Raises:
            None
        """
        
    def delete_file(self, file_type: str, file_name: str) -> None:
        """
        Deletes a file from the local filesystem.
        
        Args:
            file_type: The type or category of the file
            file_name: Name of the file to delete
            
        Returns:
            None
            
        Raises:
            FileNotFoundError: If the file does not exist
            IOError: If there is an error deleting the file
        """
        pass
