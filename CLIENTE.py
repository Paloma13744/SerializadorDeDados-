import socket

host = '127.0.0.1'     # Endereço IP do Servidor
porta = 5000           # Porta que o Servidor está
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (host, porta)

# Conecta ao servidor
soquete.connect(destino)

# Envia a mensagem (convertida para bytes)
soquete.sendall(b"Ola Mundo!")  # Use b"" para enviar uma string como bytes

# Fecha o socket
soquete.close()

