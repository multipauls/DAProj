import subprocess as sp
import pymysql
import pymysql.cursors

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

