

# Cliente-Servidor de Detecção de Formatos

Este projeto implementa um sistema **Cliente-Servidor** para enviar e detectar dados em diferentes formatos de serialização, incluindo **JSON**, **CSV**, **XML**, **YAML** e **TOML**. O servidor recebe dados de um cliente, detecta o formato, e exibe o conteúdo no terminal.

## 🚀 Funcionalidades

- Serialização de dados nos seguintes formatos:
  - JSON
  - CSV
  - XML
  - YAML
  - TOML
  - Envio de dados do cliente para o servidor.
  - Detecção do formato de dados no lado do servidor.

## Instalação de Dependências
``` bash
pip install pyyaml toml
```

``` bash
pip install dicttoxml
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
  - Bibliotecas:
    - `socket` (para comunicação TCP)
    - `csv`, `json`, `yaml`, `toml`, `dicttoxml` (para serialização)
      
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


## 📂 Estrutura do Projeto

└── cliente.py   # Código do cliente responsável por serializar e enviar os dados.

└── servidor.py  # Código do servidor que recebe e detecta o formato dos dados.


## ⚙️ Como Executar

### Servidor
Clone o repositório:

```bash
git clone
```

**Navegue até a pasta do projeto:**
**Execute o servidor:**
```bash
python servidor.py
```
O servidor estará escutando na porta 5001.

**Cliente**
Após iniciar o servidor, execute o cliente em uma nova janela do terminal:
``` bash
python cliente.py
```

Insira os dados solicitados no terminal. O cliente enviará os dados serializados para o servidor em vários formatos.

## 📖 Exemplo de Uso
Ao executar o **cliente**, será solicitado que o usuário insira:

```bash
Informe o seu nome: João
Informe o seu CPF: 123456789
Informe a sua idade: 30
Informe a sua mensagem: Olá, mundo!
```

O servidor exibirá:
```bash
Conexão de ('127.0.0.1', 12345) estabelecida.
Tipo de formato: CSV
Dados recebidos:
Nome,CPF,idade,mensagem
João,123456789,30,Olá, mundo!

Conexão de ('127.0.0.1', 12345) estabelecida.
Tipo de formato: JSON
Dados recebidos:
{"Nome": "João", "CPF": "123456789", "idade": "30", "mensagem": "Olá, mundo!"}
```










