import socket
import sys

def send_commands(s, conn):
    print("$: ", end="")
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(4096)
                print(data.decode("utf-8"), end="")
        except KeyboardInterrupt:
            print("\nServer Exited...")
            conn.close()
            sys.exit()
        except Exception as e:
            print(e)
            conn.close()
            e.close()
            sys.exit()

def server(address):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(address)
    s.listen()
    print("Server listening for incoming connections...")
    conn, client_addr = s.accept()
    print(f"Connected to {client_addr}")
    send_commands(s, conn)

if __name__ == "__main__":
    host = "192.168.1.3"
    port = 19876
    server((host, port))
        
        
