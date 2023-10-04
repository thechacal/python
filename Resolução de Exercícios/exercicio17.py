'''
Este código em Python cria um cliente de rede TCP que se conecta a um servidor em um determinado hostname e porta e recebe dados do servidor. Aqui está uma descrição detalhada do que o código faz:

1. Importa os módulos necessários: O código importa os módulos `socket` e `sys` para trabalhar com sockets e lidar com argumentos da linha de comando, respectivamente.

2. Define a classe `NetworkClient`: Esta classe encapsula a lógica do cliente de rede TCP. Ela tem os seguintes métodos:

   - `__init__(self, hostname, port)`: O construtor da classe recebe o hostname (ou endereço IP) do servidor e o número da porta como parâmetros e inicializa os atributos do cliente.

   - `connect(self)`: Este método tenta estabelecer uma conexão TCP com o servidor especificado pelo hostname e porta. Se a conexão for bem-sucedida, exibe uma mensagem de conexão.

   - `receive_data(self)`: Este método fica em um loop infinito para receber dados do servidor. Ele recebe os dados em blocos de 1024 bytes, exibe o tamanho dos dados e imprime os dados recebidos como uma string decodificada.

   - `close_connection(self)`: Este método fecha a conexão com o servidor e exibe uma mensagem indicando que a conexão foi fechada.

3. Bloco `if __name__ == "__main__"`: Neste bloco, o código verifica se foram fornecidos os argumentos corretos na linha de comando. Os argumentos esperados são o hostname (ou endereço IP) do servidor e o número da porta. Se os argumentos não estiverem corretos, exibe uma mensagem de uso e encerra o programa.

4. Cria uma instância do cliente: O código cria uma instância da classe `NetworkClient` com base nos argumentos da linha de comando (hostname e porta).

5. Conecta-se ao servidor: Chama o método `connect()` para estabelecer uma conexão TCP com o servidor.

6. Recebe dados do servidor: Chama o método `receive_data()` para receber dados do servidor. O loop permanece ativo até que não haja mais dados para receber.

7. Fecha a conexão: Após receber todos os dados, chama o método `close_connection()` para fechar a conexão com o servidor.

Em resumo, este código cria um cliente TCP simples que se conecta a um servidor em um hostname e porta específicos, recebe e exibe os dados recebidos e lida com erros e encerramentos de conexão de maneira apropriada. É útil para testar a comunicação com um servidor TCP.
'''
import socket
import sys

# Classe para representar um cliente de rede TCP
class NetworkClient:
    def __init__(self, hostname, port):
        self.hostname = hostname  # Armazena o hostname ou endereço IP do servidor
        self.port = port  # Armazena o número da porta do servidor
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um objeto de socket TCP

    def connect(self):
        try:
            self.socket.connect((self.hostname, self.port))  # Tenta estabelecer a conexão com o servidor
            peer_address, peer_port = self.socket.getpeername()  # Obtém as informações do servidor remoto
            print(f"Connected to {peer_address}:{peer_port}")  # Exibe uma mensagem de conexão bem-sucedida
        except Exception as e:
            print("Error:", e)
            sys.exit(1)  # Em caso de erro, exibe uma mensagem de erro e encerra o programa

    def receive_data(self):
        while True:
            try:
                data = self.socket.recv(1024)  # Recebe dados do servidor em blocos de 1024 bytes
                if not data:
                    break  # Se não houver mais dados para receber, sai do loop
                print(f"{len(data)} bytes from {self.hostname}:{self.port}")  # Exibe o tamanho dos dados recebidos
                print(data.decode())  # Decodifica e imprime os dados recebidos como uma string
            except Exception as e:
                print("Error:", e)
                break  # Em caso de erro, sai do loop

    def close_connection(self):
        self.socket.close()  # Fecha a conexão com o servidor
        print("Connection closed")  # Exibe uma mensagem indicando que a conexão foi fechada

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python NetworkClient.py <hostname or IP address> <service or port#>")
        sys.exit(1)  # Verifica se foram fornecidos os argumentos corretos na linha de comando e exibe uma mensagem de uso

    hostname = sys.argv[1]  # Obtém o hostname ou endereço IP do servidor a partir dos argumentos
    port = int(sys.argv[2])  # Obtém o número da porta do servidor a partir dos argumentos

    client = NetworkClient(hostname, port)  # Cria uma instância do cliente de rede
    client.connect()  # Conecta-se ao servidor
    client.receive_data()  # Recebe dados do servidor
    client.close_connection()  # Fecha a conexão com o servidor
