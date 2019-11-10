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

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

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
    row["Locations"] = input("Store IDs of Locations: ").split(" ")

    for i in range(len(row["Locations"])):
	    query1 = "INSERT INTO HAS(StoreID, ItemName) VALUES('%s', '%s')" %(row["Name"], row["Locations"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO ITEM(ItemID, Name, ItemNumber, ItemCostPrice, ItemSalePrice) VALUES('%s', '%s', '%d', '%d', '%d')" %(row["ItemID"], row["Name"], row["ItemNo"], row["CP"], row["SP"])

    cur.execute(query2)
    con.commit()
    return

def openStore():
    global cur
    row = {}
    print("Enter new store's details: ")
    row["StoreID"] = input("Store ID: ")
    row["Location"] = input("Location: ")
    row["NumReg"] = input("Number of Registers: ")

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

    #calc regno as regNo here

    for i in range(len(row["CashierIDs"])):
	    query1 = "INSERT INTO REGISTER(StoreID, RegisterNumber, CashierHRID, ManagerHRID) VALUES('%s', '%d', '%s', '%s')" %(row["StoreID"], regNo, row["CashierIDs"][i], row["ManagerID"])
    	cur.execute(query1)
    	con.commit()

    query2 = "UPDATE EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def newSale():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def newPurchase():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

#Removing and deleting fns
def closeStore():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def fireEmp():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def removeSale():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def removeItemFromStore():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

#Modification fns

def modifyItem():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def modifyCustomerDetails():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def modifyEmpDetails():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def modifyRegister():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return


 def modifySale():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def changeSuperviser():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def newCustomer():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

#Update and show fns

def updateSalaryProfit():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def reportProfit():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def showStoreItems():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def checkNowSales():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return


def checkSuperviseeSalaryProfit():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return

def checkMySalary():
    global cur
    row = {}
    print("Enter new employee's details: ")
    row["HRID"] = input("HR ID: ")
    row["Name"] = input("Name: ")
    row["Email"] = input("Email Address: ")
    row["Phone"] = input("Phone Numbers: ").split(" ")
    row["StoreID"] = input("Store ID: ")
    row["Type"] = input("Type of Employee: ")
    row["Salary"] = float(input("Salary: "))

    for i in range(len(row["Phone"])):
	    query1 = "INSERT INTO HR(HRID, Name, Email, PhoneNumber) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["Name"], row["Email"], row["Phone"][i])
    	cur.execute(query1)
    	con.commit()

    query2 = "INSERT INTO EMPLOYEE(HRID, StoreID, TypeOfEmployee, SALARY) VALUES('%s', '%s', '%s', '%d')" %(row["HRID"], row["StoreID"], row["Type"], row["SALARY"])

    cur.execute(query2)
    con.commit()
    return


optionFunctionMapping = {
    1: hireAnEmployee,
    2: fireAnEmployee,
    3: promoteEmployee,
    4: rewardDepartment,
    5: projectStatistics,
    6: departmentStatistics,
    7: employeeStatistics,
    8: checkMessages,
}

while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='COMPANY',
                cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Hire a new employee")
                print("2. Fire an employee")
                print("3. Promote an employee")
                print("4. Reward a department")
                print("5. Project Statistics")
                print("6. Department Statistics")
                print("7. Employee Statistics")
                print("8. Check messages")
                print("9. Logout")
                c = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if c==9:
                    break
                else:
                    send(optionFunctionMapping[c]())


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
   


