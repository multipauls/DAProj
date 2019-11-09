# CS4.301-Data-and-Applications-Project-Template

This repository will serve as a template for the aformentiontioned course project. The instructions and tools given here are compatible with python 3.X. The corresponding instructions and toold for python 2 have already been provided in the course moodle page

## Installation Instructions

I trust that the students reading this are all at a respectable age to be able to handle installation bugs themselves and won't be needing the TAs to help them. 

### MySQL

Although you haven't been strictly been told to explicitly use MySQL it is highly recommended. To install MySQL server on Ubuntu, run the following commands

```
sudo apt-get update
sudo apt-get install mysql-server
```

When installing the MySQL server for the first time, it will prompt for a root password that you can later login with. 

The start command is
```
mysql -u <user_name> -p <password>
```

If for some reason, you aren't asked for the password during installation, try prepending the start command with sudo and provide your root password. You can now set a root password or create a new user. 

Here, I would also like to point out that if your application involves a login or some form of authentication, you may do so using the USER table of the MYSQL database that exists by default. 

To create a new user, you may use the following command
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```
At this stage the created user doesn't have access to the data. To allow access, you'll have to run a grant access query as below
```
GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
```

With this you must be in a place to be able to place around with MySQL. Since this template has been made to work on top of the COMPANY dataset, proceed to load the dataset using the following command within the mysql environment
```
source path_to_COMPANY.sql;
```

### PyMySQL

Again although you weren't explicitly told to use PyMySQL it is recommended that you do.

That being said, **YOU CANNOT USE PANDAS OR OTHER PYTHON LIBRARIES TO DO THIS PROJECT**

PyMySQL is an interface for connection to the MySQL server from Python.

To install PyMySQL, you can use one of the two routes  
**Pip**
```
pip install PyMySQL
```
**Conda**
```
conda install -c anaconda pymysql
```

## Boiler Plate

In this section, I will explain the boiler plate to the best of my abilities and also explain what is required of you.

### UI Interface
Due to the timeline, you are not expected to implement a graphical UI (although you aren't disallowed either). A CLI (Command Line Interface) will do for the sake of the project

You can also have different interfaces depending on which kind of user logged in to your software. Under the assumption that someone from adminstration logged into mine, the UI for the boiler plate looks something like this
```
1. Hire a new employee
2. Fire an employee
3. Promote an employee
4. Reward a department 
5. Project Statistics
6. Department Statistics
7. Employee Statistics
8. Check messages

Enter Choice > 
```

These options perform the following functions
* Hire a new employee - The function performs the task of hiring a new employee, from taking in the details to inseting relevant rows

* Fire an employee - similar to hiring one except it technically removes all relevant rows

* Promote an employee - Updates the position (makes employee a supervisor or maybe a manager) and also possibly increases the salary

* Reward a department - Increases the salary of a whole department by some user specified x%

* Project Statistics - Given the project number, the function displays a statistical report showing how much money and time is spent on each project per department.

* Department Statistics - Given a department number, this fuction displays a report showing how productive this department is given the amount of money spent for each project 

* Employee Statistics - Given an employee ESSN, this function displays a report showing how much time this employee spends on each project and how much the company spends on this employee wrt the amount of salary he is being paid

* Check messages - An email like feature on the local server. To show the working of this feature you may locally open two instances of the software, that is if you choose to implement it. This may be relaxed.

Since the orignal database didn't support messaging functionality, another table called MESSAGES is included. To create this table just run
```
CREATE TABLE MESSAGES( 
    Essn1 CHAR(9) NOT NULL, 
    Essn2 CHAR(9) NOT NULL, 
    Timestamp TIMESTAMP NOT NULL, 
    Message VARCHAR(1000), 
    PRIMARY KEY(Essn1, Essn2, Timestamp), 
    FOREIGN KEY (Essn1) REFERENCES EMPLOYEE(Ssn)
    FOREIGN KEY(Essn2) REFERENCES EMPLOYEE(Ssn) );
    
```

## Resources


