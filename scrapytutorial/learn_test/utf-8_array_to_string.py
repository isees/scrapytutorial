# -*- coding: utf-8 -*-
import json

x = [1, 2, 5, 3, 5, 3, 6, 3, 32, ]
for key in range(len(x)):
    print key, x[key]

y = ['世界是平的', '世界是不平等的', 'the world is flat']

file_name = "D:\workspace\python\scrapytutorial\doc\\ascii_test.txt"
with open(file_name, 'wb') as file:
    file.write(json.dumps(y))
    file.write('\n')
    file.write(json.dumps(y, ensure_ascii=False))
    file.write('\n')
    # print json.dumps(y, ensure_ascii=False)
    # print json.dumps(y, ensure_ascii=False)
    # print json.dumps(y, ensure_ascii=False)


