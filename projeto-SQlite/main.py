import sqlite3

conn = sqlite3.connect("meubanco.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER
               )
""")

# Inserindo usuario de exemplo
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("JC", 19))
conn.commit()

# ler usuarios

cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fechar conexão
conn.close()