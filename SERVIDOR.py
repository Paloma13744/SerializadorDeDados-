import socket
import csv
import io
import json
import xml.etree.ElementTree as ET
import yaml
import toml
import threading

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

def desserializar_data(data, formato):
    if formato == 'JSON':
        return json.loads(data)
    elif formato == 'CSV':
        reader = csv.DictReader(io.StringIO(data))
        return list(reader)[0]  # Retorna o primeiro registro
    elif formato == 'XML':
        return desserializar_xml(data)
    elif formato == 'YAML':
        return yaml.safe_load(data)
    elif formato == 'TOML':
        return toml.loads(data)
    return None

def desserializar_xml(data):
    root = ET.fromstring(data)
    resultado = {}
    for child in root:
        resultado[child.tag] = child.text
    return resultado

def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5001))
    server_socket.listen(5)
    print('Servidor esperando por conexões...\n')

    while True:
        client_socket, address = server_socket.accept()
        print(f'\nConexão de {address} estabelecida.')
        threading.Thread(target=processar_cliente, args=(client_socket,)).start()

def processar_cliente(client_socket):
    data = client_socket.recv(1024).decode()
    formato = detectar_formato(data)
    
    # Desserializa os dados recebidos
    dados_desserializados = desserializar_data(data, formato)
    
    # Exibe o tipo de formato e, em seguida, os dados recebidos
    print(f'Tipo de formato: {formato}')
    print('Dados recebidos:')
    print(dados_desserializados, '\n')
      
    client_socket.close()

if __name__ == '__main__':
    iniciar_servidor()
