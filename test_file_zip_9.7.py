import os
import zipfile
from typing import TextIO
from zipfile import ZipFile
import time
import shutil
import content

# z_archive = r"C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\tmp\\test_archive.zip"
# z_archive = ZipFile(z_archive, 'w')  # создаем архив
# with ZipFile("metanit.zip", "w") as myzip:
myzip = ZipFile("test_archive.zip", "w")  # создаем архив
with ZipFile("test_archive.zip", "w") as myzip:  #
    myzip.write("test_file.txt")
    myzip.write("test_file.csv")
    myzip.write("test_file.xlsx")
    # os.rename('.\\qa_guru_python_9.7\\test_archive.zip', '.\\qa_guru_python_9.7\\tmp\\test_archive.zip')
os.rename('C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\test_archive.zip',
          'C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\tmp\\test_archive.zip')
with ZipFile("test_archive.zip", "r") as myzip:
    content = myzip.read("test_file.txt")
print(content)





# z_archive.write(r'C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\tmp\Test_file.txt')  # добавляем файл 1 в архив
# z_archive.write(r'C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\tmp\\Test_file.xlsx')  # добавляем файл 2 в архив
# z_archive.write(r'C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\tmp\\Test_file.csv')  # добавляем файл в 3 архив
#
# zname = ZipFile('C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\tmp\Test_file.txt\\test_archive.zip')
# print(zname.namelist())

# myzip = ZipFile("test_archive1.zip", "w")
# ...