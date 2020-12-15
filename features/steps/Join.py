import codecs
import fileinput
import pathlib
import json

pth = 'C:/Users/pushi/PycharmProjects/pythonProject1/reports'
pattern = '*.json'
files_path = pathlib.Path(pth)
list_files = files_path.glob(pattern)
final_report = 'final_report.json'


def generate_report():
    if list_files:
        with fileinput.FileInput(files=list_files, openhook=fileinput.hook_encoded("utf-8")) as fr, \
                open(final_report, 'w', encoding="utf-8") as fw:
            for line in fr:
                if fr.isfirstline():
                    file_name = fr.filename()
                    fw.write(f'\n\n------------ {file_name}\n\n')
                    print(line)
                fw.write(line)


generate_report()
