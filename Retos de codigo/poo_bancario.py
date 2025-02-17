''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''
class ContaBancaria:
  
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
    def __init__(self, nome):
        self.nome = nome
        self.saldo =0
        self.operacoes =[]

    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
    def depositar(self,deposito):
        self.operacoes.append(f"+{valor}")
        self.saldo += valor
        return self.saldo

    # TODO: Implemente o método para realizar um saque:
    def sacar(self, valor):
        valor = abs(valor)
        # TODO: Verifique se há saldo suficiente para o saque
        if valor <= self.saldo:
            # TODO: Subtraia o valor do saldo (valor já é negativo)
            self.operacoes.append(f"-{valor}" if valor != 0 else f"{valor}" )
            self.saldo -=valor
            
        else:
        # TODO: Registre a operação e retorne a  mensagem de saque negado
            self.operacoes.append(f"Saque não permitido")
            return  "Saque não permitido"
       
            

    # TODO: Crie o método para exibir o extrato da conta e junte as operações no formato correto:
    def extrato (self):
        # mensaje +=  [valor for valor in self.operacoes]
        # print(mensaje)
        print (f"Operações: {', '.join(self.operacoes)}; Saldo: {self.saldo}")
        return f"Operações: {', '.join(self.operacoes)}; Saldo: {self.saldo}"
    


nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

conta.extrato()