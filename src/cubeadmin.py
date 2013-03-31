# -*- coding: utf-8 -*-
#!/usr/bin/python
# author: leo
# data: 2012-09-25

import urllib2, json, re
GOODS='''
7805697692599882047 -8357764129371492671 
7805692474482761243 4100233072702397979 
7805704165596612305 1245479610659653329 
7806122599751894737 124547961065965332 
7806140663848081403 3333897175387445243 
7805800309123501159 5365535713433537639 
7806163087669930784 4301964567872088864 
7806242500781779614 -5707390929499302558 
7806242698756074142 -5707390929499302558 
7806330078493427409 1245479610659653329 
7806166999170600039 5365535713433537639 
7806242865274137246 -5707390929499302558 
7805672732267401506 -3910570211317666082 
7806527787888646808 -468892103376738968 
7806476211625208608 4301964567872088864 
7805615848110322370 -916746110903939778 
7805615661783610050 -916746110903939778 
7821098000718448983 -1082009531446675799 
7805849274464514881 8461941596354687809 
7806522788179784513 8461941596354687809 
'''

URL_BASE = "http://bafang.163.com/api?doctype=json&rpwt=supercube@163.com&method="
URL_GETWALL = URL_BASE + "getWall&index=0&count=300"
URL_OFFWALL = URL_BASE + "takeEleOffWall&type=%s&oriId=%s"
URL_ONWALL = URL_BASE + "addToWallByOp&type=1&oriId=%s&referUser=%s&wallIndex=%d"

def offwall(type, id):
    url = URL_OFFWALL %(type, id)
    response = urllib2.urlopen(urllib2.Request(url, None, {}))
    result = json.load(response)
    print result[1]['value'], '(', url, ')'
    
def alloffwall():
    response = urllib2.urlopen(urllib2.Request(URL_GETWALL, None, {}))
    results = json.load(response)
    if results[1].has_key('elements'):
        for e in results[1]['elements']:
            offwall(e['type'], e['oriId'])

def onwall():
    goods = re.split('\s*\n\s*', GOODS)
    wallidx = 0
    for good in goods:
        eu = re.split('\s+', good)
        if len(eu) != 2:
            continue
        url = URL_ONWALL %(eu[0], eu[1], wallidx)
        response = urllib2.urlopen(urllib2.Request(url, None, {}))
        result = json.load(response)
        wallidx = wallidx + 1
        print result,
        if result[0].has_key('message'):
            print result[0]['message'],
        elif len(result) > 1 and result[1].has_key('value'):
            print result[1]['value'],
        
        print '(', url, ')|(', good, ')'

def main():
    alloffwall()
    onwall()
    
main()
