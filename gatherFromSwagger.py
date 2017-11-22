import requests
import json, re

r = requests.get("http://192.168.1.6:8082/yry/v2/api-docs")
content = r.json()
insert_sql = ["insert into sys_menu(name, pid) values('幼儿园综合管理系统', 0);", "set @rootId=(select @@IDENTITY);"]
insert_sql_template = "insert into sys_menu(name, url, method, pid) values('%s', '%s', '%s', %s);"
# group tags...
tags = content["tags"]
tags_dict = {}
for t in tags:
    insert_sql.append(insert_sql_template % (t['name'], '', '', '@rootId'))
    tag_name = t['description'].replace(" ", "")
    insert_sql.append("set @%s=(select @@IDENTITY);" % tag_name)
    tags_dict[t['name']] = tag_name

# url paths...
paths = content["paths"]
urls = []
pattern = re.compile(r'(/\w+)/')
for p in paths:
    path = paths[p]
    rel_url = pattern.findall(p)
    m = ""
    for method in path:
        m = path[method]['tags'][0]
        break

    if rel_url and rel_url != "":
        urls.append(rel_url[0] + ":" + m)


for path in set(urls):
    (url, name) = path.split(":")
    insert_sql.append(insert_sql_template % (name.replace("接口", ""), url + "/**", 'ALL', '@'+tags_dict[name]))


output = open("E:\\insertsql.sql", "w+")
output.write("\n".join(insert_sql))
output.close()
print("ok")
