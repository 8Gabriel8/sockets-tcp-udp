import socket

def iniciar_cliente_udp():
    HOST = '127.0.0.1'
    PORT = 65433

    # Enviar mensaje sin conexión previa (UDP)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        mensaje = "Hola servidor, soy el cliente UDP!"
        s.sendto(mensaje.encode('utf-8'), (HOST, PORT))
        print(f"[UDP CLIENT] Mensaje enviado a {HOST}:{PORT}: '{mensaje}'")

        data, addr = s.recvfrom(1024)
        respuesta = data.decode('utf-8')
        print(f"[UDP CLIENT] Respuesta recibida de {addr}: '{respuesta}'")

if __name__ == "__main__":
    iniciar_cliente_udp()
