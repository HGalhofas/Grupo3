import json
import socket

# Classe que representa um item de tarefa
class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

# Classe que representa uma lista de tarefas
class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, title, description):
        item = TodoItem(title, description)
        self.items.append(item)

    def complete_item(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Invalid index")
        self.items[index].completed = True

    def display_items(self):
        result = ""
        for i, item in enumerate(self.items):
            status = "[x]" if item.completed else "[ ]"
            result += f"{i}. {status} {item.title}: {item.description}\n"
        return result

    def count_incomplete_items(self):
        # Retorna a contagem de itens que ainda não estão completos
        return sum(1 for item in self.items if not item.completed)

# Configuração do servidor
host = 'localhost'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print(f"Servidor iniciado e escutando na porta {port}...")

todo_list = TodoList()

# Loop para aceitar e processar conexões de clientes
while True:
    print("Aguardando conexão...")
    client_socket, address = server_socket.accept()
    print(f"Conectado a {address}")

    # Recebe o comando do cliente
    command = client_socket.recv(1024).decode()
    print(f"Comando recebido: {command}")
    
    # Processa o comando
    try:
        choice, data = command.split("-")
        if choice == "1":
            title, description = data.split(",")
            todo_list.add_item(title, description)
            result = "Todo added."
        elif choice == "2":
            result = todo_list.display_items()
        elif choice == "3":
            index = int(data)
            todo_list.complete_item(index)
            result = "Todo completed."
        elif choice == "4":
            # Novo comando para contar itens incompletos
            count = todo_list.count_incomplete_items()
            result = f"Number of incomplete todos: {count}"
        else:
            result = "Invalid command."
    except Exception as e:
        result = f"Error: {str(e)}"
    
    print("Resposta enviada ao cliente: " + result)
    client_socket.send(result.encode())
    client_socket.close()
