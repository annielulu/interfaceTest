# coding:utf-8
__author__ = 'lenovo'

# 1.导入包
# 2.找到excel文件并打开(找不到文件时捕获异常)
# 3.定位sheet页
# 4.定位行和列
# 5.读取excel数据
# 6.组装测试数据，变为一条正确的匹配的接口测试数据
# 7.return data给testCase模块

# 1.导入包
import xlrd
# 读取excelsheet页中的数据
class readExcel:
    # 2.找到excel文件并打开(找不到文件时捕获异常)
    readbook = xlrd.open_workbook(r'F:\Code\interfaceTest\testDate\data.xls')
    # 获取所有的sheet页名字的列表
    sheetlist = readbook.sheet_names()
    print(sheetlist)
    # 将读取的数据存入一个列表
    sheetData = []
    sheetUrl = []
    sheetParam = []
    sheetAssert = []
    # 获取sheet页数据
    def getData(self):
        # 3.定位sheet页
        for n in self.sheetlist:
            print('sheet页的名称为：',n)
            # 通过名字区分每个sheet页的数据
            sheet = self.readbook.sheet_by_name(n)
            # 通过索引定位sheet页
            # sheet = self.readbook.sheet_by_index(0)
            # 4.定位行和列
            sheet_nrows = sheet.nrows # 获取sheet页最大行数
            sheet_ncols = sheet.ncols  # 获取sheet页最大列数
            print(sheet_ncols,sheet_nrows)
            # 5.读取excel数据
            # 循环读取excel表格
            for i in range(1,sheet_nrows):
                row_values = sheet.row_values(i)
                if self.sheetlist.index(n) == 0:
                    self.sheetUrl.append(row_values)
                    # print(row_values)
                elif self.sheetlist.index(n) == 1:
                    self.sheetParam.append(row_values)
                elif self.sheetlist.index(n) == 2:
                    self.sheetAssert.append(row_values)
            print(self.sheetUrl,self.sheetParam,self.sheetAssert)

    # 6.组装测试数据，变为一条正确的匹配的接口测试数据
    # 组装数据，将三个列表按照id进行匹配
    def assembleData(self):
        data = self.sheetUrl[0] + self.sheetParam[0][1:]
        print(data)
        pass
    # 7.return data给testCase模块
    # 待补充
read = readExcel()
read.getData()

