import openpyxl
import sys
N= int(sys.argv[1])
wb=openpyxl.workbook()
sheet=wb.active()
sheet.title("Multiplication Table")
row = 1
for i in range(0,N+1):
    for j in range(0,11):
        result=f"{i}*{j}={i*j}"
        sheet.cell(row=row,column=1,value=result)
        row+=1
wb.save("Multiplication.xlsx")
print("Saved")