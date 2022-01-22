import xlrd as excel
import webbrowser as wbs
from datetime import date 

numberofclasses = [5,7,5,4,4,0,0]
weekend = ["Saturday","Sunday"]

def login(number,today):
    check=0
    wb = excel.open_workbook(r"C:\Users\ASUS\OneDrive\Pictures\Screenshots\OneDrive\Desktop\Zoom-Class-Logger\Timetable.xlsx")
    sheet = wb.sheet_by_index(0)
    i=0
    for i in range(sheet.ncols):
        if today in sheet.cell_value(0,i):
            link = sheet.cell_value(number,i)
            print("Loging into zoom link ",link)
            wbs.open(link)
            break
    if numberofclasses[i] == number:
        check=1
    lis = [number+1,check]
    return lis

def main():
    i=1
    check=0
    today = date.today().strftime("%A");
    for i in weekend:
        if i==today:
            return
    print("Press Enter to proceed")
    while((not check) and (input()=="" or input())):
        lis=login(i,today)
        i=lis[0]
        check=lis[1]
main()
