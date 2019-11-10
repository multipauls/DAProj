import pymysql

connection = pymysql.connect("localhost","root","","LEARN");
cursor = connection.cursor();

sql_query = "SELECT VERSION()";

try:
    cursor.execute(sql_query);
    data = cursor.fetchone();
    print("DB Version: %s" %data);

except Exception as e:
    print("Exception: ",e);

connection.close();
