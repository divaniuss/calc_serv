import socket
import pyodbc

server_base = r'localhost\SQLEXPRESS'  
database = 'CalculatorDB'

dsn = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_base};DATABASE={database};Trusted_Connection=yes'

IP = '127.0.0.1'
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)
print("Сервер запущен, ожидание подключения...")

conn, addr = server.accept()
print(f"Подключение от: {addr}")

while True:
    try:
        request = conn.recv(1024).decode().strip()
        if not request:
            break  

        allowed_chars = "0123456789+-*/(). "
        if not all(char in allowed_chars for char in request):
            conn.send("Ошибка: Некорректный ввод. Разрешены только числа и операторы +, -, *, /".encode())
        else:
            expression = request
            result = eval(expression)

            result_str = f"Результат: {result}"

            conn.send(result_str.encode())

    except Exception as e:
        conn.send(f"Ошибка: {e}".encode())

print("Клиент отключился, сервер завершает работу.")
conn.close()
server.close()
