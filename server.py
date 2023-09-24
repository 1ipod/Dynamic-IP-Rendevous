import socket

id = "Name_Here"

clients = []

port = 420

def run_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    server.bind((server_ip, port))
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    i = 0

    end = False

    while not(end):
        request = client_socket.recv(1024)
        request = request.decode("utf-8")

        if i == 0:
            if request == "Dynamic IP Rendevous Protocol INIT":
                msg = "Yes, I am a real human person, no skateboards to be found"
            else:
                msg = "https://github.com/1ipod/Dynamic-IP-Rendevous"
                end = True
        elif i == 1:
            if request[47:] in clients:
                msg = "I am human, defenitely not cow man my human name is " + id
            else:
                msg = "Huzza I'm the skateboard cow killer"
                end = True

        server.send(msg.encode("utf-8")[:1024])
        i += 1

while True:
    run_server(port)
