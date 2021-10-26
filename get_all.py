from flask import Flask
from flaskext.mysql import MySQL

def connection_to_db():
    app = Flask(__name__)
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'mr-robot'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'dfcdewq1'
    app.config['MYSQL_DATABASE_DB'] = 'orangery'
    app.config['MYSQL_DATABASE_HOST'] = '35.158.103.32'
    mysql.init_app(app)
    conn = mysql.connect()
    cursor =conn.cursor()
    return (conn, cursor)



def see_all():   #get_all_database
    conn, cursor = connection_to_db()
    result = cursor.execute(f'''SELECT * FROM plants;''')
    data = cursor.fetchall()
    s1 = 'ID:  Name:         description:       number:  price:     rare:\n'
    for i in data:
        s1 += str(i[0]).ljust(4) + i[1].ljust(14) + i[2].ljust(23) + str(i[3]).ljust(10) + str(i[4]).ljust(9) + i[5] + '\n'

    cursor.close()

    return (s1)

def get_id(id):
    conn, cursor = connection_to_db()
    try:
        result = cursor.execute(f'''SELECT * FROM plants WHERE plant_id={id}''')
        data = cursor.fetchone()
        cursor.close()
        s1 = 'ID:  Name:         description:       number:  price:     rare:\n'
        s1 += str(data[0]).ljust(4) + data[1].ljust(14) + data[2].ljust(23) + str(data[3]).ljust(10) + str(data[4]).ljust(9) + data[5] + '\n'
        return (s1)
    except Exception:
        pass
        return ('Please, enter the correct ID')


def get_n(n):
    conn, cursor = connection_to_db()
    try:
        result = cursor.execute(f'''SELECT * FROM plants ORDER BY plant_id DESC LIMIT {n}''')
        data = cursor.fetchall()
        cursor.close()
        s1 = 'ID:  Name:         description:       number:  price:     rare:\n'
        for i in data:
            s1 += str(i[0]).ljust(4) + i[1].ljust(14) + i[2].ljust(23) + str(i[3]).ljust(10) + str(i[4]).ljust(9) + i[5] + '\n'

        return (s1)
    except Exception:
        pass
        return ('N is incorrect')


def del_id(id):
    conn, cursor = connection_to_db()
    try:
        result = cursor.execute(f'''DELETE FROM plants WHERE plant_id={id}''')
        conn.commit()
        cursor.close()
        return (" Done ! ...")
    except Exception:
        pass
        return ("ID is incorrect")



def edit(id, name, desc, number, price, rare):
    conn, cursor = connection_to_db()
    try:
        result = cursor.execute(f'''UPDATE plants SET name='{name}', description='{desc}', number={number}, price={price}, rare='{rare}' WHERE plant_id={id}''')
        conn.commit()
        cursor.close()
        return ("Done ! ...")
    except Exception:
        pass
        return ('Something is wrong with your entered data')


def create(name, desc, number, price, rare):
    conn, cursor = connection_to_db()
    try:
        result = cursor.execute(f'''INSERT INTO plants (plant_id, name, description, number, price, rare)  VALUES(NULL, '{name}', '{desc}', '{number}', '{price}', '{rare}')''')
        conn.commit()
        cursor.close()
        return ("Done ! ...")
    except Exception:
        pass
        return ('Something is wrong with your entered data')




