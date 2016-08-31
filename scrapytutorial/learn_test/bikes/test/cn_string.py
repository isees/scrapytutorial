# coding:utf-8
import json

print u'世界是平的'
array = [u'时间', u'是', u'相对的']
print json.dumps(array, ensure_ascii=False)