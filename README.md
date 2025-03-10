# Lidya File Access Repository

A Python package that provides a unified interface for accessing files from different storage systems.

## Features

- Abstract `FileAccessRepository` interface
- Local file system implementation
- MinIO object storage implementation
- Factory pattern for creating repositories

## Installation

### From Git

```bash
pip install git+https://github.com/LidyaGenomics/lidya_file_access_repository.git@0.2.0
```

## Usage

First create a file access repository.

```python
# Import FileAccessRepositoryFactory
from lidya_file_access_repository import FileAccessRepositoryFactory

# Create file access repository
# It will check the environment variable to see which file access repository to use and create it

# If STORAGE_TYPE=local -> LocalFileAccessRepository
# No other variables are needed

# If STORAGE_TYPE=minio -> MinioFileAccessRepository
# Other variables are needed as well
# MINIO_ACCESS_KEY=minio
# MINIO_SECRET_KEY=minio123
# MINIO_ENDPOINT=minio:9000
# MINIO_SECURE=false
# MINIO_CERT_CHECK=false

file_access_repository = FileAccessRepositoryFactory.create()
```

Then you can use the file access repository to get, put, and delete files.

```python
# Get a file from storage and save it locally
# file_type: The type or category of the file
# file_name: Name of the file to retrieve
# to_path: Local path where the retrieved file should be saved
file_access_repository.get_file(file_type="fastq", file_name="subsamp_10k_AD_1211_L001_R1.fastq.gz", to_path="opt/fastq_files/subsamp_10k_AD_1211_L001_R1.fastq.gz")

# Put a local file into storage
# file_type: The type or category of the file
# file_name: Name to give the file in storage
# from_path: Local path of the file to store
file_access_repository.put_file(file_type="fastq", file_name="subsamp_10k_AD_1211_L001_R1.fastq.gz", from_path="opt/fastq_files/subsamp_10k_AD_1211_L001_R1.fastq.gz")

# Delete a file from storage
# file_type: The type or category of the file
# file_name: Name of the file to delete
file_access_repository.delete_file(file_type="fastq", file_name="subsamp_10k_AD_1211_L001_R1.fastq.gz")
```

## Error Handling

The repository methods may raise the following exceptions:

```python
# When retrieving a file that doesn't exist
try:
    file_access_repository.get_file("documents", "missing.pdf", "/local/path/output.pdf")
except FileNotFoundError:
    print("The requested file does not exist in storage")
except IOError:
    print("Error reading the file from storage")

# When storing a file
try:
    file_access_repository.put_file("documents", "report.pdf", "/local/path/report.pdf")
except IOError:
    print("Error writing the file to storage")

# When deleting a file
try:
    file_access_repository.delete_file("documents", "report.pdf")
except FileNotFoundError:
    print("The file to delete does not exist in storage")
except IOError:
    print("Error deleting the file from storage")
```

## License

[MIT](LICENSE) 