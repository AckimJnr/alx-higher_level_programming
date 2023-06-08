#!/usr/bin/python3

import marshal

with open('hidden_4.pyc', 'rb') as pyc_file:
    pyc_data = pyc_file.read();

pcfileobj = marshal.loads(pyc_data[8:])
names = code_obj.co_names

print(names)
