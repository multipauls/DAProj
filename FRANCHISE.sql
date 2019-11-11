CREATE DATABASE IF NOT EXISTS FRANCHISE;

USE FRANCHISE;

CREATE TABLE IF NOT EXISTS ITEM (ItemID VARCHAR(6) PRIMARY KEY NOT NULL, Name VARCHAR(20) NOT NULL, ItemNumber INT, ItemCostPrice INT, ItemSalePrice INT, Profit INT AS (ItemSalePrice - ItemCostPrice));


CREATE TABLE IF NOT EXISTS STORE (StoreID VARCHAR(3) PRIMARY KEY NOT NULL, Location VARCHAR(30) NOT NULL, NumOfRegisters INT);

CREATE TABLE IF NOT EXISTS HR (HRID VARCHAR(5) NOT NULL, Name VARCHAR(30) NOT NULL, Email VARCHAR(50), PhoneNumber INT(10) NOT NULL, PRIMARY KEY (HRID, PhoneNumber)); 

CREATE TABLE IF NOT EXISTS EMPLOYEE (HRID VARCHAR(5) NOT NULL PRIMARY KEY, StoreID VARCHAR(3) NOT NULL, TypeOfEmployee VARCHAR(20) DEFAULT 'New Hire', Salary INT DEFAULT 5000);

CREATE TABLE IF NOT EXISTS CUSTOMER (HRID VARCHAR(5) NOT NULL PRIMARY KEY, StoreCredit INT DEFAULT 0);

CREATE TABLE IF NOT EXISTS REGISTER (StoreID VARCHAR(3) NOT NULL, RegisterNumber INT NOT NULL, CashierHRID VARCHAR(5) NOT NULL, ManagerHRID VARCHAR(5) NOT NULL, TotalProfit INT DEFAULT 0, PRIMARY KEY (StoreID, RegisterNumber, CashierHRID));

CREATE TABLE IF NOT EXISTS SALE (SaleID VARCHAR(6) NOT NULL PRIMARY KEY, StoreID VARCHAR(3) NOT NULL, PercentageCredit INT DEFAULT 0, StartDate DATE NOT NULL, EndDate DATE NOT NULL);

CREATE TABLE IF NOT EXISTS HAS (StoreID VARCHAR(3) NOT NULL, ItemName VARCHAR(20) NOT NULL, PRIMARY KEY(StoreID, ItemName));

CREATE TABLE IF NOT EXISTS BOUGHT (CustomerHRID VARCHAR(5) NOT NULL, ItemName VARCHAR(20) NOT NULL, PRIMARY KEY (CustomerHRID, ItemName));

CREATE TABLE IF NOT EXISTS SUPERVISES (SupervisorHRID VARCHAR(5) NOT NULL DEFAULT '00000', CashierHRID VARCHAR(5) NOT NULL PRIMARY KEY);

CREATE TABLE IF NOT EXISTS PURCHASES (CustomerHRID VARCHAR(5) NOT NULL, ItemID VARCHAR(6) NOT NULL, EmployeeHRID VARCHAR(5) NOT NULL, StoreID VARCHAR(3) NOT NULL, SaleID VARCHAR(6) NOT NULL, PRIMARY KEY (CustomerHRID, ItemID, EmployeeHRID, StoreID, SaleID));

CREATE TABLE IF NOT EXISTS ISTYPE (ItemID VARCHAR(6) NOT NULL, TypeOfItem VARCHAR(20), PRIMARY KEY (ItemID, TypeOfItem));

CREATE TABLE IF NOT EXISTS HASTYPE (StoreID VARCHAR(3) NOT NULL, TypesOfItems VARCHAR(20), PRIMARY KEY (StoreID, TypesOfItems));

