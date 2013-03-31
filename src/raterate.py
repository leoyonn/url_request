'''
Created on 2012-8-10

@author: liuyang
'''
import re
import sys

pat_method = re.compile('m=\[\[(.*)\]\]');
pat_uid = re.compile('userid=(\-?\d+)');

'''
analyze what the user rates come from
'''
def raterate(infile):
    lines = open(infile, 'r');
    count = 0;
    user_methods = dict()
    # parse each line of the log, and collect by userid.
    for line in lines:
        m = pat_method.search(line);
        uid = pat_uid.search(line);
        if m is None or uid is None:
            continue
        m = m.group(1)[1:];
        m = m[0 : m.find('"')];
        uid = uid.group();
        uid = uid[7 : len(uid)];
        methods = user_methods.get(uid)
        if not methods:
            methods = list()
            user_methods[uid] = methods
        methods.append(m)

    n_per = 0
    n_rec = 0
    n_rest = 0
    n_rate = 0
    n_rrate = 0
    # for each user
    for u in user_methods:
        # find his 'rate' api's source: recommend or personalize
        for i in range(len(user_methods[u])):
            methods = user_methods[u]
            m = user_methods[u][i] 
            if m != 'rate':
                continue
            per = False
            rec = False
            rest = False
            for j in reversed(range(i)):
                if per or rec:
                    break
                if methods[j] == 'recommend':
                    rec = True
                    n_rec += 1
                elif methods[j] == 'personalize':
                    per = True
                    n_per += 1
                elif methods[j] == 'restinfo' and not rest:
                    rest = True
                    n_rest += 1
                elif methods[j] == 'rate':
                    n_rrate += 1
                    break
            n_rate += 1
    print 'rate:', n_rate, '| per:', n_per, '| rec:', n_rec, '| rest:', n_rest, '| rrate:', n_rrate

raterate(sys.argv[1]);
#raterate('/home/liuyang/codes/silmaril/0810.dat');
