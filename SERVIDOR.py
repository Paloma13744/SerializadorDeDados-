import socket

host = '127.0.0.1'  # Endereço IP do Servidor
port = 5000         # Porta que o Servidor está
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (host, port)
soquete.bind(origem)
soquete.listen(1)  # Escuta por 1 conexão de cada vez

print("Servidor ouvindo...")

while True:
    conexao, cliente = soquete.accept()
    print("Conectado por", cliente)
    
    mensagem = conexao.recv(1024).decode()  # Decodifica a mensagem de bytes
    print("Cliente", cliente[0], "Recebida:", mensagem)
    
    conexao.close()
