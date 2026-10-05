import sqlite3
conection = sqlite3.connect("clientes.db")
cursor = conection.cursor()
cursor.execute("DROP TABLE IF EXISTS cliente")

cursor.execute("create table cliente(id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cidade TEXT)")
cursor.execute("""
INSERT into cliente (id_cliente, nome, cidade)
VALUES
(6767, 'samuel', 'Ribeirao'),
(4242, 'kaio', 'inferno'),
(6969, 'pedrin', 'uganda');
""")
conection.commit()
cursor.execute("SELECT * FROM cliente")
cliente = cursor.fetchall()
print(cliente)
conection.close()