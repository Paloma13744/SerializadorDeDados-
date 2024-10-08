import socket

def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5001))
    server_socket.listen(1)
    print('Servidor esperando por conexões...')

    while True:
        client_socket, address = server_socket.accept()
        print(f'Conexão de {address} estabelecida.')
        data = client_socket.recv(1024).decode()
        print('Dados recebidos:')
        print(data)
        client_socket.close()

if __name__ == '__main__':
    iniciar_servidor()
