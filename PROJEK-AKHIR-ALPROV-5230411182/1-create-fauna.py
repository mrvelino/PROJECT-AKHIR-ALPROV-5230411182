import sqlite3



bende = sqlite3.connect('database_fauna.db')


bende.execute('''
             CREATE TABLE fauna(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_fauna VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_skrng INTEGER(10),
                thn_ditemukan INTEGER(10)
             )
             ''')

bende.close()