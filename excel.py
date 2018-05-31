# -*- coding: utf-8 -*-

import xlrd


def open_excel(file=''):
    try:
        data = xlrd.open_workbook(file)
        sheet = data.sheet_by_name("新兴产业总表")
        print(sheet.name, sheet.nrows, sheet.ncols)
        types = []
        for i in range(1, sheet.nrows):
            type = sheet.cell(i, 5).value
            if type.strip():
                types.append(type)
        i = 1005
        for name in set(types):
            print("insert into jcsjgl_hygl(code, name, pid) values('%s', '%s', %s);" % (str(i), name, 12))
            i = i + 1

    except Exception as e:
        print(e)


def read_sheets(file):
    try:
        data = xlrd.open_workbook(file)
        sheet_names = data.sheet_names()
        print(sheet_names)
        i = 1016
        for name in sheet_names:
            print("insert into jcsjgl_hygl(code, name) values('%s', '%s');" % (str(i), name))
            i = i + 1
    except Exception as e:
        print(e)


'''
统计产业类型与企业关系 
'''


def read_sheets_hydm(file):
    try:
        data = xlrd.open_workbook(file)
        sheets_list = ['新兴产业总表', '电子信息', '装备制造业', '机器人和智能制造', '纺织业', '化工医药', '建材', '冶金业']
        sql = open('C:\\Users\\Administrator\\Desktop\\sql.sql', 'w', encoding='utf-8')
        for name in sheets_list:
            sheet = data.sheet_by_name(name)
            xxcy_col = 0
            hydm_col = 0
            # 取标题
            for i in range(0, sheet.ncols):
                value = sheet.cell_value(0, i)
                # print(value)
                if value == '新兴产业类别':
                    xxcy_col = i
                if value == '单位名称':
                    hydm_col = i

            for i in range(1, sheet.nrows):
                hy_name = sheet.cell_value(i, xxcy_col)
                if name != '新兴产业总表':
                    hy_name = name
                hydm = str(sheet.cell_value(i, hydm_col))
                # print(hydm)
                if hydm:
                    sql.write(
                        "update xmgl_qyda set industry=(select hy.code from jcsjgl_hygl hy where hy.name='%s')  where orgn_name='%s'; \n" %
                        (hy_name, hydm.strip()))


    except Exception as e:
        print(e)


def read_zxqy_myqy(file):
    try:
        data = xlrd.open_workbook(file)
        sheets_list = ['中小企业', '民营企业']
        sql = open('C:\\Users\\Administrator\\Desktop\\sql.sql', 'w', encoding='utf-8')
        for name in sheets_list:
            sheet = data.sheet_by_name(name)
            xxcy_col = 0
            hydm_col = 0
            # 取标题
            for i in range(0, sheet.ncols):
                value = sheet.cell_value(0, i)
                if value == '组织机构代码':
                    hydm_col = i

            for i in range(1, sheet.nrows):
                tag_name = ''
                if name == '中小企业':
                    tag_name = 'zxqy'
                elif name == '民营企业':
                    tag_name = 'myqy'
                hydm = sheet.cell_value(i, hydm_col)
                if isinstance(hydm, float):
                    hydm = str(int(hydm))
                # print(hydm)
                if hydm:
                    print(tag_name, hydm)
                    sql.write("insert into xmgl_qyda_tag(tag_num, qy_orgn_code) values('%s', '%s');\n" %
                              (tag_name, hydm.strip()))


    except Exception as e:
        print(e)


if __name__ == '__main__':
    file = "C:\\Users\\Administrator\\Desktop\\经信数据\\Files\\规上产值数据库-分行业-2017.4.xls"
    # open_excel(file)
    # read_sheets(file)
    # read_sheets_hydm(file)
    read_zxqy_myqy(file)
