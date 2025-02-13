"""
Descrição
Você foi solicitado a criar um programa que analise uma lista de transações bancárias e filtre apenas aquelas que ultrapassam um valor limite. Seu programa deve retornar uma nova lista contendo somente as transações cujo valor absoluto (ignorar sinal negativo) seja maior que o limite informado.

Atenção:
As transações incluem tanto depósitos (positivos) quanto saques (negativos).
Valor absoluto é o critério para filtrar, então tanto 300 (depósito) quanto -150 (saque) serão considerados, já que ambos têm módulo maior que 100.
Entrada
Uma lista de valores representando as transações bancárias (ex.: [100, -50, 300, -150]).
Um valor limite (inteiro ou decimal) fornecido pelo usuário.
Saída
Uma nova lista com as transações que ultrapassam o limite, no formato: "Transações: [X, Y, Z]"

"""


def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # TODO: Itere sobre cada transação na lista:
    for transacao in transacoes:
        # TODO: Verifique se o valor absoluto da transação é maior que o limite:
        if abs(transacao) > limite :
            # TODO: Adicione a transação à lista filtrada:
            transacoes_filtradas.append(transacao)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
limite = float(limite.strip())  # Converte o limite para float


transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# TODO: Filtre as transações que ultrapassam o limite:
resultado = filtrar_transacoes(transacoes, limite)


print(f"Transações: {resultado}")