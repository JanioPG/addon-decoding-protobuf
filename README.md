
# Addon (mitmproxy): Protobuf for Google Analytics 4

### Feature: decodificar o binário protobuf enviado numa request para o endpoint do Google Analtyics 4.
---

## Dependências:
- [Protocol Buffer Compiler v27.2+](https://grpc.io/docs/protoc-installation/)
- [mitmproxy](https://mitmproxy.org/)
- [python 3.12](https://www.python.org/)
- 
## Instalation:
Todos os comandos a seguir devem ser executados na raiz do projeto.
### Ambiente virtual e dependências:
Clone o repositório e, preferencialmente, crie um ambiente virtual.
Para isso, execute no terminal o comando:
`python -m venv venv`
Em seguida, ative o ambiente virtual com o comando:
`source venv/bin/activate`
Com o ambiente virtual ativo, instale as dependências com o comando:
`pip install -r requirements.txt`

### Protocol Buffer Compiler
Acesse a página do [Protocol Buffer Compiler](https://grpc.io/docs/protoc-installation/) e siga as orientações para baixar a versâo mais recente, a partir da v27.2.
Após instalado, execute o seguinte comando:
`protoc --python_out=. appanalytics.proto`
Após executar o comando, o arquivo *appanalytics_pb2.py* será criado na raiz do projeto.
O comando anterior teve o argumento -I omitido, porque por padrâo aponta para o diretório atual. O argumento --python_out também aponta para o diretório atual com o valor '.'.
O arquivo appanalytics.proto é o arquivo presente na raiz do projeto (diretório atual).

## Como utilizar
Com o ambiente virtual ativo e as dependências instaladas, você é capaz de utilizar o mitmproxy (dump) executando o script *decode_protobuf.py*.
Excute o comando:
`mitmdump -s decode-protobuf.py`

###Links úteis:
- [Protocol Buffers Documentation](https://protobuf.dev/): Protocol Buffers are language-neutral, platform-neutral extensible mechanisms for serializing structured data.
- [GA4 Recommended events](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtag): description of GA4 events and parameters.

### Authors
- [@JanioPG](https://github.com/JanioPG)
