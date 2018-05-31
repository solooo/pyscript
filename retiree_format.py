# -*- coding: utf-8 -*-

import datetime
import re
import time

import xlrd

'''
离退休人员数据导入
'''

def read_excel():
    file = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\经信数据\离退休人员模板.xlsx')
    sheet = file.sheet_by_index(0)
    sql = open(r'C:\Users\Administrator\Desktop\经信数据\retiree_insert_sql.sql', 'w', encoding='utf-8')
    for i in range(0, sheet.nrows):
        if i == 0:
            continue
        dt = xlrd.xldate.xldate_as_datetime(sheet.cell(i, 5).value, 0)
        birthday = time.strftime("%Y-%m-%d", dt.timetuple())
        retiree_dt = xlrd.xldate.xldate_as_datetime(sheet.cell(i, 7).value, 0)
        retire_date = time.strftime("%Y-%m-%d", retiree_dt.timetuple())
        cols = ("name, id_card, sex, age, birthday, branch, retire_date, is_party_member, "
                "contacter, address, phone, original_unit, original_duty, health_status, live_status")
        values = "'%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'"
        phone_cell = sheet.cell(i, 12)
        ctype = phone_cell.ctype
        phone = int(phone_cell.value) if ctype == 2 else phone_cell.value

        value_tuple = (
            re.sub('\s+', '', sheet.cell_value(i, 1)),
            sheet.cell_value(i, 2),
            1 if (sheet.cell_value(i, 3) == '男') else 0,
            sheet.cell_value(i, 4),
            birthday,
            sheet.cell_value(i, 6),
            retire_date,
            sheet.cell_value(i, 8),
            sheet.cell_value(i, 10),
            sheet.cell_value(i, 11),
            phone,
            sheet.cell_value(i, 13),
            sheet.cell_value(i, 14),
            sheet.cell_value(i, 15),
            sheet.cell_value(i, 16)
        )

        join_party_date = sheet.cell_value(i, 9)
        if join_party_date != '':  # 入党日期不为空
            # print(join_party_date)
            cols = cols + ",join_party_date, party_age"
            values = values + ", '%s', %s"
            date_join = time.strptime(join_party_date, '%Y-%m-%d')
            value_tuple = (
                re.sub('\s+', '', sheet.cell_value(i, 1)),
                sheet.cell_value(i, 2),
                1 if (sheet.cell_value(i, 3) == '男') else 0,
                sheet.cell_value(i, 4),
                birthday,
                sheet.cell_value(i, 6),
                retire_date,
                sheet.cell_value(i, 8),
                sheet.cell_value(i, 10),
                sheet.cell_value(i, 11),
                phone,
                sheet.cell_value(i, 13),
                sheet.cell_value(i, 14),
                sheet.cell_value(i, 15),
                sheet.cell_value(i, 16),
                join_party_date,
                datetime.datetime.now().year - date_join.tm_year
            )
        str = ("insert into zhyw_ltxry(" + cols + ") values(" + values + "); \n")

        print(str % value_tuple)
        sql.write(str % value_tuple)


if __name__ == '__main__':
    read_excel()
