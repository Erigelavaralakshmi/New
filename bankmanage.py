import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="root123@",port="3306",autocommit=True)
my_cursor = conn.cursor()

my_cursor.execute("create database if not exists bank_db")
my_cursor.execute("use bank_db")
#creating tables
my_cursor.execute(
    "create table if not exists bank_account(acc_no int primary key auto_increment,name varchar(30),city char(20),mobile_no char(10),balance int(6))")
my_cursor.execute(
    "create table if not exists user_transaction(acc_no int,amount int(6),dp int(6),ttype char(1),foreign key(acc_no) references bank_account(acc_no))")
while True:
    print("1.Create account    2.Deposit money   3.Withdraw money   4.View account details   5.Exit")
    ch = int(input("Enter your choice: "))
    
    #create new account
    if ch == 1:
        name = input("Enter your name: ")
        city = input("Enter city name: ")
        mn = input("Enter mobile no: ")
        balance = 0
        sql = "insert into bank_account(name,city,mobile_no,balance) values (%s, %s, %s, %s)"
        val = (name, city, mn, balance)
        my_cursor.execute(sql,val)
        my_cursor.execute("select * from bank_account where name='" + name + "'")
        print("Account is successfully created! " )
        for i in my_cursor:
            print(i)
    
    # Transaction or deposit money
    elif ch == 2:
        accno = input("Enter account number: ")
        dp = int(input("Enter amount to be deposited: "))
        ttype = "d"
        
        query = "INSERT INTO user_transaction(acc_no, amount, ttype) VALUES (%s, %s, %s)"
        values = (accno, dp, ttype)
        my_cursor.execute(query, values)

        # my_cursor.execute("insert into user_transaction values('" + accno + "','" + str(dp) + "','" + ttype + "')")
        # my_cursor.execute("update bank_account set balance=balance+'" + str(dp) + "' where acc_no='" + accno + "'")
        print("Rs.",dp, " has been deposited successfully in account no: ", accno)
    
    #Withdraw money
    elif ch == 3:
        accno = input("Enter a account number: ")
        wd = int(input("Enter amount to be withdraw: "))
        select_Query = "select balance from bank_account where acc_no = '" + accno +"' "
        my_cursor.execute(select_Query)
        bal = my_cursor.fetchone()[0]
        if wd < bal:
            ttype = "w"
            my_cursor.execute("insert into user_transaction values('" + accno + "','" + str(wd) + "', " + ttype + "')")
            my_cursor.execute("update bank_account set balance=balance-'" + str(wd) + "' where acc_no='" + accno + "'")
            print("Rs", wd, " has been withdraw successfully from account no ", accno)
        else:
            print("can't withdraw money due ti insufficient balance! ")
    
    # Display account details
    elif ch == 4:
        accno = input("Enter account number: ")
        my_cursor.execute("select * from bank_account where acc_no='" + accno + "'")
        for i in my_cursor:
            print(i)
    else:
        break










