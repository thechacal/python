'''
Esse código implementa um programa de busca na web que baixa arquivos de um servidor web. Ele utiliza threads para baixar múltiplos arquivos simultaneamente, e os arquivos são baixados em pedaços.

O programa aceita vários argumentos da linha de comando, incluindo o número máximo de conexões concorrentes, o endereço IP do servidor web, a página inicial e os nomes dos arquivos para baixar. Ele se conecta ao servidor, envia solicitações HTTP GET e baixa os arquivos em pedaços, exibindo informações sobre o progresso do download.

As classes File, WebFetcher, WebFetcherRunnable e TcpConnect são usadas para organizar o código e realizar as operações necessárias. O programa principal é executado na função main() e inicia a instância da classe WebFetcher para iniciar o processo de download.
'''
import socket  # Importa o módulo de soquete para comunicação de rede
import threading  # Importa o módulo de threading para criar threads concorrentes
import sys  # Importa o módulo sys para acessar os argumentos da linha de comando

# Classe que representa um arquivo para ser baixado
class File:
    def __init__(self, name, host):
        self.f_name = name  # Nome do arquivo
        self.f_host = host  # Host de onde baixar o arquivo
        self.f_fd = -1  # Descritor de arquivo
        self.f_flags = 0  # Flags para controle
        self.f_tid = None  # Thread ID (ID da thread)

# Classe principal que realiza o download dos arquivos da web
class WebFetcher:
    def __init__(self):
        self.MAXFILES = 20  # Número máximo de arquivos para baixar
        self.SERV = '80'  # Porta HTTP padrão
        self.files = [None] * self.MAXFILES  # Lista de arquivos
        self.nconn = 0  # Número de conexões ativas
        self.nfiles = 0  # Número de arquivos para baixar
        self.nlefttoconn = 0  # Número de arquivos restantes para conectar
        self.nlefttoread = 0  # Número de arquivos restantes para ler
        self.ndone = 0  # Número de arquivos concluídos
        self.ndoneMutex = {}  # Mutex para controle de threads
        self.ndoneLock = {}  # Bloqueio para controle de threads
        self.ndoneCond = {}  # Condição para controle de threads
        self.ndoneLock = threading.Lock()  # Inicializa o bloqueio
        self.ndoneCond = threading.Condition(self.ndoneLock)  # Inicializa a condição

    # Método para iniciar o processo de download
    async def start(self, args, maxnconn):
        self.nfiles = min(len(args) - 3, self.MAXFILES)  # Calcula o número de arquivos para baixar

        # Cria objetos File para cada arquivo a ser baixado
        for i in range(self.nfiles):
            self.files[i] = File(args[i + 3], args[1])

        print('nfiles = ' + str(self.nfiles))  # Exibe o número de arquivos

        # Realiza a requisição da página inicial
        await self.homePage(args[1], args[2])

        self.nlefttoread = self.nlefttoconn = self.nfiles  # Inicializa contadores
        self.nconn = 0  # Inicializa o número de conexões ativas

        # Loop principal para baixar os arquivos
        while self.nlefttoread > 0:
            while self.nconn < maxnconn and self.nlefttoconn > 0:
                i = 0
                while i < self.nfiles:
                    if self.files[i].f_flags == 0:
                        break
                    i += 1

                if i == self.nfiles:
                    print('nlefttoconn = ' + str(self.nlefttoconn) + ' but nothing found')
                    return

                # Configura a flag e inicia uma nova thread para baixar o arquivo
                self.files[i].f_flags = 1
                file = self.files[i]
                file.f_tid = WebFetcherRunnable(file)
                file.f_tid.start()
                self.nconn += 1
                self.nlefttoconn -= 1

            # Aguarda até que os arquivos sejam baixados
            self.ndoneLock.acquire()
            try:
                while self.ndone == 0:
                    self.ndoneCond.wait()

                for i in range(self.nfiles):
                    if (self.files[i].f_flags & 4) != 0:
                        fptr = self.files[i].f_tid
                        fptr.f_flags = 8
                        self.ndone -= 1
                        self.nconn -= 1
                        self.nlefttoread -= 1
                        print('thread ' + str(fptr.f_tid) + ' for ' + fptr.f_name + ' done')
            finally:
                self.ndoneLock.release()

    # Método para baixar a página inicial
    async def homePage(self, host, fname):
        try:
            fd = await TcpConnect.connect(host, self.SERV)  # Conecta-se ao servidor HTTP
            request = f'GET {fname} HTTP/1.0\r\n\r\n'  # Requisição GET para a página inicial

            # Envia a requisição para o servidor
            with open(fd, 'wb') as out:
                out.write(request.encode())

            # Lê a resposta do servidor
            with open(fd, 'rb') as reader:
                chunk = reader.read(1024)
                while chunk:
                    print(f'read {len(chunk)} bytes of home page')
                    chunk = reader.read(1024)

            print('end-of-file on home page')

        except Exception as e:
            print('Error:', e)

# Classe que representa uma thread para baixar um arquivo
class WebFetcherRunnable:
    def __init__(self, file):
        self.fptr = file

    def start(self):
        self.run()

    async def run(self):
        try:
            fd = await TcpConnect.connect(self.fptr.f_host, WebFetcher.SERV)  # Conecta-se ao servidor
            self.fptr.f_fd = fd

            print('do_get_read for ' + self.fptr.f_name + ', fd ' + str(fd) + ', thread ' + str(self.fptr.f_tid))

            self.writeGetCmd(self.fptr)  # Envia comando GET para o servidor

            # Lê os dados do arquivo baixado
            with open(fd, 'rb') as reader:
                chunk = reader.read(1024)
                while chunk:
                    print(f'read {len(chunk)} bytes from {self.fptr.f_name}')
                    chunk = reader.read(1024)

            print('end-of-file on ' + self.fptr.f_name)
            self.fptr.f_flags = 4

            # Notifica a conclusão da thread
            self.ndoneLock.acquire()
            try:
                self.ndone += 1
                self.ndoneCond.notify()
            finally:
                self.ndoneLock.release()

        except Exception as e:
            print('Error:', e)

    # Método para enviar o comando GET para o servidor
    def writeGetCmd(self, fptr):
        line = f'GET {fptr.f_name} HTTP/1.0\r\n\r\n'
        with open(fptr.f_fd, 'wb') as out:
            out.write(line.encode())
        print(f'wrote {len(line)} bytes for {fptr.f_name}')

# Classe para realizar a conexão TCP
class TcpConnect:
    @staticmethod
    async def connect(host, serv):
        try:
            # Realiza a conexão TCP com o host e a porta especificados
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(serv)))
            return s

        except Exception as e:
            print('Error:', e)
            return -1

# Função principal
def main():
    args = sys.argv[1:]  # Obtém os argumentos da linha de comando
    if len(args) < 4:
        print('Usage: python WebFetcher.py <#conns> <IPaddr> <homepage> file1 ...')
    else:
        maxnconn = int(args[0])
        webFetcher = WebFetcher()
        webFetcher.start(args, maxnconn)

if __name__ == '__main__':
    main()  # Executa a função principal se o script for executado diretamente