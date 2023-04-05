import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_cafe.db")

def cafe_Items_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category, price, instock
        FROM username 
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'name': row[0],
            'category': row[1],
            'price': row[2],
            'instock': row[3]
            }
        data.append(record)
    
    conn.close()
    return data

def find_cafe_name(Items):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category, price, instock
        FROM username 
        WHERE user=?
    """
    val = (Items,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'name': rows[0],
        'category': rows[1],
        'price': rows[2],
        'instock': rows[3]
        }
    data.append(record)
    
    conn.close()
    return data

def cafe_name_add(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO username(name,category,price,instock)
        VALUES(?,?,?)
    """
    val = (name,category,price,instock)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Created successfully"

def cafe_remove(Items):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM username
        WHERE user=?
    """
    val = (Items,)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Delete successfully"

def cafe_Items_update(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE username
        SET password=?, name=?
        WHERE user=?
    """
    val = (category,price,instock,name)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Update successfully"