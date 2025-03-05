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
pip install git+https://github.com/LidyaGenomics/lidya_file_access_repository.git
```

## Usage

```python
from lidya_file_access_repository import FileAccessRepositoryFactory

# Create a local file repository
local_repo = FileAccessRepositoryFactory.create_local_repository(base_path="/path/to/local/storage")

# Create a MinIO repository
minio_repo = FileAccessRepositoryFactory.create_minio_repository(
    endpoint="minio.example.com:9000",
    access_key="your_access_key",
    secret_key="your_secret_key",
    bucket_name="your_bucket",
    secure=True
)

# Read a file
content = repo.read_file("path/to/file.txt")

# Write a file
repo.write_file("path/to/file.txt", "Hello, World!")

# Delete a file
repo.delete_file("path/to/file.txt")
```

## License

[MIT](LICENSE) 