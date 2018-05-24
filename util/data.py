"""
1. 从excel中获取用例数据
2. 从excel中获取sql
"""
import os
import xlrd
import sys
sys.path.append("..")
from util.config import project_dir

data_path = os.path.join(project_dir, 'data')


class Data():
    def __init__(self, file_name):
        data_file = os.path.join(data_path, file_name)
        # 打开excel文件
        self.wb = xlrd.open_workbook(data_file)

    # 获取用例
    def get_test_case(self, sheet_name, case_name):
        sh = self.wb.sheet_by_name(sheet_name)
        for i in range(1, sh.nrows):
            if sh.cell(i, 0).value == case_name:
                title = sh.row_values(0)
                return dict(zip(title, sh.row_values(i)))
        return None

    def get_sql(self, sql_name):
        sh = self.wb.sheet_by_name('SQL')
        for i in range(0, sh.nrows):
            if sh.cell(i,0).value == sql_name:
                return sh.cell(i,1).value
        return None


if __name__ == '__main__':
    # d = Data("新建 Microsoft Office Excel 工作表.xlsx")
    # print(d.get_test_case('sheet1', 'test'))
    # print(d.get_sql('checkUser'))
    d = Data("test_user_data.xlsx")
    # print(d.get_test_case('login', 'test_user_login_normal'))
    print("hgjlkhgfdsfghjk1111111111111111111111111111111")


