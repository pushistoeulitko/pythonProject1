import fileinput
import pathlib
import pprint
import json

pth = 'C:/Users/pushi/PycharmProjects/pythonProject1/reports'
pattern = '*.json'
files_path = pathlib.Path(pth)
list_files = files_path.glob(pattern)
final_report = 'final_report.json'

scenario={}

def generate_report():
    if list_files:
        with fileinput.FileInput(files=list_files, openhook=fileinput.hook_encoded("utf-8")) as fr, \
                open(final_report, 'w', encoding="utf-8") as fw:
            for line in fr:
                info = eval(line)
                scenario.update({
                    info['name']: {
                        'status': info['status'],
                        'steps': len(info['steps']),
                        'start': info['start'],
                        'stop': info['stop']
                    }
                })
                #pprint.pprint((info['start'] - info['stop'])//60)
                #pprint.pprint(scenario)
            json.dump(scenario, fw, indent=4, sort_keys=True, ensure_ascii=False, separators=(',', ': '))

generate_report()
