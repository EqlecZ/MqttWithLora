import sqlite3

def writedata(temp,humi,illu,date):
    conn = sqlite3.connect('../../data.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO db1 (temp, humi, illu, time) VALUES ({temp},{humi},{illu},{date})")
    conn.commit()
    conn.close()
    print("Data written successfully")


