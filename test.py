import os
from zipfile import ZipFile

directory = os.path.join(os.path.dirname(__file__), "resources")
print(directory)

if not os.path.exists(directory):
    os.mkdir(directory)


def test_create_zip_archive():
    with ZipFile("resources/test_archive.zip", "w") as myzip:
        myzip.write("test_file.txt")
        myzip.write("test_file.csv")
        myzip.write("test_file.xlsx")
        myzip.write("test_file.pdf")


with ZipFile("resources/test_archive.zip") as myzip:
    print(myzip.namelist())  # отобразить содержимое архива
    myzip.extractall(path="resources")  # извлечь все файлы из архива в папку resources