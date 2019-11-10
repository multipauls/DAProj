import pymysql
connection = pymysql.connect("localhost","root","","LEARN");
cursor = connection.cursor();

delete_existing_table = "Drop table if exists employee";

create_table_query = """CREATE TABLE EMPLOYEE(
        id int auto_increment primary key,
        name varchar(20) not null
)""";

try:
    cursor.execute(delete_existing_table);
    print("Existing table has been deleted");
    cursor.execute(create_table_query);
    print("Employee table has been created!");

except Exception as e:
    print("Exception occurred: ",e);

connection.close();
