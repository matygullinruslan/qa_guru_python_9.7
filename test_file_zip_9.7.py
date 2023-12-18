import os

from zipfile import ZipFile

import file

myzip = ZipFile("test_archive.zip", "w")  # создаем архив
with ZipFile("test_archive.zip", "w") as myzip:  #
    myzip.write("test_file.txt")
    myzip.write("test_file.csv")
    myzip.write("test_file.xlsx")
    myzip.write("test_file.pdf")
    # os.rename('.\\qa_guru_python_9.7\\test_archive.zip', '.\\qa_guru_python_9.7\\tmp\\test_archive.zip')
os.rename('C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\test_archive.zip',
          'C:\\Users\\rusel\\QA.GURU\\qa_guru_python_9.7\\tmp\\test_archive.zip')
directory = os.path.join(os.path.dirname(file), "tmp")
print('directory')
with ZipFile("test_archive.zip", "r") as myzip:
    content = myzip.read('')
print(content)



