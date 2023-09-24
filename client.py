import socket, masscan

servers = []

id = "Test_client"

range = "0.0.0.0-255.255.255.255"

port = 420

found_hosts = {}

def run_client(ip, port):
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = ip  # replace with the server's IP address
    server_port = port  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))
    
    i = 0
    
    end = False

    while not(end):
        response = client.recv(1024)
        response = response.decode("utf-8")

        if i == 0:
            msg = "Dynamic IP Rendevous Protocol INIT"
        elif i == 1:
            if response == "Yes, I am a real human person, no skateboards to be found":
                msg = "no clue what you're on, we're computers but im " + id
        elif i == 2:
            if response[52:] in servers:
                found_hosts += {response[52:]:server_ip}

        client.send(msg.encode("utf-8")[:1024])
        i += 1

for ip in masscan.PortScanner()["scan"].keys():
    run_client(ip,port)