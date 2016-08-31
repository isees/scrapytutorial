from xgoogle.search import GoogleSearch, SearchError

import os
os.environ['http_proxy'] = '127.0.0.1:1080'
os.environ['https_proxy'] = '127.0.0.1:1080'

try:
    gs = GoogleSearch("hello")
    # gs.results_per_page = 10
    results = gs.get_results()
    for res in results:
        print res.title.encode("utf8")
        print res.desc.encode("utf8")
        print res.url.encode("utf8")
        print res
except SearchError, e:
    print "Search failed: %s" % e
