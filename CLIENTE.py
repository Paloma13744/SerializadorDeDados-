import socket
import csv
import io
import json
import dicttoxml
import yaml
import toml

def serialize_csv(data):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)
    return output.getvalue().strip()

def serialize_json(data):
    return json.dumps(data)

def serialize_xml(data):
    return dicttoxml.dicttoxml(data).decode()

def serialize_yaml(data):
    return yaml.dump(data)

def serialize_toml(data):
    return toml.dumps(data)

def envio_msg_serializada(data):
    formats = {
        'CSV':  serialize_csv,
        'JSON': serialize_json,
        'XML': serialize_xml,
        'YAML': serialize_yaml,
        'TOML': serialize_toml
    }

    for format_name, serializer in formats.items():
        mensagem = serializer(data)
        enviar_mensagem(mensagem)

def enviar_mensagem(mensagem):  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 5001))  # Conectando com o servidor 
        client_socket.send(mensagem.encode())  
    except Exception as e:
        print(f'Erro ao enviar a mensagem: {e}')
    finally:
        client_socket.close() 

if __name__ == '__main__':
    nome = input('Informe o seu nome: ')
    cpf = input('Informe o seu CPF: ')
    idade = input('Informe a sua idade: ')
    mensagem = input('Informe a sua mensagem: ')

    # Criando aqui o dicionário com os dados
    data = {
        'Nome': nome,
        'CPF': cpf,
        'Idade': idade,
        'Mensagem': mensagem
    }

    # Envio das mensagens serializadas
    envio_msg_serializada(data)
