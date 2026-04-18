import socket

def iniciar_servidor_udp():
    HOST = '127.0.0.1'
    PORT = 65433

    # Crear socket UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[UDP SERVER] Escuchando en {HOST}:{PORT}...")

        data, addr = s.recvfrom(1024)
        mensaje = data.decode('utf-8')
        print(f"[UDP SERVER] Mensaje recibido de {addr}: '{mensaje}'")

        respuesta = f"Hola desde el servidor UDP! Recibí: '{mensaje}'"
        s.sendto(respuesta.encode('utf-8'), addr)
        print(f"[UDP SERVER] Respuesta enviada a {addr}")

if __name__ == "__main__":
    iniciar_servidor_udp()
