import os
from zipfile import ZipFile


with test_archive.zip() as archive:
    archive.create_entry("file", "file.txt")
