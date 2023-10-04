'''
Este código em Python cria um servidor UDP que ouve e processa mensagens recebidas em uma porta específica. Ele também inclui classes para representar informações de controle associadas a pacotes de datagrama UDP.

Aqui está uma descrição do que o código faz:

1. Importamos o módulo `socket` para lidar com comunicações de rede.

2. A classe `ExtendedDatagramPacket` é definida para representar um pacote de datagrama UDP estendido. Ele possui os seguintes atributos:
   - `buffer`: O conteúdo do pacote.
   - `length`: O comprimento do pacote.
   - `source_address`: O endereço de origem do pacote.
   - `destination_address`: O endereço de destino do pacote.
   - `interface_index`: O índice da interface associada ao pacote.
   Além disso, a classe fornece métodos para obter esses atributos.

3. A classe `ControlInfo` é definida para criar informações de controle com base em um objeto `ExtendedDatagramPacket`. Ela extrai os atributos de endereço de origem, endereço de destino e índice de interface do pacote. Também fornece métodos para obter esses atributos.

4. A classe `UDPServerWithControlInfo` representa um servidor UDP com informações de controle. No construtor, criamos um socket UDP e o vinculamos ao endereço local e à porta especificada.

5. O método `start_server` inicia o servidor e aguarda mensagens UDP. Quando uma mensagem é recebida, criamos um objeto `ExtendedDatagramPacket` com base nela, em seguida, criamos um objeto `ControlInfo`. Em seguida, exibimos informações sobre a mensagem e as informações de controle no console.

6. No bloco `if __name__ == "__main__":`, definimos a porta do servidor e iniciamos o servidor UDP com a porta especificada.

Basicamente, o código cria um servidor UDP simples que é capaz de receber mensagens UDP e extrair informações de controle dessas mensagens, exibindo essas informações no console.
'''
import socket

# Classe ExtendedDatagramPacket representa um pacote de datagrama UDP estendido
class ExtendedDatagramPacket:
    def __init__(self, buf, length, source_address, destination_address, interface_index):
        self.buffer = buf
        self.length = length
        self.source_address = source_address
        self.destination_address = destination_address
        self.interface_index = interface_index

    def get_source_address(self):
        return self.source_address

    def get_destination_address(self):
        return self.destination_address

    def get_interface_index(self):
        return self.interface_index

# Classe ControlInfo cria informações de controle com base em um objeto ExtendedDatagramPacket
class ControlInfo:
    def __init__(self, packet):
        if isinstance(packet, ExtendedDatagramPacket):
            self.source_address = packet.get_source_address()
            self.destination_address = packet.get_destination_address()
            self.interface_index = packet.get_interface_index()

    def get_source_address(self):
        return self.source_address

    def get_destination_address(self):
        return self.destination_address

    def get_interface_index(self):
        return self.interface_index

# Classe UDPServerWithControlInfo representa um servidor UDP com informações de controle
class UDPServerWithControlInfo:
    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', port))  # Liga o socket ao endereço local

    def start_server(self):
        print(f"UDP server listening on port {self.port}")
        while True:
            message, remote_address = self.socket.recvfrom(1024)  # Recebe uma mensagem e o endereço remoto
            packet = ExtendedDatagramPacket(message, len(message), remote_address[0], 'localhost', 0)
            control_info = ControlInfo(packet)

            # Exibe informações sobre a mensagem e as informações de controle no console
            print(f"Received: {message.decode()}")
            print(f"Source Address: {control_info.get_source_address()}")
            print(f"Destination Address: {control_info.get_destination_address()}")
            print(f"Interface Index: {control_info.get_interface_index()}")

if __name__ == "__main__":
    port = 12345
    server = UDPServerWithControlInfo(port)
    server.start_server()
