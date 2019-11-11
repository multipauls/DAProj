
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
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='FRANCHISE',
                cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
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
                tmp = sp.call('clear',shell=True)
                if c==27:
                    break
                else:
                    send(optionFunctionMapping[c]())


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
   
