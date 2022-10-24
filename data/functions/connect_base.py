import sqlite3


def on_startup():
    with sqlite3.connect('./data/base.db') as base:
        base.execute("""CREATE TABLE IF NOT EXISTS users(
                     id, 
                     UNIQUE(id)
                     )""")
        base.execute("""CREATE TABLE IF NOT EXISTS goals( 
                     row_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                     id, 
                     goal, 
                     description
                     )""")
        base.execute("""CREATE TABLE IF NOT EXISTS habits( 
                     row_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                     id, 
                     habit, 
                     description
                     )""")
        base.execute("""CREATE TABLE IF NOT EXISTS tasks( 
                     row_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                     id, 
                     task, 
                     description
                     )""")
        base.execute("""CREATE TABLE IF NOT EXISTS viewed_goal(
                     row_id, id
                     )""")
        base.execute("""CREATE TABLE IF NOT EXISTS viewed_habit(
                     row_id, 
                     id
                     )""")
        base.execute("""CREATE TABLE IF NOT EXISTS viewed_task(
                     row_id, id
                     )""")
        base.commit()
        print('Database connected successfully')
