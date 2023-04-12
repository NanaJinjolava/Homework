# exercise 1
import sqlite3
conn = sqlite3.connect("sqlite1.sqlite")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE books_db
 (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
 title VARCHAR(50),
 author VARCHAR(30),
 release_year INT)""")
cursor.execute("""INSERT INTO books_db(title, author, release_year)
 VALUES("No Longer Human", "Dazai Osamu", 1948)""")
conn.commit()
book_ls = [
    ("Rashomon", "Ryunoske Akutagava", 1915),
    ("1984", "George Orwell", 1949),
    ("The First Garment", "Guram Dochanashvili", 1975),
    ("Kill Switch", "Penelope Douglas", 2019)
]
cursor.execute("""INSERT INTO books_db(title, author, release_year)
 VALUES(?,?,?)""", book_ls)
conn.commit()
conn.close()

# exercise 2
conn_1 = sqlite3.connect("sqlite2.sqlite")
cursor_1 = conn_1.cursor()
cursor_1.execute("""CREATE TABLE titanic
(passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,
passenger_name VARCHAR(30),
age INT,
sex VARCHAR(10),
ticket VARCHAR(15),
cabin VARCHAR(5)""")
cursor_1.execute("""INSERT INTO titanic(passenger_name, age, sex, ticket, cabin)
VALUES ("Nana Jinjolava", 18, "female", "econom class", "36-A")""")
passenger_lst = [
    (input("enter passenger name:"), input("enter age:"),
     input("enter gender:"), input("enter ticket verity:"),
     input("enter desired cabin number:")),
    (input("enter passenger name:"), input("enter age:"),
     input("enter gender:"), input("enter ticket verity:"),
     input("enter desired cabin number:")),
    (input("enter passenger name:"), input("enter age:"),
     input("enter gender:"), input("enter ticket verity:"),
     input("enter desired cabin number:"))
     ]
cursor_1.execute("""INSERT INTO titanic(passenger_name, age, sex, ticket, cabin)
VALUES(?,?,?)""", passenger_lst)
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
        return f"movie title:{self.title} \ngenre:{self.genre}" \
               f" \nrelease year:{self.year}, imdb:{self.IMDb}"


movie_1 = Movie("The Legend Of 1900", "Drama", 1998, "0.8/10 stars")
movie_2 = Movie("???", "?", 2023, "?/10")
movie_3 = Movie("???", "?", 2022, "?/10")
movie_4 = Movie("???", "?", 2021, "?/10")
conn_2 = sqlite3.connect("sqlite3.sqlite")
cursor_2 = conn_2.cursor()
cursor_2.execute("""CREATE TABLE movies(
movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(30),
genre VARCHAR(20),
release_year INT,
IMDd VARCHAR(10))""")
cursor_2.execute("""INSERT INTO movies(title, genre, release_year, IMDb)
VALUES (?, ?, ?)""", (movie_1.title, movie_1.genre, movie_1.year, movie_1.IMDb))
conn_2.commit()
movie_lst = [(movie_2.title, movie_2.genre, movie_2.year, movie_2.IMDb),
             (movie_3.title, movie_3.genre, movie_3.year, movie_3.IMDb),
             (movie_4.title, movie_4.genre, movie_4.year, movie_4.IMDb)]
cursor_2.execute("""INSERT INTO movies(title, genre, release_year, IMDb)
VALUES (?, ?, ?)""", movie_lst)
conn_2.commit()
conn_2.close()


