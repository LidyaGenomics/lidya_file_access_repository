from setuptools import setup, find_packages

setup(
    name="lidya_file_access_repository",
    version="0.2.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "minio>=7.0.0",
    ],
    author="Ahmet Can Ogreten",
    author_email="ahmetcan@lidyagenomics.com",
    description="A file access repository package for Lidya",
    keywords="file, access, repository, minio",
    url="https://github.com/LidyaGenomics/lidya_file_access_repository.git",
    python_requires=">=3.10",
) 