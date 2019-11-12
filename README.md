# STORE FRANCHISE DATABASE
 Database Name: FRANCHISE
## Entities:
- Items
- Stores
- HR
	- Employees
	- Customers
- Registers
- Sales

## Relationships:
- BOUGHT
- ISTYPE
- HASTYPE
- HAS
- PURCHASES
- SUPERVISES

## Setup for IDs:
- ItemID: 6 characters long
- StoreID: 3 characters long
- SaleID: 6 characters long
- HRID: 5 characters long

## Defaults
- StoreCredit for Customers: 0
- TypeOfEmployee for Employees: New Hire
- Salary for Employees: 5000
- TotalProfit for Register: 0
- PercentageCredit for Sale: 0
- SupervisorHRID for Supervises: 00000
All other values must be user defined