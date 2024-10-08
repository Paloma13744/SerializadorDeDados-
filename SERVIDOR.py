import socket
def detectar_formato(data):
    
    if data.startswith('{') and data.endswith('}'):  # JSON
        return 'JSON'
    elif data.startswith('Nome,') or ',' in data:  # CSV
        return 'CSV'
    elif data.startswith('<?xml') or data.startswith('<root>'):  # XML
        return 'XML'
    elif ':' in data and not ('=' in data):  # YAML
        return 'YAML'
    elif '=' in data:  # TOML
        return 'TOML'
    return 'Formato desconhecido'




def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5001))
    server_socket.listen(1)
    print('Servidor esperando por conexões...\n')

    while True:
        client_socket, address = server_socket.accept()
        print(f'\nConexão de {address} estabelecida.')
        data = client_socket.recv(1024).decode()
        formato = detectar_formato(data)
        
        # Exibe o tipo de formato e, em seguida, os dados recebidos formatados
        print(f'Tipo de formato: {formato}')
        print('Dados recebidos:')
        print(f"{data}\n")
      
        client_socket.close()

if __name__ == '__main__':
    iniciar_servidor()