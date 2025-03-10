from abc import ABC, abstractmethod


class FileAccessRepository(ABC):
    """
    Abstract base class for file access repositories.
    Provides an interface for accessing files from different storage systems.
    """

    @abstractmethod
    def get_file(self, file_type: str, file_name: str, to_path: str) -> None:
        """
        Retrieves a file from the storage system and saves it to the specified path.

        Args:
            file_type: The type or category of the file
            file_name: Name of the file to retrieve
            to_path: Local path where the retrieved file should be saved

        Returns:
            None

        Raises:
            FileNotFoundError: If the file does not exist
            IOError: If there is an error reading the file
        """

    @abstractmethod
    def put_file(self, file_type: str, file_name: str, from_path: str) -> None:
        """
        Stores a file in the storage system.

        Args:
            file_type: The type or category of the file
            file_name: Name of the file to store
            from_path: Local path of the file to store

        Returns:
            None

        Raises:
            IOError: If there is an error writing the file
        """

    @abstractmethod
    def delete_file(self, file_type: str, file_name: str) -> None:
        """
        Deletes a file from the storage system.

        Args:
            file_type: The type or category of the file
            file_name: Name of the file to delete

        Returns:
            None

        Raises:
            FileNotFoundError: If the file does not exist
            IOError: If there is an error deleting the file
        """
