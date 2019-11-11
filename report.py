import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date


#Update and show fns

def updateManagerSalary():
    global cur
    row = {}
    query1 = "SELECT HRID FROM EMPLOYEE WHERE TypeOfEmployee='Manager'"
    cur.execute(query1)
    Managers=cur.fetchall()
    for i in range(len(Managers)):
        query="SELECT SUM(TotalProfit) FROM REGISTER WHERE ManagerHRID='%s'" %(Managers[i])
        cur.execute()
        managerSalary=cur.fetchall()
        managerSalary=float(managerSalary[0])
        query2="UPDATE EMPLOYEE SET Salary='%d' WHERE HRID='%s'" %(managerSalary*0.2, Managers[i])
        cur.execute(query2)
        con.commit()
    return

def reportProfit():
    global cur
    storeid=input("Enter Store ID")
    print("The Store with ID ",storeid ,"has profits of", )

    query = "SELECT SUM(TotalProfit) FROM REGISTER WHERE StoreID = '%s'"
    cur = execute(query)
    blah = cur.fetchall()
    blah=int(blah[0])
    print blah
    return

def showStoreItems():
    global cur
    storeID=input("Enter Store ID: ");

    query2 = "SELECT * FROM HAS WHERE StoreID='%s'" %(storeID)

    cur.execute(query2)
    blah = cur.fetchall()
    for value in blah:
        print value

    return

def checkNowSales():
    global cur
    today=date.today()
    query="SELECT * FROM SALE WHERE '%s' BETWEEN StartDate AND EndDate"
    cur.execute()
    salesNow=cur.fetchall()
    for i in range(len(salesNow)):
        print(salesNow[i])
    return


def checkSuperviseeSalaryProfit():
    global cur
    id=input("Enter your HRID: ")
    empid=input("Enter supervisee's HRID: ")

    query = "SELECT A.Salary FROM EMPLOYEE A, SUPERVISES B WHERE B.CashierHRID='%s' AND B.SupervisorHRID='%s' AND B.CashierHRID=A.HRID" %(empid, id)
    cur = execute(query)
    superviseeSalary = cur.fetchall()
    for i in range(len(superviseeSalary)):
        print(superviseeSalary[i])
    if len(superviseeSalary) == 0:
        print("This employee is not your supervisee")
    return
 
def checkMySalary():
    global cur
    id=input("Enter HRID whose salary you want to see:")
    print("The Employee with ID ",id ,"has a salary of", )

    query = "SELECT SALARY FROM EMPLOYEE WHERE HRID = '%s'"
    cur.execute(query)
    blah = cur.fetchall()
    blah=int(blah[0])
    print blah
    return
