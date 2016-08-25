# -*- coding: utf-8 -*-
import json
import sys


def get_member_array(file_path):
    member_array = []
    print file_path
    con_line = open(file_path.decode('utf8').encode('gbk'), 'r')
    for line in con_line:
        if line.strip() in member_array:
            continue
        member_array.append(line.strip())
    return member_array


app_member_file = 'C:\Users\Bain\Desktop\\app会员.txt'
member_file = 'C:\Users\Bain\Desktop\花店会员.txt'

app_member_list = get_member_array(app_member_file)
member_list = get_member_array(member_file)

for member in member_list:
    if member in app_member_list:
        continue
    print member

