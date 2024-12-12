import sqlite3

# connection = sqlite3.connect('sqlite.db')                           # start def __enter__
# cursor = connection.cursor()                                        # end def __enter
# cursor.execute("""create table if not exists users(name, age);""")  # start inner with
# cursor.execute("""insert into users values ('Naton', 42);""")       # end inner with
# connection.commit()                                                 # start def __exit__
# connection.close()                                                  # end def __exit__

class DB:  # CONTEXT-MANAGER
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):   # exc_type, exc_val, exc_tb - тип, текст и трассировка (действия, вызвавшие её) ошибки
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None  # сброс к изначальному состоянию



db = DB('sqlite.db')
with db as curs:
    curs.execute("""create table if not exists users(name, age);""")
    curs.execute("""insert into users values ('Naton', 42);""")

