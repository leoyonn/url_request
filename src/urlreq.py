#coding=utf-8
'''
Created on 2012-7-18
读入url文件，将其中的每一条url发送访问请求

@author: liuyang
'''

import urllib   
import datetime
import sys

def re_request(infile):
    lines = open(infile, 'r').readlines();
    count = 0;
    for line in lines:
        print line;
        time = datetime.datetime.now();
        urllib.urlopen(line);
        time = datetime.datetime.now() - time;
        print '[', count, ', ', time, '], url: ', line;
        count = count + 1;

re_request(sys.argv[1]);
