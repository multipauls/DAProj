import subprocess as sp
import pymysql
import pymysql.cursors

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

    query = "SELECT ItemName FROM Item WHERE ItemID='%s' " %(row["ItemID"])
    cur.execute(query)
    Name = cur.fetchall()
    Name=string(Name[0])

    query="DELETE FROM HAS WHERE ItemName='%s'" %(Name)
    cur.execute(query)
    con.commit()

    for i in range(len(row["Locations"])):
        query1 = "INSERT INTO HAS(StoreID, ItemName) VALUES('%s', '%s')" %(row["Locations"][i], Name)
        cur.execute(query1)
        con.commit()

    query2 = "UPDATE ITEM SET ItemNumber='%d', ItemCostPrice='%d', ItemSellPrice='%d' WHERE ItemID='%s'" %(row["ItemNo"], row["CP"], row["SP"], row["ItemID"])

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
        query2 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
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
	    query2 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query2)
    	con.commit()

    query3 = "UPDATE EMPLOYEE SET StoreID='%s', TypeOfEmployee='%s', SALARY='%d' WHERE HRID='%s'" %( row["StoreID"], row["Type"], row["Salary"], row["HRID"])
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


    query1 = "DELETE FROM REGISTER WHERE HRID='%s'" %(row["HRID"])
    cur.execute(query1)
    con.commit()

    for i in range(len(row["CashierIDs"])):
        query2 = "INSERT INTO REGISTER(StoreID, RegisterNumber, CashierHRID, ManagerHRID) VALUES('%s', '%d', '%s', '%s')" %(row["StoreID"], row["RegID"], row["CashierIDs"][i], row["ManagerID"])
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

    query2 = "UPDATE SALE SET StoreID='%s', PercentageCredit='%s', StartDate='%s', EndDate='%d' WHERE SaleID='%s'" %(row["StoreID"], row["Credit"], row["StartDate"], row["EndDate"], row["SaleID"])

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
    

    query1 = "DELETE FROM HASTYPES WHERE StoreID='%s'" %(row["StoreID"])
    cur.execute(query1)
    con.commit()

   for i in range(len(row["Types"])):
        query2 = "INSERT INTO HASTYPE(StoreID, TypesOfItems) VALUES('%s', '%s')" %( row["StoreID"], row["Types"][i])
        cur.execute(query2)
        con.commit()   

    return
