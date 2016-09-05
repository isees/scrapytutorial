import ast
import json

real_list = ['aaa', 'bbb', 'ccc']
teststr = "['aaa','bbb','ccc']"
testarray = ast.literal_eval(teststr)

print teststr
x = json.dumps(teststr)
print x

for element in testarray:
    print element

print json.dumps(real_list)