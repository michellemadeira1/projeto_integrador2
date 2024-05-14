import MySQLdb

# Configurações de conexão com o banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'agenda_psico2',
}

# Estabelece a conexão com o banco de dados
conn = MySQLdb.connect(**db_config)

# Cria um cursor para executar consultas SQL
cursor = conn.cursor()

# Exemplo de consulta SQL
consulta = "SELECT * FROM tabela_exemplo"

# Executa a consulta
cursor.execute(consulta)

# Obtém os resultados
resultados = cursor.fetchall()

# Imprime os resultados
for linha in resultados:
    print(linha)

# Fecha o cursor e a conexão
cursor.close()
conn.close()
