import sqlite3
conn = sqlite3.connect("customers.sqlite")
cursor = conn.cursor()
sel_res = cursor.execute("SELECT * FROM users")
all_rows = cursor.fetchall()
for row in all_rows:
    print(row[1], row[5])

sele_res = cursor.execute("SELECT * FROM users WHERE age > 25")
for row in sele_res:
    print(row[2], row[3], row[4])

age = 25
selec_res = cursor.execute("SELECT * FROM users WHERE age > :age_con", {"age_con": age})
for row in selec_res:
    print(row[2], row[3], row[4])

sele_resu = cursor.execute("SELECT * FROM users WHERE age BETWEEN 10 AND 25")
for row in sele_resu:
    print(row)

sele_resul = cursor.execute("SELECT * FROM users WHERE age <> 20")
for row in sele_resul:
    print(row[2], row[3])

user_amount = cursor.execute("SELECT count() as users_count FROM users")
print(tuple(user_amount))

selec_resu = cursor.execute("SELECT * FROM users order by age desc")

selec_resul = cursor.execute("SELECT DISTINCT firstname FROM users order by firstname")
for row in selec_resul:
    print(row)

sel_resu = cursor.execute("UPDATE users SET firstname = 'Nana' WHERE age = 20")

sel_resul = cursor.execute("UPDATE users SET age = 15 WHERE age > 30")

select_res = cursor.execute("DELETE FROM users WHERE user_id = 5")

select_result = cursor.execute("DELETE FROM users WHERE firstname < 'ბ'")
conn.commit()
conn.close()
