''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

#TODO: Implemente a classe SistemaBancario:
class  SistemaBancario:
    def __init__(self):
    # TODO: Inicialize a lista de contas:
        self.lista_contas =[]
    
    # def criar_conta(self, titular, saldo):
    # # TODO: Crie uma nova conta e adicione à lista de contas:
        
    #     self.lista_contas.append(f"{titular}: R$ {saldo}")
    

    # # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
    # def listar_contas(self):
    #     print(", ".join(self.lista_contas))
    def criar_conta(self, titular, saldo):
        conta = ContaBancaria(titular, saldo)  # Cria uma conta com titular e saldo
        self.lista_contas.append(conta)  # Adiciona à lista de contas

    def listar_contas(self):
        # Formata a saída corretamente no formato desejado
        saida = ", ".join([f"{conta.titular}: R$ {conta.saldo}" for conta in self.lista_contas])
        print(saida)

#TODO: Crie uma instância de SistemaBancario:
sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()