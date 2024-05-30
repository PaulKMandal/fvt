import socket

def start_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        data_to_send = "Hello, Server!"
        print(f"Sending data: {data_to_send}")
        s.sendall(data_to_send.encode())
        data = s.recv(1024)
        print(f"Received data: {data.decode()}")

if __name__ == "__main__":
    start_client()
