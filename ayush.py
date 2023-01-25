import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="8084",database="facebook")
curs =conn.cursor()

# if conn.is_connected():
#     print("Connection Sucessful")

while 1>0:
    
    user = input("Enter 1 to Sign Up \nEnter 2 to Login\n")
    if user=="1":
        name = input("Enter Your Name : ")
        Mobile = input("Enter Mobile Number : ")
        passwd = input("Enter Password : ")

        query = "INSERT INTO user_Data(Name,Mobile_no,Passwd) VALUES('{}','{}','{}')".format(name,Mobile,passwd)
        curs.execute(query)
        conn.commit()

        var = input("Want to Add More ..   Y or N : ")
        if var=="N" or var=="n":
            break

    # query = "ALTER TABLE user_Data MODIFY COLUMN Mobile_No int NOT NULL PRIMARY KEY"
    # curs.execute(query)
    # conn.commit()

    elif user=="2":
    
        no = input("Enter the Number : ")
        passwd = input("Enter Password : ")
        tple = [(no,passwd)]

        query = "SELECT Mobile_no , Passwd FROM User_Data WHERE Mobile_no = '{}' AND Passwd = '{}'".format(no,passwd)
        curs.execute(query)
        confirm = curs.fetchall()


        if confirm==tple:
            print("You are Logged in.....")

        else :
            print("Your Login Credential are invalid . Try Again ....")    

         

    
