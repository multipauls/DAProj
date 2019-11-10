import subprocess as sp
import pymysql
import pymysql.cursors



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



