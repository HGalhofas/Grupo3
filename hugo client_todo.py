import socket

host = 'localhost'  # assume que o servidor está rodando localmente
port = 12345        # número da porta que deve coincidir com o servidor

def send_command(command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server.")
    client_socket.send(command.encode())
    result = client_socket.recv(1024).decode()
    client_socket.close()
    print("Connection closed.")
    return result

def menu():
    while True:
        print("** Todo List Menu **")
        print("1. Add todo")
        print("2. Print todos")
        print("3. Complete todo")
        print("4. Count incomplete todos")  # Nova opção no menu
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter todo title: ")
            description = input("Enter todo description: ")
            command = f"1-{title},{description}"
            result = send_command(command)
            print(result)

        elif choice == "2":
            print("Print todos")
            command = "2-"
            result = send_command(command)
            print(result)

        elif choice == "3":
            print("Complete todo")
            index = int(input("Enter index: "))
            command = f"3-{index}"
            result = send_command(command)
            print(result)

        elif choice == "4":
            # Envia comando para contar os itens incompletos
            command = "4-"
            result = send_command(command)
            print(result)

        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

menu()
