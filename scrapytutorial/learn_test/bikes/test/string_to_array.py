# coding: utf-8

import ast
import json

real_list = ['aaa', 'bbb', 'ccc']
teststr = '["无论什么情况，只需按一下按钮，就可实现11速系统快如闪电般的变速，并且具高精确性"]'
testarray_1 = ast.literal_eval(teststr)
# testarray_2 = json.loads(teststr)


print teststr
x = json.dumps(teststr)
print x

for element in testarray_1:
    print element

# for element in testarray_2:
#     print element

print json.dumps(real_list)
