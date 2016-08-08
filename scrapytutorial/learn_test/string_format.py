import random

print 'I codes %s %d' % ('56c7d4ac7c1f5d3b683c7097', random.randint(10000000000, 99999999999))


def get_mobile_params(supplier_id):
    return [{'id': 'id' + str(random.randint(1000000000, 9999999999)),
             'name': 'supplierWebRpc.showSupplierMobile',
             'args': ["\"%s\"" % supplier_id, "\"%d\"" % (random.randint(10000000000, 19999999999))]}]

print get_mobile_params('56c7d4ac7c1f5d3b683c7097')