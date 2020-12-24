import random
import sqlite3
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

def login(_conn,id):
    try:
        cur = _conn.cursor()
        print('Login:')
        print('--------------------')
        print('Option:')
        print('1. Create a new account')
        print('2. Login to my account')
        print('3. Login as an Agent account')
        print('4. Go back to Main Menu')
        choice = int(input('Enter number:'))
        if(choice == 1):
            #create a new account and return new id
            while(1):
                nEmail = input('Enter your email: ')
                if(nEmail == 'exit'):
                    print("++++++++++++++++++++++++++++++++++")
                    return id
                sql = '''select * from customer'''
                cur.execute(sql)
                rows = cur.fetchall()
                same = 0
                for row in rows:
                    if(row[3] == nEmail):
                        same = 1
                        break
                        
                if same == 0:        
                    nP = input('Create a new password: ')
                    name = input('Enter your first name: ')
                    address = input('Enter your address: ')
                    sql = '''insert into customer(ct_name,ct_address,ct_email,ct_password)
                        values(?,?,?,?)'''
                    args = [name, address, nEmail, nP]
                    cur.execute(sql,args)
                    _conn.commit()

                    sql = '''select * from customer where ct_email = ?'''
                    cur.execute(sql,[nEmail])
                    rs = cur.fetchall()
                    for r in rs:
                        print("++++++++++++++++++++++++++++++++++")
                        print('You have successfully created account and enter as customer: '+str(r[0])+' '+name)
                        return int(r[0])
                else:
                    print('Error: Email already exist. Please enter another email or enter "exit"')
        if(choice == 2):
            print('--------------------')
            while(1):
                #search, find and return customer id
                cEmail = input('Enter your email: ')
                if(cEmail == 'exit'):
                    print("++++++++++++++++++++++++++++++++++")
                    login(_conn, id)
                sql = '''select * from customer where ct_email = ?'''
                cur.execute(sql,[cEmail])
                rows = cur.fetchall()
                for row in rows:
                    if(row[3] == cEmail):
                        while(1):
                            cP = input('Enter customer password: ')
                            if(cP == 'exit'):
                                print('--------------------')
                                return id
                            if(cP == row[4]):
                                print("++++++++++++++++++++++++++++++++++")
                                print('You have login as: '+str(row[0])+' '+row[1])
                                return int(row[0])
                            print('Error: Please try again or enter "exit"')
                print('Error: No email exist. Please enter another email or enter "exit"')
        if(choice == 3):
            print('--------------------')
            while(1):
                mkey = input('Enter agent key: ')
                if(mkey == 'Nu'):
                    print('You have enter as an Agent!!!!')
                    print("++++++++++++++++++++++++++++++++++")
                    return 0
                if(mkey == 'exit'):
                    return id
                print('Error: Please try again or enter "exit"')

        if(choice == 4):
            print("++++++++++++++++++++++++++++++++++")
            return id
        else:
            print("++++++++++++++++++++++++++++++++++")
            print('Error: Number is not Recognize, Please reenter.')
            print("++++++++++++++++++++++++++++++++++")
            return login(_conn,id)
    except Error as e:
        print(e)

def buy(_conn,id):
    try:
        cur = _conn.cursor()
        low = 0
        high = 100000
        brand = 'Subaru'
        lyear = 1900
        hyear = 2020
        ts = 'clean'
        lmile = 0
        hmile = 200000
        color = 'light blue'
        while(1):
            print('Buy:')
            print('--------------------')
            print('Option:')
            print('0. Go back to Main Menu')
            print('1. View cars')
            print('---------------------')
            print('Add Filter: ')
            print('2. Price Range: \t'+str(low)+'-'+str(high))
            print('3. Brand: \t\t'+brand)
            print('4. Year: \t\t'+str(lyear)+'-'+str(hyear))
            print('5. Titlestatus: \t'+ts)
            print('6. Mileage range: \t'+str(lmile)+'-'+str(hmile))
            print('7. Color: \t\t'+color)
            choice = int(input("Enter number: "))
            if choice == 0:
                return
            if choice == 1:
                sql ='''select c_price,c_brand,c_year,c_titlestatus,c_mileage,c_color
                        from car, branch
                        where c_custkey != ?
                            and c_carkey = b_carkey
                            and c_price >= ?
                            and c_price <= ?
                            and c_brand = ?
                            and c_year >= ?
                            and c_year <= ?
                            and c_titlestatus = ?
                            and c_mileage >= ?
                            and c_mileage <= ?
                            and c_color = ?;'''
                args = [id,low,high,brand,lyear,hyear,ts,lmile,hmile,color]
                cur.execute(sql,args)
                rows = cur.fetchall()
                l = '{:>10}{:>15}{:>15}{:>10}{:>15}{:>10}'.format('Price','brand','year','titlestatus','mileage','color')
                print(l)
                print('---------------------------------------------------------------------------')
                for row in rows:
                    l = '{:>10}{:>15}{:>15}{:>10}{:>15}{:>20}'.format(row[0],row[1],row[2],row[3],row[4],row[5])
                    print(l)
                pause = input('Press enter to go back to selection or scroll up for car details')
                print('--------------------')
            if choice == 2:
                print('--------------------')
                low = input('Enter the lowest price: ')
                high = input('Enter the highest price: ')
                print('--------------------')
            if choice == 3:
                print('--------------------')
                print('Car brand:\nAcura, Audi, BMW, Chevorlet, Dodge, Fiat, Ford, GMC, Honda, Hyundai\n, Infinit, Jeep, Kia, Lexus, Mazda, Nissian, Mitsubishi, Ram\nSubaru, Tesla, Toyota, Volkswagen, Volvo')
                brand = input('Enter car brand: ')
                print('--------------------')
            if choice == 4:
                print('--------------------')
                lyear = input('Enter the lowest year: ')
                hyear = input('Enter the highest year: ')
                print('--------------------')
            if choice == 5:
                print('--------------------')
                print('Titlestatus:\n clean, salvage, junk, bonded, reconstucted, rebuilt')
                ts = input('Enter the titlestatus: ')
                print('--------------------')
            if choice == 6:
                print('--------------------')
                lmile = input('Enter the lowest mile: ')
                hmile = input('Enter the highest mile: ')
                print('--------------------')
            if choice == 7:
                print('--------------------')
                print('Color:\nred, blue, green, light blue, silver, black, white, yellow, orange, purple')
                color = input('Enter the preferred color: ')
                print('--------------------')
    except Error as e:
        print(e)

def sell(_conn, id):
    try:
        cur = _conn.cursor()
        print('Sell: ')
        print('---------------------')
        brand = input('Enter your car brand: ')
        year = input('Enter the year of the car: ')
        ts = input('Enter the titlestatus: ')
        mileage = input('Enter the number of mileage: ')
        color = input('Enter the color: ')
        price = input('Enter the price for the car: ')
        sql = '''insert into car(c_custkey,c_price,c_brand,c_year,c_titlestatus,c_mileage,c_color) VALUES (?,?,?,?,?,?,?)'''
        args = [id,price,brand,year,ts,mileage,color]
        cur.execute(sql,args)
        _conn.commit()
        print('---------------------')
        print('You have succesfully added car!')
        print('---------------------')
        
    except Error as e:
        print(e)

def track(_conn,id):
    try:
        cur = _conn.cursor()
        low = 0
        high = 100000
        brand = 'Acura'
        lyear = 1900
        hyear = 2020
        ts = 'salvage'
        lmile = 0
        hmile = 200000
        color = 'blue'
        while(1):
            print('Track Cars:')
            print('--------------------')
            print('Option:')
            print('0. Go back to Main Menu')
            print('1. Track location of my cars')
            print('2. Track location of other cars')
            print('---------------------')
            print('Add Filter: ')
            print('3. Price Range: \t'+str(low)+'-'+str(high))
            print('4. Brand: \t\t'+brand)
            print('5. Year: \t\t'+str(lyear)+'-'+str(hyear))
            print('6. Titlestatus: \t'+ts)
            print('7. Mileage range: \t'+str(lmile)+'-'+str(hmile))
            print('8. Color: \t\t'+color)
            choice = int(input("Enter number: "))
            if choice == 0:
                return
            if choice == 1:
                sql = '''select b_location,c_price,c_brand,c_year,c_titlestatus,c_mileage,c_color
                        from car, branch
                        where c_custkey == ?
                            and c_carkey = b_carkey;'''
                cur.execute(sql,[id])
                l = '{:>15}{:>10}{:>15}{:>10}{:>15}{:>10}{:>10}'.format('Location','Price','brand','year','titlestatus','mileage','color')
                print(l)
                print('-------------------------------------------------------------------------------------')
                rows = cur.fetchall()
                for row in rows:
                    l = '{:>15}{}{:>10}{:>15}{:>10}{:>15}{:>10}{:>10}'.format(row[0],':',row[1],row[2],row[3],row[4],row[5],row[6])
                    print(l)
                pause = input('Press enter to go back to selection or scroll up for car details')
                print('--------------------')
            if choice == 2:
                sql ='''select c_price, b_location,c_brand,c_year,c_titlestatus,c_mileage,c_color
                        from car, branch
                        where c_custkey != ?
                            and c_carkey = b_carkey
                            and c_price >= ?
                            and c_price <= ?
                            and c_brand = ?
                            and c_year >= ?
                            and c_year <= ?
                            and c_titlestatus = ?
                            and c_mileage >= ?
                            and c_mileage <= ?
                            and c_color = ?;'''
                args = [id,low,high,brand,lyear,hyear,ts,lmile,hmile,color]
                cur.execute(sql,args)
                rows = cur.fetchall()
                l = '{:>15}{:>10}{:>15}{:>10}{:>15}{:>10}{:>10}'.format('Location','Price','brand','year','titlestatus','mileage','color')
                print(l)
                print('-------------------------------------------------------------------------------------')
                for row in rows:
                    l = '{:>15}{}{:>10}{:>15}{:>10}{:>15}{:>10}{:>10}'.format(row[1],':',row[0],row[2],row[3],row[4],row[5],row[6])
                    print(l)
                pause = input('Press enter to go back to selection or scroll up for car details')
                print('--------------------')
            if choice == 3:
                print('--------------------')
                low = input('Enter the lowest price: ')
                high = input('Enter the highest price: ')
                print('--------------------')
            if choice == 4:
                print('--------------------')
                print('Car brand:\nAcura, Audi, BMW, Chevorlet, Dodge, Fiat, Ford, GMC, Honda, Hyundai\n, Infinit, Jeep, Kia, Lexus, Mazda, Nissian, Mitsubishi, Ram\nSubaru, Tesla, Toyota, Volkswagen, Volvo')
                brand = input('Enter car brand: ')
                print('--------------------')
            if choice == 5:
                print('--------------------')
                lyear = input('Enter the lowest year: ')
                hyear = input('Enter the highest year: ')
                print('--------------------')
            if choice == 6:
                print('--------------------')
                print('Titlestatus:\n clean, salvage, junk, bonded, reconstucted, rebuilt')
                ts = input('Enter the titlestatus: ')
                print('--------------------')
            if choice == 7:
                print('--------------------')
                lmile = input('Enter the lowest mile: ')
                hmile = input('Enter the highest mile: ')
                print('--------------------')
            if choice == 8:
                print('--------------------')
                print('Color:\nred, blue, green, light blue, silver, black, white, yellow, orange, purple')
                color = input('Enter the preferred color: ')
                print('--------------------')
    except Error as e:
        print(e)

def update(_conn,id):
    try:
        cur = _conn.cursor()
        while(1):
            print('Update: ')
            print('---------------------')
            print('0. Go back to Main Menu')
            print('1. update customer information')
            print('2. update car')
            print('3. delete car')
            choice = int(input("Enter number: "))
            print('---------------------')
            if choice == 0:
                return
            if choice == 1:
                while(1):
                    sql = '''select * from customer where ct_custkey = ?'''
                    cur.execute(sql,[id])
                    l = '{:>10}{:>10}{:>25}{:>20}{:>17}'.format('Customer ID','Name', 'Address', 'Email', 'Password')
                    print(l)
                    print('------------------------------------------------------------------------------------')
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:>10}{:>10}{:>25}{:>25}{:>10}'.format(row[0],row[1],row[2],row[3],row[4])
                        print(l)
                    print('Option:\t0 - exit')
                    print('\t1 - Change Name')
                    print('\t2 - Change Address')
                    print('\t3 - Change Email')
                    print('\t4 - Change Password')
                    change = int(input('Enter Option: '))
                    print('---------------------')
                    if change == 0:
                        return update(_conn,id)
                    if change == 1:
                        newName = input('Enter new name: ')
                        sql = '''Update customer set ct_name = ? where ct_custkey = ?'''
                        cur.execute(sql,[newName,id])
                        _conn.commit()
                        l = '{:>10}{:>10}{:>25}{:>20}{:>17}'.format('Customer ID','Name', 'Address', 'Email', 'Password')
                        print(l)
                        print('------------------------------------------------------------------------------------')
                        rows = cur.fetchall()
                        for row in rows:
                            l = '{:>10}{:>10}{:>25}{:>25}{:>10}'.format(row[0],row[1],row[2],row[3],row[4])
                            print(l)
                        print('---------------------')
                        print('You have successfullly change your name')
                        print('---------------------')
                    if change == 2:
                        newAddress = input('Enter new address: ')
                        sql = '''Update customer set ct_address = ? where ct_custkey = ?'''
                        cur.execute(sql,[newAddress,id])
                        _conn.commit()
                        l = '{:>10}{:>10}{:>25}{:>20}{:>17}'.format('Customer ID','Name', 'Address', 'Email', 'Password')
                        print(l)
                        print('------------------------------------------------------------------------------------')
                        rows = cur.fetchall()
                        for row in rows:
                            l = '{:>10}{:>10}{:>25}{:>25}{:>10}'.format(row[0],row[1],row[2],row[3],row[4])
                            print(l)
                        print('---------------------')
                        print('You have successfullly change your address')
                        print('---------------------')
                    if change == 3:
                        newEmail = input('Enter new email: ')
                        sql = '''Update customer set ct_email = ? where ct_custkey = ?'''
                        cur.execute(sql,[newEmail,id])
                        _conn.commit()
                        l = '{:>10}{:>10}{:>25}{:>20}{:>17}'.format('Customer ID','Name', 'Address', 'Email', 'Password')
                        print(l)
                        print('------------------------------------------------------------------------------------')
                        rows = cur.fetchall()
                        for row in rows:
                            l = '{:>10}{:>10}{:>25}{:>25}{:>10}'.format(row[0],row[1],row[2],row[3],row[4])
                            print(l)
                        print('---------------------')
                        print('You have successfullly change your email')
                        print('---------------------')
                    if change == 4:
                        newPassword = input('Enter new password: ')
                        sql = '''Update customer set ct_password = ? where ct_custkey = ?'''
                        cur.execute(sql,[newPassword,id])
                        _conn.commit()
                        l = '{:>10}{:>10}{:>25}{:>20}{:>17}'.format('Customer ID','Name', 'Address', 'Email', 'Password')
                        print(l)
                        print('------------------------------------------------------------------------------------')
                        rows = cur.fetchall()
                        for row in rows:
                            l = '{:>10}{:>10}{:>25}{:>25}{:>10}'.format(row[0],row[1],row[2],row[3],row[4])
                            print(l)
                        print('---------------------')
                        print('You have successfullly change your password')
                        print('---------------------')
            if choice == 2:
                while(1):
                    print('Option:\t 0 - exit')
                    print('\t1. Price')
                    print('\t2. Brand')
                    print('\t3. Year')
                    print('\t4. Titlestatus')
                    print('\t5. Mileage')
                    print('\t6. Color')
                    sql = '''select * from car where c_custkey = ?'''
                    cur.execute(sql,[id])
                    l = '{:>10}{:>10}{:>10}{:>20}{:>5}{:>10}{:>10}{:>10}'.format('Car ID','Customer ID', 'Price', 'Brand', 'Year','Titlestatus', 'mileage','color')
                    print(l)
                    print('------------------------------------------------------------------------------------')
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:>10}{:>10}{:>10}{:>20}{:>5}{:>10}{:>10}{:>10}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                        print(l)
                    carID = int(input('Enter car ID: '))
                    change = int(input('Enter Option: '))
                    print('---------------------')
                    if change == 0:
                        return update(_conn,id)
                    if change == 1:
                        newPrice = input('Enter new price: ')
                        sql = '''Update car set c_price = ? where c_custkey = ? and c_carkey = ?'''
                        cur.execute(sql,[newPrice,id,carID])
                        _conn.commit()
                        print('---------------------')
                        print('You have successfullly change your car Price')
                        print('---------------------')
                    if change == 2:
                        new = input('Enter new brand: ')
                        sql = '''Update car set c_brand = ? where c_custkey = ? and c_carkey = ?'''
                        cur.execute(sql,[new,id,carID])
                        _conn.commit()
                        print('---------------------')
                        print('You have successfullly change your car brand')
                        print('---------------------')
                    if change == 3:
                        new = input('Enter new year: ')
                        sql = '''Update car set c_year = ? where c_custkey = ? and c_carkey = ?'''
                        cur.execute(sql,[new,id,carID])
                        _conn.commit()
                        print('---------------------')
                        print('You have successfullly change your car year')
                        print('---------------------')
                    if change == 4:
                        new = input('Enter new titlestatus: ')
                        sql = '''Update car set c_titlestatus = ? where c_custkey = ? and c_carkey = ?'''
                        cur.execute(sql,[new,id,carID])
                        _conn.commit()
                        print('---------------------')
                        print('You have successfullly change your car titlestatus')
                        print('---------------------')
                    if change == 5:
                        new = input('Enter new mileage: ')
                        sql = '''Update car set c_mileage = ? where c_custkey = ? and c_carkey = ?'''
                        cur.execute(sql,[new,id,carID])
                        _conn.commit()
                        print('---------------------')
                        print('You have successfullly change your car mileage')
                        print('---------------------')
                    if change == 6:
                        new = input('Enter new color: ')
                        sql = '''Update car set c_color = ? where c_custkey = ? and c_carkey = ?'''
                        cur.execute(sql,[new,id,carID])
                        _conn.commit()
                        print('---------------------')
                        print('You have successfullly change your car color')
                        print('---------------------')
            if choice == 3:
                while(1):
                    print('Option:\t 0 - exit')
                    print('\t1. Delete car')
                    sql = '''select * from car where c_custkey = ?'''
                    cur.execute(sql,[id])
                    l = '{:>10}{:>10}{:>10}{:>20}{:>5}{:>10}{:>10}{:>10}'.format('Car ID','Customer ID', 'Price', 'Brand', 'Year','Titlestatus', 'mileage','color')
                    print(l)
                    print('------------------------------------------------------------------------------------')
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:>10}{:>10}{:>10}{:>20}{:>5}{:>10}{:>10}{:>10}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                        print(l)
                    carID = int(input('Enter car ID: '))
                    change = int(input('Enter Option: '))
                    print('---------------------')
                    if change == 0:
                        return update(_conn,id)
                    if change == 1:
                        sql = '''Delete from car where c_custkey = ? and c_carkey = ?'''
                        cur.execute(sql,[id,carID])
                        _conn.commit()
                        print('---------------------')
                        print('You have successfullly delete the car')
                        print('---------------------')
            
    except Error as e:
        print(e)

def rent(_conn, id):
    try:
        cur = _conn.cursor()
        pdate = ''
        rdate = ''
        while(1):
            print('Rental:')
            print('---------------------')
            print('0. Go back to Main Menu')
            print('1. Comfirm your rental')
            print('---------------------')
            print('3. Pick up date: '+pdate)
            print('4. Return date: '+rdate)
            choice = int(input('Enter Option: '))
            print('---------------------')
            if choice == 0:
                return
            if choice == 1:
                price = 356*(int(rdate[8:9])-int(pdate[8:9]))
                sql = '''insert into rental(r_price,r_pdate,r_ddate) values(?,?,?)'''
                cur.execute(sql,[price,pdate,rdate])
                _conn.commit()
                sql = '''select * from rental where r_price = ? and r_pdate = ? and r_ddate = ?'''
                cur.execute(sql,[price,pdate,rdate])
                rows = cur.fetchall()
                rentID = 0
                for row in rows:
                    rentID = row[0]
                carID = random.randint(1,200)
                serkey = 0
                sql = '''insert into sales(sp_name) values(?)'''
                name = ['True','False','Range','Domain']
                sName = random.choice(name)
                cur.execute(sql, [sName])    
                _conn.commit()
                sql = '''select * from sales where sp_name = ?'''
                cur.execute(sql,[sName])
                rows = cur.fetchall()
                salekey = 0
                for row in rows:
                    salekey = row[0]
                location = input('Which location: ')
                sql = '''insert into branch(b_custkey,b_carkey,b_serkey,b_salekey,b_rentkey,b_location) values(?,?,?,?,?,?)'''
                args = [id,carID,serkey,salekey,rentID,location]
                cur.execute(sql,args)
                _conn.commit()
                print('---------------------')
                print('You have successfullly rent a car')
                print('---------------------')
            if choice == 3:
                pdate = input('Enter the Pick up date: ')
            if choice == 4: 
                rdate = input('Enter the return date: ')
            print('---------------------')
    except Error as e:
        print(e)

def service(_conn,id):
    try:
        cur = _conn.cursor()
        date = ''
        term = 'unconfirm'
        stype = ''
        order = ''
        price = ''
        repair = ''
        while(1):
            print('Service:')
            print('---------------------')
            print('0. Go back to Main Menu')
            print('1. Confirm your service')
            print('---------------------')
            print('2. Date: '+date)
            if id == 0:
                print('3. Term: '+term)
                print('4. Type of problem: '+stype)
                print('5. Workorder: '+order)
                print('6. Price: '+price)
                print('7. Repair: '+repair)
                print('8. Update/Confirm services')
            choice = int(input('Enter Option: '))
            print('---------------------')
            if choice == 0:
                return
            if choice == 1:
                sql = '''insert into services(s_price, s_date,s_term,s_type,s_repair,s_workorder)
                        values (?,?,?,?,?,?);'''
                arg = [price,date,term,stype,repair,order]
                cur.execute(sql,arg)
                _conn.commit()

                sql = '''select * 
                        from services 
                        where s_price = ? 
                        and s_date = ?
                        and s_term = ?
                        and s_type = ?
                        and s_repair = ?
                        and s_workorder = ?;'''
                cur.execute(sql,arg)
                rows = cur.fetchall()
                rentID = 0
                serkey = 0
                for row in rows:
                    serkey = row[0]
                sql = '''insert into sales(sp_name) values(?)'''
                name = ['Mine','What','Catch','Flame']
                sName = random.choice(name)
                cur.execute(sql, [sName])    
                _conn.commit()
                sql = '''select * from sales where sp_name = ?'''
                cur.execute(sql,[sName])
                rows = cur.fetchall()
                salekey = 0
                for row in rows:
                    salekey = row[0]
                location = input('Which location: ')
                sql = '''insert into branch(b_custkey,b_carkey,b_serkey,b_salekey,b_rentkey,b_location) values(?,?,?,?,?,?)'''
                args = [id,random.randint(1,200),serkey,salekey,rentID,location]
                cur.execute(sql,args)
                _conn.commit()
                print('---------------------')
                print('You have successfullly set an appointment service')
                print('---------------------')
            if choice == 2:
                date = input('Enter the appointment date: ')
            if id == 0:
                if choice == 3:
                    term = input('Enter confirm or unconfirm: ')
                if choice == 4:
                    print('1. oil change')
                    print('2. transmission change')
                    print('3. coolant change')
                    print('4. other problems')
                    number = int(input('Enter Option: '))
                    if number == 1:
                        stype = 'oil change'
                    if number == 2:
                        stype = 'transmission change'
                    if number == 3:
                        stype = 'coolant change'
                    if number == 4:
                        stype = 'other problems'
                if choice == 5:
                    print('1. no ordering of new parts')
                    print('2. ordering new parts')
                    number = int(input('Enter Option: '))
                    if number == 1:
                        order = 'no ordering of new parts'
                    if number == 2:
                        order = 'ordering new parts'
                if choice == 6:
                    price = input('Enter price: ')
                if choice == 7:
                    repair = input('Enter yes or no: ')
                if choice == 8:
                    sql = '''select * from services'''
                    cur.execute(sql)
                    rows = cur.fetchall()
                    for row in rows:
                        l = '{:>5}{:>10}{:>15}{:>15}{:>30}{:>5}{:>30}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                        print(l)
                    serkey = input('Enter the service key: ')
                    sql = '''update services
                            set s_price = ?,
                                s_date = ?,
                                s_term = ?,
                                s_type = ?,
                                s_repair = ?,
                                s_workorder = ?
                            where s_serkey = ?'''
                    args = [price,date,term,stype,repair,order,serkey]
                    cur.execute(sql,args)
                    _conn.commit()
                    print('---------------------')
                    print('You have successfullly update the service')
                    print('---------------------')
    except Error as e:
        print(e)

def option(_conn):
    try:
        id = -1
        choice = -1
        while(choice != 0):
            print('Car Dealership:')
            print('---------------------')
            print('Option:\t0 - exit')
            print('\t1 - login')
            if id != -1:
                print('\t2 - Buy cars')
                print('\t3 - Sell cars')
                print('\t4 - Track cars')
                print('\t5 - Update Option')
                print('\t6 - Rent cars')
                print('\t7 - Service cars')
            choice = int(input("Enter number: "))
            
            if choice == 1:
                print("++++++++++++++++++++++++++++++++++")
                id = login(_conn,id)
            if id != -1:
                print("++++++++++++++++++++++++++++++++++")
                if choice == 2: #buy
                    buy(_conn,id)
                if choice == 3: #sell
                    sell(_conn,id)
                if choice == 4: #track
                    track(_conn,id)
                if choice == 5: #update
                    update(_conn, id)
                if choice == 6: #rent
                    rent(_conn, id)
                if choice == 7: #service
                    service(_conn,id)
            print("++++++++++++++++++++++++++++++++++")
    except Error as e:
        print(e)

def main():
    database = r"table/table.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        option(conn)
        print('You have now exit out of the application')
    closeConnection(conn, database)

if __name__ == '__main__':
    main()