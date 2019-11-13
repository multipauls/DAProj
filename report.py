import subprocess as sp
import pymysql
import pymysql.cursors
from datetime import date

#Loading and adding fns
def hireEmp():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = input("Salary: ")

    for i in range(len(row["Phone"])):
        query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], int(row["Phone"][i]))
        cur.execute(query1)
        con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, Salary) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], int(row["Salary"]))

    cur.execute(query2)
    con.commit()
    return


def addItem():
    global cur
    row = {}
    print("Enter new item's details: ")
    row["ItemID"] = input("Item ID: ")
    row["Name"] = input("Name: ")
    row["ItemNo"] = input("Item Number: ")
    row["CP"] = input("Item Cost Price: ")
    row["SP"] = input("Item Sell Price: ")
    row["Types"] = input("Types of Item: ").split(" ")
    row["Locations"] = input("Store IDs of Locations: ").split(" ")

    for i in range(len(row["Locations"])):
        query1 = "INSERT INTO HAS(StoreID, ItemName) VALUES('%s', '%s')" %( row["Locations"][i], row["Name"])
        cur.execute(query1)
        con.commit()

    for i in range(len(row["Types"])):
        query2 = "INSERT INTO ISTYPE(ItemID, TypeOfItem) VALUES('%s', '%s')" %( row["ItemID"], row["Types"][i])
        cur.execute(query2)
        con.commit()

    query3 = "INSERT INTO ITEM(ItemID, Name, ItemNumber, ItemCostPrice, ItemSalePrice) VALUES('%s', '%s', '%d', '%d', '%d')" %(row["ItemID"], row["Name"], int(row["ItemNo"]), int(row["CP"]), int(row["SP"]))

    cur.execute(query3)
    con.commit()
    return

def openStore():
    global cur
    row = {}
    print("Enter new store's details: ")
    row["StoreID"] = input("Store ID: ")
    row["Location"] = input("Location: ")
    row["NumReg"] = input("Number of Registers: ")
    row["Types"] = input("Types of Items: ").split(" ")

    for i in range(len(row["Types"])):
        query1 = "INSERT INTO HASTYPE(StoreID, TypesOfItems) VALUES('%s', '%s')" %( row["StoreID"], row["Types"][i])
        cur.execute(query1)
        con.commit()


    query2 = "INSERT INTO STORE(StoreID, Location, NumOfRegisters) VALUES('%s', '%s', '%d')" %(row["StoreID"], row["Location"], int(row["NumReg"]))

    cur.execute(query2)
    con.commit()
    return

def newCustomer():
    global cur
    row = {}
    print("Enter new customer's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")

    for i in range(len(row["Phone"])):
        query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], int(row["Phone"][i]))
        cur.execute(query1)
        con.commit()

    query2 = "INSERT INTO CUSTOMER(HRID) VALUES('%s')" %(row["HRID"])

    cur.execute(query2)
    con.commit()
    return

def buyRegister():
    global cur
    row = {}
    print("Enter new register's details: ")
    row["StoreID"] = input("Store ID: ")
    row["CashierIDs"] = input("Cashier IDs: ").split(" ")
    row["ManagerID"] = input("Manager ID: ")

    #calculate register no as regNo here
    query = "SELECT NumOfRegisters FROM STORE WHERE StoreID='%s' " %(row["StoreID"])
    cur.execute(query)
    calcRegNo = cur.fetchall()
    RegNo=int(calcRegNo[0][0])+1


    for i in range(len(row["CashierIDs"])):
        query1 = "INSERT INTO REGISTER(StoreID, RegisterNumber, CashierHRID, ManagerHRID) VALUES('%s', '%d', '%s', '%s')" %(row["StoreID"], RegNo, row["CashierIDs"][i], row["ManagerID"])
        cur.execute(query1)
        con.commit()

    query2 = "UPDATE STORE SET NumOfRegisters='%d' WHERE StoreID='%s' " %( RegNo, row["StoreID"])

    cur.execute(query2)
    con.commit()
    return

def newSale():
    global cur
    row = {}
    print("Enter new sale details: ")
    row["SaleID"] = input("Sale ID: ")
    row["StoreID"] = input("Store ID: ")
    row["Credit"] = input("Percentage Credit: ")
    row["Start"] = input("Start Date (YYYY-MM-DD): ")
    row["End"] = input("End Date (YYYY-MM-DD): ")

    query2 = "INSERT INTO SALE(SaleID, StoreID, PercentageCredit, StartDate, EndDate) VALUES('%s', '%s', '%d', '%s', '%s')" %(row["SaleID"], row["StoreID"], int(row["Credit"]), row["Start"], row["End"])

    cur.execute(query2)
    con.commit()
    return

def newPurchase():
    global cur
    row = {}
    print("Enter new purchase details: ")
    row["CustID"] = input("Customer HR ID: ")
    row["ItemIDs"] = input("Item IDs: ").split(" ")
    row["EmployeeID"] = input("Employee HR ID: ")
    row["StoreID"] = input("Store ID: ")
    row["SaleID"] = input("Sale ID: ")
    sumans = 0
    for i in range(len(row["ItemIDs"])):
        query1 = "INSERT INTO PURCHASES(CustomerHRID, ItemID, EmployeeHRID, StoreID, SaleID) VALUES('%s', '%s', '%s', '%s', '%s')" %(row["CustID"], row["ItemIDs"][i], row["EmployeeID"], row["StoreID"], row["SaleID"])
        cur.execute(query1)
        con.commit()

        query = "SELECT Name FROM ITEM WHERE ItemID='%s' " %(row["ItemIDs"][i])
        cur.execute(query)
        itemname = cur.fetchall()
        itemname = str(itemname[0][0])

        query2 = "INSERT INTO BOUGHT(CustomerHRID, ItemName) VALUES('%s', '%s')" %(row["CustID"], itemname)
        cur.execute(query2)
        con.commit()

        query3 = "SELECT Profit FROM ITEM WHERE ItemID='%s' " %(row["ItemIDs"][i])
        cur.execute(query3)
        profit=cur.fetchall()
        profit=int(profit[0][0])
        sumans = sumans+profit

    query4 = "SELECT PercentageCredit FROM SALE WHERE SaleID='%s'" %(row["SaleID"])
    cur.execute(query4)
    Credit=cur.fetchall()
    Credit=int(Credit[0][0])

    query5 = "SELECT StoreCredit FROM CUSTOMER WHERE HRID='%s'" %(row["CustID"])
    cur.execute(query5)
    curCredit=cur.fetchall()
    print(curCredit)
    curCredit=float(curCredit[0][0])

    query6 = "UPDATE CUSTOMER SET StoreCredit='%d' WHERE HRID='%s'" %(curCredit+Credit*profit/100,row["CustID"])
    cur.execute(query6)
    con.commit()

    query7 = "SELECT RegisterNumber FROM REGISTER WHERE CashierHRID='%s'" %(row["EmployeeID"])
    cur.execute(query7)
    regno=cur.fetchall()
    regno=int(regno[0][0])
    query8= "UPDATE REGISTER SET TotalProfit=TotalProfit+'%d' WHERE RegisterNumber='%s' AND StoreID='%s'" %(sumans, regno, row["StoreID"]) 
    cur.execute(query8)
    con.commit()
    return


def addSupervisor():
    global cur
    row = {}
    print("Enter New Supervisor's and Supervisee's details: ")
    row["EmpHRID"] = input("Supervisee HR ID: ")
    row["SuperHRID"] = input("Supervisor HR ID: ")


    query2 = "INSERT INTO SUPERVISES(CashierHRID, SupervisorHRID) VALUES('%s', '%s')" %(row["EmpHRID"], row["SuperHRID"])
    cur.execute(query2)
    con.commit()
    return


#Removing and deleting fns
def closeStore():
    global cur
    row = {}
    row["StoreID"] = input("Enter Store ID to close: ")

    query1 = "DELETE FROM STORE WHERE StoreID='%s' " %(row["StoreID"])
    cur.execute(query1)
    con.commit()

    query2 = "DELETE FROM HAS WHERE StoreID='%s' " %(row["StoreID"])
    cur.execute(query2)
    con.commit()

    query3 = "UPDATE EMPLOYEE SET StoreID='000' WHERE StoreID='%s' " %(row["StoreID"])
    cur.execute(query3)
    con.commit()

    query4 = "DELETE FROM REGISTER WHERE StoreID='%s' " %(row["StoreID"])
    cur.execute(query4)
    con.commit()

    query5 = "DELETE FROM SALE WHERE StoreID='%s' " %(row["StoreID"])
    cur.execute(query5)
    con.commit()

    query6 = "DELETE FROM HASTYPE WHERE StoreID='%s' " %(row["StoreID"])
    cur.execute(query6)
    con.commit()


    return

def fireEmp():
    global cur
    row = {}
    row["HRID"] = input("Enter Employee HR ID to remove: ")

    query1 = "DELETE FROM EMPLOYEE WHERE HRID='%s' " %(row["HRID"])
    cur.execute(query1)
    con.commit()

    query2 = "DELETE FROM HR WHERE HRID='%s' " %(row["HRID"])
    cur.execute(query2)
    con.commit()

    query3 = "DELETE FROM REGISTER WHERE CashierHRID='%s' " %(row["HRID"])
    cur.execute(query3)
    con.commit()

    query4 = "UPDATE REGISTER SET ManagerHRID='00000' WHERE ManagerHRID='%s' " %(row["HRID"])
    cur.execute(query4)
    con.commit()


    query5 = "DELETE FROM SUPERVISES WHERE CashierHRID='%s' " %(row["HRID"])
    cur.execute(query5)
    con.commit()

    query6 = "UPDATE SUPERVISES SET SupervisorHRID='00000' WHERE SupervisorHRID='%s' " %(row["HRID"])
    cur.execute(query6)
    con.commit()

    return

def removeSale():
    row = {}
    row["SaleID"] = input("Enter Sale ID to delete: ")

    query1 = "DELETE FROM SALE WHERE SaleID='%s' " %(row["SaleID"])
    cur.execute(query1)
    con.commit()

    return

def removeItemFromStore():
    row = {}
    row["StoreID"] = input("Enter Store ID: ")
    row["ItemName"] = input("Enter Item Name: ")


    query1 = "DELETE FROM HAS WHERE StoreID='%s' AND ItemName='%s'" %(row["StoreID"],row["ItemName"])
    cur.execute(query1)
    con.commit()



    return

#Modification fns

def modifyItem():
    global cur
    row = {}
    print("Enter item's details: ")
    row["ItemID"] = input("Item ID: ")
    row["ItemNo"] = input("New Item Number: ")
    row["CP"] = input("New Item Cost Price: ")
    row["SP"] = input("New Item Sell Price: ")
    row["Locations"] = input("Store IDs of New Locations: ").split(" ")

    query = "SELECT Name FROM ITEM WHERE ItemID='%s' " %(row["ItemID"])
    cur.execute(query)
    Name = cur.fetchall()
    Name=str(Name[0][0])
    query="DELETE FROM HAS WHERE ItemName='%s'" %(Name)
    cur.execute(query)
    con.commit()

    for i in range(len(row["Locations"])):
        query1 = "INSERT INTO HAS(StoreID, ItemName) VALUES('%s', '%s')" %(row["Locations"][i], Name)
        cur.execute(query1)
        con.commit()

    query2 = "UPDATE ITEM SET ItemNumber='%d', ItemCostPrice='%d', ItemSalePrice='%d' WHERE ItemID='%s'" %(int(row["ItemNo"]), int(row["CP"]), int(row["SP"]), row["ItemID"])

    cur.execute(query2)
    con.commit()
    return

def modifyCustomerDetails():
    global cur
    row = {}
    print("Enter Customer's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("New Name: ")
    row["Email"] = input("New Email Address: ")
    row["Phone"] = input("New Phone Numbers: ").split(" ")


    query1 = "DELETE FROM HR WHERE HRID='%s'" %(row["HRID"])
    cur.execute(query1)
    con.commit()

    for i in range(len(row["Phone"])):
        query2 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], int(row["Phone"][i]))
        cur.execute(query2)
        con.commit()

    return

def modifyEmpDetails():
    global cur
    row = {}
    print("Enter Employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("New Name: ")
    row["Email"] = input("New Email Address: ")
    row["Phone"] = input("New Phone Numbers: ").split(" ")
    row["StoreID"] = input("New Store ID: ")
    row["Type"] = input("New Type of Employee: ")
    row["Salary"] = float(input("New Salary: "))

    query1 = "DELETE FROM HR WHERE HRID='%s'" %(row["HRID"])
    cur.execute(query1)
    con.commit()

    for i in range(len(row["Phone"])):
        query2 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], int(row["Phone"][i]))
        cur.execute(query2)
        con.commit()

    query3 = "UPDATE EMPLOYEE SET StoreID='%s', TypeOfEmployee='%s', Salary='%d' WHERE HRID='%s'" %( row["StoreID"], row["Type"], int(row["Salary"]), row["HRID"])
    cur.execute(query3)
    con.commit()
    return

def modifyRegister():
    global cur
    row = {}
    print("Enter Register details: ")
    print("Enter new register's details: ")
    row["StoreID"] = input("Store ID: ")
    row["RegID"] = input("Register Number: ")
    row["CashierIDs"] = input("New Cashier IDs: ").split(" ")
    row["ManagerID"] = input("New Manager ID: ")


    query1 = "DELETE FROM REGISTER WHERE StoreID='%s' AND RegisterNumber='%d'" %(row["StoreID"], int(row["RegID"]))
    cur.execute(query1)
    con.commit()

    for i in range(len(row["CashierIDs"])):
        query2 = "INSERT INTO REGISTER(StoreID, RegisterNumber, CashierHRID, ManagerHRID) VALUES('%s', '%d', '%s', '%s')" %(row["StoreID"], int(row["RegID"]), row["CashierIDs"][i], row["ManagerID"])
        cur.execute(query2)
        con.commit()
    return

def modifySale():
    global cur
    row = {}
    print("Enter Sale details: ")
    row["SaleID"] = input("Sale ID: ")
    row["StoreID"] = input("New Store ID: ")
    row["Credit"] = input("New Percentage Credit: ")
    row["Start"] = input("New Start Date (YYYY-MM-DD): ")
    row["End"] = input("New End Date (YYYY-MM-DD): ")

    query2 = "UPDATE SALE SET StoreID='%s', PercentageCredit='%s', StartDate='%s', EndDate='%s' WHERE SaleID='%s'" %(row["StoreID"], row["Credit"], row["Start"], row["End"], row["SaleID"])

    cur.execute(query2)
    con.commit()
    return

def changeSupervisor():
    global cur
    row = {}
    print("Enter Supervisor's and Supervisee's details: ")
    row["EmpHRID"] = input("Supervisee HR ID: ")
    row["SuperHRID"] = input("Supervisor HR ID: ")


    query2 = "UPDATE SUPERVISES SET SupervisorHRID='%s' WHERE CashierHRID='%s' " %(row["SuperHRID"], row["EmpHRID"])
    cur.execute(query2)
    con.commit()
    return

def changeTypes():
    global cur
    row = {}
    print("Enter Store's details: ")
    row["StoreID"] = input("Store ID: ")
    row["Types"] = input("Types of Items Carried ").split(" ")


    query1 = "DELETE FROM HASTYPE WHERE StoreID='%s'" %(row["StoreID"])
    cur.execute(query1)
    con.commit()

    for i in range(len(row["Types"])):
        query2 = "INSERT INTO HASTYPE(StoreID, TypesOfItems) VALUES('%s', '%s')" %( row["StoreID"], row["Types"][i])
        cur.execute(query2)
        con.commit()

    return




#Update and show fns

def updateManagerSalary():
    global cur
    row = {}
    query1 = "SELECT HRID FROM EMPLOYEE WHERE TypeOfEmployee='Manager'"
    cur.execute(query1)
    Managers=cur.fetchall()
    
    for i in range(len(Managers)):
        query="SELECT SUM(TotalProfit) FROM REGISTER WHERE ManagerHRID='%s'" %(Managers[i])
        cur.execute(query)
        managerSalary=cur.fetchall()
        managerSalary=float(managerSalary[0][0])
        query2="UPDATE EMPLOYEE SET Salary='%d' WHERE HRID='%s'" %(managerSalary*0.2, Managers[i][0])
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
    blah=int(blah[0][0])
    print (blah)
    return

def showStoreItems():
    global cur
    storeID=input("Enter Store ID: ");

    query2 = "SELECT * FROM HAS WHERE StoreID='%s'" %(storeID)

    cur.execute(query2)
    blah = cur.fetchall()
    for value in blah:
        print (value)

    return



def showCustomerCredits():
    global cur
    CustID=input("Enter Customer HRID: ")
    query2 = "SELECT StoreCredit FROM CUSTOMER WHERE HRID='%s'" %(CustID)

    cur.execute(query2)
    blah = cur.fetchall()
    blah=int(blah[0][0])
    print(blah)
    return

def checkNowSales():
    global cur
    today=date.today()
    query="SELECT * FROM SALE WHERE '%s' BETWEEN StartDate AND EndDate"
    cur.execute(query)
    salesNow=cur.fetchall()
    for i in range(len(salesNow)):
        print(salesNow[i])
    return


def checkSuperviseeSalaryProfit():
    global cur
    id=input("Enter your HRID: ")
    empid=input("Enter supervisee's HRID: ")

    query = "SELECT A.Salary FROM EMPLOYEE A, SUPERVISES B WHERE B.CashierHRID='%s' AND B.SupervisorHRID='%s' AND B.CashierHRID=A.HRID" %(empid, id)
    cur.execute(query)
    superviseeSalary = cur.fetchall()
    for i in range(len(superviseeSalary)):
        print(superviseeSalary[i][0])
    if len(superviseeSalary) == 0:
        print("This employee is not your supervisee")
    return

def checkMySalary():
    global cur
    id=input("Enter HRID whose salary you want to see:")

    query = "SELECT Salary FROM EMPLOYEE WHERE HRID = '%s'" %(id)
    cur.execute(query)
    blah = cur.fetchall()
    print (blah)

    blah=int(blah[0][0])
    print (blah)
    return


optionFunctionMapping = {
    1: hireEmp,
    2: addItem,
    3: openStore,
    4: newCustomer,
    5: buyRegister,
    6: newSale,
    7: newPurchase,
    8: addSupervisor,
    9: closeStore,
    10: fireEmp,
    11: removeSale,
    12: removeItemFromStore,
    13: modifyItem,
    14: modifyCustomerDetails,
    15: modifyEmpDetails,
    16: modifyRegister,
    17: modifySale,
    18: changeSupervisor,
    19: changeTypes,
    20: updateManagerSalary,
    21: reportProfit,
    22: showStoreItems,
    23: showCustomerCredits,
    24: checkNowSales,
    25: checkSuperviseeSalaryProfit,
    26: checkMySalary
}

while(1):

        username = input("Username: ")
        password = input("Password: ")

        try:
            tmp = sp.call('clear',shell=True)
            con = pymysql.connect("localhost",username,password,"FRANCHISE");


            cur = con.cursor()
            while(1):
                print("1. Hire a new employee")
                print("2. Add an item")
                print("3. Open a store")
                print("4. Add a customer")
                print("5. Buy a register")
                print("6. Add a sale")
                print("7. Add a purchase")
                print("8. Add a Supervisor")
                print("9. Close a Store")
                print("10. Fire an employee")
                print("11. Remove a sale")
                print("12. Remove an item from a store")
                print("13. Modify details of an item")
                print("14. Modify details of a customer")
                print("15. Modify details of an employee")
                print("16. Modify details of a register")
                print("17. Modify details of a sale")
                print("18. Change a supervisor")
                print("19. Change types of items carried by a store")
                print("20. Update the managers' salaries")
                print("21. Report store's profits")
                print("22. Show items available in a store")
                print("23. Show store credits for a customer")
                print("24. Check sales going on now")
                print("25. Check supervisee's salary and profit")
                print("26. Check own salary")
                print("27. Logout")

                c = int(input("Enter choice> "))
                if(c==27):
                    break
                else:
                    optionFunctionMapping[c]()
                    


        except:
            tmp = sp.call('clear',shell=True)
            print("Error in executing command")
            tmp = input("Enter any key to CONTINUE>")



