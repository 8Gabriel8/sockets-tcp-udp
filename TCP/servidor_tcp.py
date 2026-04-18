import socket

def iniciar_servidor_tcp():
    HOST = '127.0.0.1'
    PORT = 65432

    # Crear socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[TCP SERVER] Escuchando en {HOST}:{PORT}...")

        conn, addr = s.accept()
        with conn:
            print(f"[TCP SERVER] Conectado por {addr}")
            data = conn.recv(1024)
            mensaje = data.decode('utf-8')
            print(f"[TCP SERVER] Mensaje recibido: '{mensaje}'")

            respuesta = f"Hola desde el servidor TCP! Recibí tu mensaje: '{mensaje}'"
            conn.sendall(respuesta.encode('utf-8'))
            print(f"[TCP SERVER] Respuesta enviada.")

if __name__ == "__main__":
    iniciar_servidor_tcp()
