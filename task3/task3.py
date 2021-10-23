# python task3.py -t=tests.json -v=values.json

import argparse
import json

parser = argparse.ArgumentParser(description="task3")
parser.add_argument("-t", type=argparse.FileType('r'), help="tests.json")
parser.add_argument("-v", type=argparse.FileType('r'), help="values.json")
args = parser.parse_args()
options = [args.t, args.v]

with open('values.json', 'r') as new_data:
    b = json.load(new_data)

with open('tests.json', 'r') as data:
    a = json.load(data)

def merge(a, b):
    lookup = {o['id']: o for o in a['tests']}
    for e in a['tests']:
        e['value'] = set([x.strip() for x in e['value'].split(",")])
    for e in b['values']:
        if e['id'] in lookup:
            lookup[e['id']]['value'].update([x.strip() for x in e['value'].split(",")])
        else:
            e['value'] = set([x.strip() for x in e['value'].split(",")])
            a['tests'].append(e)
    for e in a['tests']:
        if "*" in e['value']:
            e['value'] = "*"
        else:
            e['value'] = "".join(sorted(list(e['value'])))
merge(a, b)

with open("report.json", "w") as report:
    json.dump(a, report)
