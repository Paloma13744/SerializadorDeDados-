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
        # Desserializa os dados JSON
        dados = json.loads(data)
        return dados
    elif formato == 'CSV':
        # Desserializa os dados CSV
        reader = csv.DictReader(io.StringIO(data))
        dados = list(reader)
        return dados[0] if dados else None  # Retorna o primeiro registro ou None se vazio
    elif formato == 'XML':
        return desserializar_xml(data)
    elif formato == 'YAML':
        dados = yaml.safe_load(data)
        return dados
    elif formato == 'TOML':
        dados = toml.loads(data)
        return dados
    return None

def desserializar_xml(data):
    root = ET.fromstring(data)
    resultado = {}
    for child in root:
        resultado[child.tag] = child.text
    return resultado

def salvar_dados(dados, formato):
    save_path = "C:\\Users\\0056515\\Documents\\"
    
    if formato == 'JSON':
        with open(save_path + 'dados.json', 'w') as file:
            json.dump(dados, file, indent=4)
    elif formato == 'CSV':
        with open(save_path + 'dados.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=dados.keys())
            writer.writeheader()
            writer.writerow(dados)
    elif formato == 'XML':
        # Para XML, você deve converter os dados de volta para string antes de salvar
        xml_string = dict_to_xml(dados)
        with open(save_path + 'dados.xml', 'w') as file:
            file.write(xml_string)
    elif formato == 'YAML':
        with open(save_path + 'dados.yaml', 'w') as file:
            yaml.safe_dump(dados, file)
    elif formato == 'TOML':
        with open(save_path + 'dados.toml', 'w') as file:
            toml.dump(dados, file)

def dict_to_xml(data):
    root = ET.Element('root')
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    return ET.tostring(root, encoding='unicode')

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

    # Salva os dados no formato apropriado
    salvar_dados(dados_desserializados, formato)
    
    # Exibe o tipo de formato e, em seguida, os dados recebidos
    print(f'Tipo de formato: {formato}')
    print('Dados recebidos:')
    print(dados_desserializados, '\n')
      
    client_socket.close()

if __name__ == '__main__':
    iniciar_servidor()
