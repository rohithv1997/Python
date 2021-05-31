import openpyxl, os, datetime

workbook = openpyxl.Workbook()
# print(workbook.sheetnames)
sheet = workbook["Sheet"]
unixTime = int(datetime.datetime.timestamp(datetime.datetime.now()))
# print(sheet['A1'].value)
sheet["A1"] = unixTime
# print(os.getcwd())
# print(unixTime)
fileName = os.getcwd() + "/" + str(unixTime) + ".xlsx"
workbook.save(fileName)