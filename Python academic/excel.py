import openpyxl
import sys
N = int(sys.argv[1])
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title="Multiplication Table"
row=1
for i in range(1,N+1):
    for j in range(1,11):
        result=f"{i}*{j}={i*j}"
        sheet.cell(row=row,column=1,value=result)
        row+=1
wb.save('Multiplication.xlsx')
print((f"Multiplication table from 1*1 to {N}*10 has been saved to 'multiplication.xlsx .'"))

"C:\Users\gwwny\Multiplication.xlsx"