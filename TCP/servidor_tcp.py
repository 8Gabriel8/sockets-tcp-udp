import socket

def iniciar_cliente_tcp():
    HOST = '127.0.0.1'
    PORT = 65432

    # Conectarse al servidor TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[TCP CLIENT] Conectado al servidor {HOST}:{PORT}")

        mensaje = "Hola servidor, soy el cliente TCP!"
        s.sendall(mensaje.encode('utf-8'))
        print(f"[TCP CLIENT] Mensaje enviado: '{mensaje}'")

        data = s.recv(1024)
        respuesta = data.decode('utf-8')
        print(f"[TCP CLIENT] Respuesta recibida: '{respuesta}'")

if __name__ == "__main__":
    iniciar_cliente_tcp()
