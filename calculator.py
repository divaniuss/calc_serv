import tkinter as tk
import socket

IP = '127.0.0.1'
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
client.settimeout(1)

def send_to_server(expression):
    client.send(expression.encode())  
    response = client.recv(1024).decode()  
    result_var.set(response)  
CalcCore
root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)


label1 = tk.Label(root, text="Введите выражение число:")
label1.grid(row=0, column=0)

result_var = tk.StringVar()
result_label = tk.Label(root, text="Результат:")
result_label.grid(row=2, column=0)

result_display = tk.Label(root, textvariable=result_var)
result_display.grid(row=2, column=1)

def send():
    send_to_server(f"{entry1.get()}")

send_button = tk.Button(root, text="send", command=send)
send_button.grid(row=3, column=0)


def on_closing():
    client.close()  
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
