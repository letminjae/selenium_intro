import openpyxl

excel_file = openpyxl.load_workbook("/Users/chaminjae/Desktop/SQA/python_excel_demo.xlsx")

# 시트 제어
sheet1 = excel_file.active
cell = sheet1.cell(row=1, column=2) # Firstname
print(cell.value) # Firstname