#!/usr/bin/env python3
import sqlite3
import random
from sqlite3 import Error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")
    try:
        sql = "DROP TABLE customer;"
        _conn.execute(sql)
        sql = "DROP TABLE car;"
        _conn.execute(sql)
        sql = "DROP TABLE branch;"
        _conn.execute(sql)
        sql = "DROP TABLE sales;"
        _conn.execute(sql)
        sql = "DROP TABLE rental;"
        _conn.execute(sql)
        sql = "DROP TABLE services;"
        _conn.execute(sql)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")
    try:
        sql ="""create table customer(
                ct_custkey INTEGER,
                ct_name TEXT, 
                ct_address TEXT, 
                ct_email TEXT, 
                ct_password TEXT, 
                PRIMARY KEY(ct_custkey)
                );"""
        _conn.execute(sql)
        sql ="""create table car(
                c_carkey INTEGER,
                c_custkey INTEGER,
                c_price INTEGER,
                c_brand TEXT,
                c_year INTEGER,
                c_titlestatus TEXT,
                c_mileage INTEGER,
                c_color TEXT,
                PRIMARY KEY(c_carkey)
                );"""
        _conn.execute(sql)
        sql ="""create table branch(
                b_branchkey INTEGER,
                b_custkey INTEGER,
                b_carkey INTEGER,
                b_serkey INTEGER,
                b_salekey INTEGER,
                b_rentkey INTEGER,
                b_location TEXT,
                PRIMARY KEY(b_branchkey)
                );"""
        _conn.execute(sql)
        sql ="""create table sales(
                sp_salekey INTEGER,
                sp_name TEXT,
                PRIMARY KEY(sp_salekey)
                );"""
        _conn.execute(sql)
        sql ="""create table rental(
                r_rentkey INTEGER,
                r_price INTEGER,
                r_pdate NUMERIC,
                r_ddate NUMERIC,
                PRIMARY KEY(r_rentkey)
                );"""
        _conn.execute(sql)
        sql ="""create table services(
                s_serkey INTEGER,
                s_price INTEGER,
                s_date TEXT,
                s_term TEXT,
                s_type TEXT,
                s_repair TEXT,
                s_workorder TEXT,
                PRIMARY KEY(s_serkey)
                );"""
        _conn.execute(sql)
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateCustomer(_conn):
    try:
        sql = '''INSERT INTO customer(ct_name,ct_address,ct_email,ct_password) 
                VALUES(?, ?, ?, ?);'''
        arg = [
            ('Hide', '123 Fake Street', 'fake@gmail.com', '12345'),
            ('Jill', '361 Manhattan Rd', 'roesch@yahoo.ca', 'jJys3m'),
            ('Jim', '138 North Hall St', 'uqmcolyv@gmail.com', 'BZRfhD'),
            ('Singh', '436 Wild Rose Drive', 'itstatus@icloud.com', 'jYfPKf'),
            ('Ivan', '667 South Blackburn St', 'fhirsch@verizon.net', 'cKJWfA'),
            ('Thomas', '2420 Santa Fir Ct', 'tmoua3000@gmail.com', 'thx12345'),
            ('James', '8577 South North Ave', 'alastair@msn.com', 'jb4sm7'),
            ('John', '785 St Paul St', 'graham@sbcglobal.net', '2SBybj'),
            ('Robert', '78 Fairfield Lane', 'animats@outlook.com', 'Bjd2JK'),
            ('Michael', '7695 Baker Street', 'jmorris@hotmail.com', 'DGK2sA'),
            ( 'William', '27 Vernon Street', 'garyjb@aol.com', 'WvYHYs'),
            ( 'David', '220 Orchard Lane', 'presoff@verizon.net', 'AH9Y4K'),
            ( 'Richard', '6 Coffee St', 'moonlapse@yahoo.ca', 'K3qtDU'),
            ( 'Jospeh', '3 Pineknoll Ave', 'tubesteak@aol.com', 'yr9Et3'),
            ( 'Charles', '933 Glenholme Street', 'aegreene@live.com', 'FpK7SK'),
            ( 'Chirstopher', '8746 Hilltop Street', 'joelw@mac.com', 'jNp4G8'),
            ( 'Daniel', '9784 Lake Forest Lane', 'joehall@att.net', 'HPxhGQ'),
            ( 'Matthew', '9626 NW. Edgefield Street', 'hllam@comcast.net', 'kVrngH'),
            ( 'Anthony', '83 Maiden St', 'reeds@verizon.net', '2EXSfE'),
            ( 'Donald', '99C W. Temple Ave', 'gomor@optonline.net', 'yRN9Qu'),
            ( 'Mark', '7245 Joy Ridge Street', 'emmanuel@comcast.net', 'JkFWQn'),
            ( 'Paul', '7037 Marsh Dr', 'matthijs@optonline.net', 'vCK9DS'),
            ( 'Steven', '9126 Woodsman Court', 'nwiger@verizon.net', 'x3NgmZ'),
            ( 'Andrew', '58 S. Elizabeth Street', 'syncnine@verizon.net', 'hnRdYP'),
            ( 'Kenneth', '578 Illinois St', 'hauma@optonline.net', 'YAKwXe'),
            ( 'Joshua', '966 Sunset Street', 'british@msn.com', 'gAFbsw'),
            ( 'Kevin', '9659 8th St', 'gavinls@yahoo.ca', 'zVSvNY'),
            ( 'Brian', '3 Saxon Street', 'benanov@icloud.com', 'KJkbcS'),
            ( 'George', '9129 S. Galvin Street', 'tjensen@outlook.com', 'juFHUC'),
            ( 'Edward', '629 Pulaski Ave', 'lishoy@aol.com', ''),
            ( 'Ronald', '977 East School Street', 'hermanab@icloud.com', 'mKeu7r'),
            ( 'Timothy', '9566 West Elizabeth Circle', 'sassen@yahoo.ca', '3HpD5T'),
            ( 'Jason', '820 Marsh Ave', 'dbanarse@icloud.com', 'Ap5HYp'),
            ( 'Gary', '282 Shady St', 'bogjobber@gmail.com', 'kZDnyT'),
            ( 'Nicholas', '9516 Courtland Circle', 'punkis@outlook.com', 'wv8ywD'),
            ( 'Eric', '364 Rockaway Dr', 'nullchar@outlook.com', 'TQhRa8'),
            ( 'Jonathan', '989 Theatre Ave', 'bolow@yahoo.ca', 'HeVjHE'),
            ( 'Stephen', '594 Ivy St', 'timtroyr@icloud.com', 'SB39ru'),
            ( 'Justin', '10 Hudson Drive', 'dinther@gmail.com', 'NpM2a5'),
            ( 'Larry', '178 South Princeton St', 'andersbr@comcast.net', 'EYa4BN'),
            ( 'Scott', '31 Mill Pond Circle', 'marnanel@mac.com', 'AYSQk2'),
            ( 'Brandon', '676 Homewood Drive', 'cfhsoft@verizon.net', 'uTu83j'),
            ( 'Benjamin', '90 W. Harvey St', 'sonnen@hotmail.com', 'wpmNq7'),
            ( 'Samuel', '7 Old Harvey St', 'valdez@comcast.net', 'CfAB9q'),
            ( 'Frank', '8431 East Shadow Brook Rd', 'dunstan@live.com', 'Dat9nV'),
            ( 'Gregory', '7856 North St', 'staikos@sbcglobal.net', 'fMzEbe'),
            ( 'Raymond', '25 North St', 'shazow@outlook.com', 'y9HeaA'),
            ( 'Frank', '8769 Front Ave', 'curly@icloud.com', 'xGbNpJ'),
            ( 'Alexander', '356 Marshall Drive', 'optonline', 'p7erVn'),
            ( 'Patrick', '47 Oak Meadow Road', 'natepuri@mac.com', 'vc4sKA'),
            ( 'Jack', '74 River Court', 'carreras@sbcglobal.net', 'c4CyRG'),
            ( 'Dennis', '580 Arlington Street', 'garyjb@outlook.com', 'dNMfYL'),
            ( 'Jerry', '7875 West Gregory Street', 'mgreen@verizon.net', 'U4p2pq'),
            ( 'Tyler', '721 N. Bohemia Ave', 'lauronen@att.net', 'ytuSuP'),
            ( 'Aaron', '112 Glen Creek Drive', 'ntegrity@msn.com', 'shb6PR'),
            ( 'Jack', '511 Sutor Ave', 'parkes@msn.com', 'DdBCZg'),
            ( 'Jose', '255 Homewood Ave', 'mfburgo@live.com', 'afHK4m'),
            ( 'Henry', '8231 East Proctor St', 'tezbo@outlook.com', 'wXKzeU'),
            ( 'Adam', '565 Airport St', 'benits@outlook.com', 'V85Wcf'),
            ( 'Douglas', '7654 Lakeshore Road', 'pplinux@msn.com', 'kUkBGQ'),
            ( 'Nathan', '83 Division St', 'daveewart@live.com', 'kYcxqr'),
            ( 'Peter', '59 St Paul St', 'bartak@att.net', 'g74XkY'),
            ( 'Zachary', '8682 Bayberry Avenue', 'danzigism@aol.com', 'dFtvku'),
            ( 'Kyle', '408 Sierra Drive', 'dieman@verizon.net', 'ht2d9q'),
            ( 'Walter', '9088 Marsh Rd', 'pplinux@icloud.com', 'WnSYW7'),
            ( 'Harold', '222 East Victoria Street', 'leviathan@optonline.net', 'mcuqhd'),
            ( 'Jeremy', '7557 Beechwood St', 'smartfart@optonline.net', 'UnsQxE'),
            ( 'Ethan', '7572 Grand Road', 'krueger@gmail.com', 'DYCj2p'),
            ( 'Carl', '9164 Prairie Ave', 'neonatus@aol.com', 'pHqALS'),
            ( 'Keith', '23 Cardinal St', 'dvdotnet@comcast.net', 'VEJeRk'),
            ( 'Sarah', '9599 King Ave', 'heroine@optonline.net', 'ZYWmL4'),
            ( 'Roger', '109 NW. Water Street ', 'drewf@comcast.net', 'AKsEYb'),
            ( 'Gerald', '8200 NE. Arcadia Lane', 'mxiao@hotmail.com', 'UQ3Hy6'),
            ( 'Chirstian', '6 Bay Meadows Lane', 'satishr@yahoo.com', 'eGZ5CG'),
            ( 'Terry', '9824 Cherry Drive', 'parasite@outlook.com', 'jSJxUJ'),
            ( 'Sean', '70 W. Jackson Street', 'bartlett@verizon.net', 'VuP8J5'),
            ( 'Arthur', '7557 Penn Street', 'qrczak@mac.com', 'Zgphmj'),
            ( 'Austin', '658 Summit Dr.', 'jguyer@me.com', 'xqMS4p'),
            ( 'Noah', '323 Pendergast Dr.', 'kuparine@outlook.com', 'FFCSNp'),
            ( 'Lawrence', '8067 Green Lake Street', 'miami@sbcglobal.net', 'UxK4A2'),
            ( 'Jesse', '200 S. Paris Hill Ave', 'rafasgj@icloud.com', 'HRgj4F'),
            ( 'Joe', '945 Glenridge Drive', 'inico@yahoo.ca', '4bctfr'),
            ( 'Bryan', '588 Talbot St', 'pkilab@comcast.net', '8fSvm4'),
            ( 'Billy', '93 West Inverness Circle', 'amimojo@comcast.net', 'b2cau2'),
            ( 'Jordan', '2 Oak Valley Ave', 'paley@live.com', 'M8Etcj'),
            ( 'ALbert', '92 Madison Dr', 'techie@optonline.net', 'JNbBkw'),
            ( 'Dylan', '984 Lancaster Dr', 'jandrese@yahoo.com', 'pCFLgE'),
            ( 'Bruce', '135 S. 4th Dr', 'north@sbcglobal.net', 'Gt36tp'),
            ( 'Willie', '8778A Harvey Street', 'darin@live.com', 'sttZpb'),
            ( 'Gabriel', '19 Sycamore St', 'rbarreira@verizon.net', 'tNvgpy'),
            ( 'Alan', '984 Gonzales St', 'crypt@outlook.com', 'LMAxjA'),
            ( 'Juan', '90 East Armstrong Road', 'thomasj@optonline.net', 'gkDCWd'),
            ( 'Logan', '7055 Olive Drive', 'sopwith@msn.com', 'ngu6qX'),
            ( 'Wayne', '394 10th St', 'kassiesa@outlook.com', 'vpWPDQ'),
            ( 'Ralph', '5 Sleepy Hollow Ave. ', 'retoh@comcast.net', 'srFRgK'),
            ( 'Roy', '82 E. Strawberry St', 'rmcfarla@outlook.com', 'wWUfES'),
            ( 'Eugene', '50 Sycamore Street', 'sfoskett@outlook.com', 'LdwnCv'),
            ( 'Randy', '615 Wakehurst St', 'jmmuller@yahoo.ca', '5wZjah'),
            ( 'Vincent', '64 Randall Mill St', 'horrocks@yahoo.com', 'u7SDqn'),
            ( 'Russell', '148 Shadow Brook Street', 'jkegl@gmail.com', 'A5EMPk'),
            ( 'Louis', '963 Hamilton Ave', 'feamster@sbcglobal.net', '57a9E4')
        ]
        _conn.executemany(sql,arg)
        _conn.commit()
    except Error as e:
        print(e)

def populateCar(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Car")

    try:
        sql ='''INSERT INTO car(c_custkey,c_price,c_brand,c_year,c_titlestatus,c_mileage,c_color) 
                VALUES( ?, ?, ?, ?, ?, ?, ?);'''
        cur = _conn.cursor()
        
        for ckey in range (1,201):
            print(ckey)
            ctkey = random.randint(1,100)
            cPrice = random.randint(10000,50000)

            brand = ['Acura','Audi','BMW','Chevorlet','Dodge','Fiat','Ford','GMC','Honda','Hyundai','Infinit','Jeep','Kia','Lexus','Mazda','Nissian', 'Mitsubishi', 'Ram','Subaru','Tesla','Toyota','Volkswagen','Volvo']
            cBrand = random.choice(brand)

            cYear = random.randint(1900,2020)

            title = ['clean','salvage']
            cStat = random.choice(title)

            cMile = random.randint(30000,150000)

            color = ['red','blue','green','light blue','silver','black','white','yellow','orange','purple']
            cColor = random.choice(color)

            args = [ctkey, cPrice, cBrand, cYear, cStat, cMile, cColor]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populateBranch(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Branch")

    try:
        sql ='''INSERT INTO branch(b_custkey,b_carkey,b_serkey,b_salekey,b_rentkey,b_location) 
                VALUES( ?, ?,?,?, ?, ?);'''
        cur = _conn.cursor()
        
        for bkey in range (1,401):
            print(bkey)
            ckey = random.randint(1,100)
            carkey = random.randint(1,200)
            serkey = random.randint(1,50)
            salekey = random.randint(1,100)
            rkey = random.randint(1,100)
            l = ['Merced','Fresno','Atwater','Los Angeles','Riverside','Madera','Sonoma','San Diego','Chowchilla','Cerritos','Long Beach','Clovis','Colfax','Elk Grove','San Jose','Sacramento','Hayward','Hemet','Hercules','Mailbu']
            location = random.choice(l)

            args = [ ckey, carkey, serkey,salekey, rkey, location]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populatesales(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate sales")

    try:
        sql ='''INSERT INTO sales(sp_name) 
                VALUES(?);'''
        cur = _conn.cursor()
        
        for skey in range (1,101):
            print(skey)
            sName = ['Liam','Noah','William','James','Logan','Ben','Mason','Elijah','Oliver','Jacob'
                    'Micheal', 'Ethan','Daniel','Matthew','Adien','Henry','Joseph','Jackson','Samuel','Sebastian'
                    'Amy','David','Carter','Wyatt','Jayden','John','Owen','Dylan','Luke','Gabriel','Anothny',
                    'Isaac', 'Grayson','Jack','Julian','Levi','Christopher','Joshua','Andrew']
            name = random.choice(sName)
            args = [name]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populateRent(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate sales")

    try:
        sql ='''INSERT INTO rental(r_price,r_pdate, r_ddate) 
                VALUES(?,?,?);'''
        cur = _conn.cursor()
        
        for rkey in range (1,101):
            print(rkey)

            year = 2000
            day = random.randint(1,15)
            day2 = random.randint(16,31)
            month = random.randint(1,12)
            pdate = str(year)+'-'+str(month)+'-'+str(day)
            ddate = str(year)+'-'+str(month)+'-'+str(day2)
            amount = day2-day
            price = random.randint(100,300)
            pPrice = price*amount
            args = [pPrice,pdate,ddate]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def populateService(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate sales")

    try:
        sql ='''INSERT INTO services(s_price,s_date,s_term,s_type,s_repair,s_workorder) 
                VALUES(?,?,?,?,?,?);'''
        cur = _conn.cursor()
        
        for skey in range (1,51):
            print(skey)
            price = random.randint(100,1000)
            month = random.randint(1,12)
            day = random.randint(1,31)
            date = '2000-'+str(month)+'-'+str(day)
            sterm = ['confirm','unconfirm']
            term = random.choice(sterm) 
            stype = ['oil change','transmission change','coolant change','other problems']
            type = random.choice(stype)
            srepair = ['yes', 'no']
            repair = random.choice(srepair)
            order = 'no ordering of new parts'
            if(repair == 'yes'):
                price +=2000
                order = 'ordering new parts'
        
            args = [price,date,term,type,repair,order]
            cur.execute(sql, args)
            _conn.commit()

        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"table.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateCustomer(conn)
        populateCar(conn)
        populateBranch(conn)
        populatesales(conn)
        populateRent(conn)
        populateService(conn)

    closeConnection(conn, database)

if __name__ == '__main__':
    main()