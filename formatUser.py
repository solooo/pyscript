# -*- coding: utf-8 -*-

import hashlib
import re
import time

f = open("E:/tmp/users.txt", "r")

def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

def out_user():
    for line in f:
        split = line.split(',')
        tel = split[4]
        office_addr = split[5].strip()
        name = re.sub('\s+', '', split[1])
        password = md5('123456~!@' + name + '#$%')
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        insert = "insert into zhyw_zzry(user_name, password, real_name, phone, office_addr, create_time) values('%s','%s','%s','%s','%s', '%s');"
        print(insert % (name, password, name, tel, office_addr, create_time))

def out_orgn():
    s = set()
    for line in f:
        split = line.split(',')
        orgn = split[0]
        s.add(orgn)
    for orgn in s:
        print(orgn)

if __name__ == '__main__':
    out_orgn()
