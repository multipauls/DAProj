import subprocess as sp
import pymysql
import pymysql.cursors



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

    query6 = "UPDATE SUPERVISES SET SuperviserHRID='00000' WHERE SuperviserHRID='%s' " %(row["HRID"])
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
