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
        print(f'Enviando mensagem no formato {format_name}:')
        print(mensagem)
        enviar_mensagem(mensagem)


def enviar_mensagem(mensagem):  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 5001))  # Conectando com o servidor 
        client_socket.send(mensagem.encode())  
    except Exception as e:
        print(f'Erro ao enviar a mensagem: {e}')
    finally:
        client_socket.close()  # Fecha o socket após o uso


if __name__ == '__main__':
    data = {
        'Nome': 'Paloma',
        'CPF': '12994384663',
        'idade': 24,
        'mensagem': 'segue comprovante de endereço'
    }
    envio_msg_serializada(data)
