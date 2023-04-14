# exercise 1
import sqlite3
conn = sqlite3.connect("sqlite1.sqlite")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE book_db(
book_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(30),
author VARCHAR(20),
release_year INT,
price INT);
""")
cursor.execute("""INSERT INTO book_db(title, author, release_year, price)
VALUES ("No Longer Human", "Dazai Osamu", 1958, 13.45);""")
book_lst = [
    ("The First Garment", "Guram Dochanashvili", 1975, 40.95),
    ("Kill Switch", "Penelope Douglas", 2019, 20.69),
    ("It ends with us", "Collen Hoover", 2016, 9.95),
    ("It starts with us", "Collen Hoover", 2022, 10.49)
]
cursor.executemany("""INSERT INTO book_db(title, author, release_year, price)
VALUES (?,?,?,?);""", book_lst)
conn.commit()
conn.close()


# exercise 2
conn_1 = sqlite3.connect("sqlite2.sqlite")
cursor_1 = conn_1.cursor()
cursor_1.execute("""CREATE TABLE titanic(
passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,
passenger_name VARCHAR(20),
age INT,
sex VARCHAR(10),
ticket VARCHAR(10),
cabin VARCHAR(5));""")
cursor_1.execute("""INSERT INTO titanic(passenger_name, age, sex, ticket, cabin)
VALUES ("Nana", 18, "female", "econom", "142B");""")
passenger_lst = [
    (input("name:"), input("age:"), input("sex:"), input("ticket:"), input("cabin")),
    (input("name:"), input("age:"), input("sex:"), input("ticket:"), input("cabin")),
    (input("name:"), input("age:"), input("sex:"), input("ticket:"), input("cabin"))
]
cursor_1.executemany("""INSERT INTO titanic(passenger_name, age, sex, ticket, cabin)
VALUES (?,?,?,?,?);""", passenger_lst)
conn_1.commit()
conn_1.close()


# exercise 3
class Movie:
    def __init__(self, title, genre, year, IMDb):
        self.title = title
        self.genre = genre
        self.year = year
        self.IMDb = IMDb

    def __str__(self):
        return f"movie title:{self.title}\ngenre:{self.genre}" \
               f"\nyear:{self.year}\nIMDb:{self.IMDb}"


movie_1 = Movie("Castle in the sky", "Fantasy", 1986, "IMDb")
movie_2 = Movie("Howl's moving castle", "fantasy", 2004, "IMDb")
movie_3 = Movie("Grave of the fireflies", "drama", 1988, "IMDb")
movie_4 = Movie("Spirited away", "Fantasy", 2001, "IMDb")
movie_lst = [
    (movie_2.title, movie_2.genre, movie_2.year, movie_2.IMDb),
    (movie_3.title, movie_3.genre, movie_3.year, movie_3.IMDb),
    (movie_4.title, movie_4.genre, movie_4.year, movie_4.IMDb)
]
conn_2 = sqlite3.connect("sqlite3.sqlite")
cursor_2 = conn_2.cursor()
cursor_2.execute("""CREATE TABLE movie(
movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(20),
genre VARCHAR(10),
year INT,
IMDb VARCHAR(20));""")
cursor_2.execute("""INSERT INTO movie(title, genre, year, IMDb)
VALUES (?,?,?,?);""", (movie_1.title, movie_1.genre, movie_1.year, movie_1.IMDb))
cursor_2.executemany("""INSERT INTO movie(title, genre, year, IMDb)
VALUES (?,?,?,?);""", movie_lst)
conn_2.commit()
conn_2.close()

