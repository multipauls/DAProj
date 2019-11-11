import pymysql

connection = pymysql.connect("localhost","mona","password","FRANCHISE");
cursor = connection.cursor();

sql_query = "SELECT * FROM CUSTOMER";

try:
    cursor.execute(sql_query);
    data = cursor.fetchall();
    print("DB Version: %s" %data);

except Exception as e:
    print("Exception: ",e);

connection.close();
