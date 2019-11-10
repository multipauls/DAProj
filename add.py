import subprocess as sp
import pymysql
import pymysql.cursors


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
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["Salary"])

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
    row["Types"] = input("Types of Item").split(" ")
    row["Locations"] = input("Store IDs of Locations: ").split(" ")

    for i in range(len(row["Locations"])):
	    query1 = "INSERT INTO HAS(StoreID, ItemName) VALUES('%s', '%s')" %( row["Locations"][i], row["Name"])
    	cur.execute(query1)
    	con.commit()

    for i in range(len(row["Types"])):
        query2 = "INSERT INTO ISTYPE(ItemID, TypesOfItems) VALUES('%s', '%s')" %( row["ItemID"], row["Types"][i])
        cur.execute(query2)
        con.commit()

    query3 = "INSERT INTO ITEM(ItemID, Name, ItemNumber, ItemCostPrice, ItemSalePrice) VALUES('%s', '%s', '%d', '%d', '%d')" %(row["ItemID"], row["Name"], row["ItemNo"], row["CP"], row["SP"])

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
    row["Types"] = input("Types of Items").split(" ")

    for i in range(len(row["Types"])):
        query1 = "INSERT INTO HASTYPE(StoreID, TypesOfItems) VALUES('%s', '%s')" %( row["StoreID"], row["Types"][i])
        cur.execute(query1)
        con.commit()


    query2 = "INSERT INTO STORE(StoreID, Location, NumOfRegisters) VALUES('%s', '%s', %d')" %(row["StoreID"], row["Location"], row["NumReg"])

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
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
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
    RegNo=int(calcRegNo[0])+1


    for i in range(len(row["CashierIDs"])):
	    query1 = "INSERT INTO REGISTER(StoreID, RegisterNumber, CashierHRID, ManagerHRID) VALUES('%s', '%d', '%s', '%s')" %(row["StoreID"], regNo, row["CashierIDs"][i], row["ManagerID"])
    	cur.execute(query1)
    	con.commit()

    query2 = "UPDATE STORE SET NumOfRegisters='%d' WHERE StoreID='%s' " %( regNo, row["StoreID"])

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

    query2 = "INSERT INTO SALE(SaleID, StoreID, PercentageCredit, StartDate, EndDate) VALUES('%s', '%s', '%d', '%s', '%s')" %(row["SaleID"], row["StoreID"], row["Credit"], row["Start"], row["End"])

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
    sum = 0
    for i in range(len(row["ItemIDs"])):
	    query1 = "INSERT INTO PURCHASES(CustomerHRID, ItemID, EmployeeHRID, StoreID, SaleID) VALUES('%s', '%s', '%s', '%s', '%s')" %(row["CustID"], row["ItemIDs"][i], row["EmployeeID"], row["StoreID"], row["SaleID"])
    	cur.execute(query1)
    	con.commit()

    	query = "SELECT ItemName FROM ITEM WHERE ItemID='%s' " %(row["ItemIDs"][i])
    	cur.execute(query)
    	itemname = cur.fetchall()
    	itemname = string(itemname[0])
    	
    	query2 = "INSERT IGNORE INTO BOUGHT(CustomerHRID, ItemName) VALUES('%s', '%s')" %(row["CustID"], itemname)
    	cur.execute(query2)
    	con.commit()

		query3 = "SELECT Profit FROM ITEM WHERE ItemID='%s' " %(row["ItemIDs"][i])
		cur.execute(query3)
		profit=cur.fetchall()
		profit=int(profit[0])
		sum = sum+profit

	query4 = "SELECT PercentageCredit FROM SALE WHERE SaleID='%s'" %(row["SaleID"])
	cur.execute(query4)
	Credit=cur.fetchall()
	Credit=int(Credit[0])

	query5 = "SELECT StoreCredit FROM CUSTOMER WHERE HRID='%s'" %(row["CustID"])
	cur.execute(query5)
	curCredit=cur.fetchall()
	curCredit=float(curCredit[0])
	

	query6 = "UPDATE CUSTOMER SET StoreCredit='%d' WHERE HRID='%s'" %(curCredit+Credit*profit/100,row["CustID"])
	cur.execute(query6)
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