# database.py
# example
'''
https://github.com/UncleEngineer/BasicSQL?fbclid=IwAR27hLA3U6EK6J3d9ZPS_t_eQ-gymSSQM7s8w1bQKco4vl6_p9CCB69Fvk8
https://github.com/UncleEngineer/BasicSQL/blob/master/submarine.py
VS Code Browser: https://vscode.dev/
Program DB Browser: https://sqlitebrowser.org/
'''

import sqlite3

conn = sqlite3.connect('transaction_history-database.sqlite3')
c = conn.cursor()

# CREATE TABLE
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tid TEXT,
                stamp TEXT,
                product TEXT,
                price REAL,
                quan REAL,
                total REAL )""")

print('Success')

def insert_transaction(data):
    # data = {'tid':'12341234124','stamp':'2021-12-12 10:20:59'...}
    ID = None
    tid = data['tid']
    stamp = data['stamp']
    product = data['product']
    price = data['price']
    quan = data['quan']
    total = data['total']
    
    with conn:
        command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
        c.execute(command,(ID,tid,stamp,product,price,quan,total))
        conn.commit()
    print('inserted!')

'''
transaction = {'tid':'1456131231',
               'stamp':'2022-01-31 12:40:20',
               'product':'ทุเรียน',
               'price':'100',
               'quan':'50',
               'total':'5000'}
'''

def view_transaction():
    with conn:
        c.execute("SELECT * FROM transaction_history")
        data = c.fetchall()
        print(data)

#insert_transaction(transaction)

view_transaction()

def update_transaction(ID,field,data):
    with conn:
        command = 'UPDATE transaction_history SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command,([data,ID]))
    conn.commit()
    print('updated success')

def delete_transaction(ID):
    with conn:
        command = 'DELETE FROM transaction_history WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()
    print('deleted!')

#delete_transaction(4)