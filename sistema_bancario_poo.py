# Sistema bancário atualizado com classes (POO) e menu interativo

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"

class ContaCorrente:
    LIMITE_SAQUES = 3

    def __init__(self, numero, cliente):
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\n❌ Valor de depósito inválido.")

    def sacar(self, valor):
        limite = 500
        if valor <= 0:
            print("\n❌ Valor de saque inválido.")
        elif valor > self.saldo:
            print("\n❌ Saldo insuficiente.")
        elif valor > limite:
            print("\n❌ Valor do saque excede o limite permitido.")
        elif self.numero_saques >= ContaCorrente.LIMITE_SAQUES:
            print("\n❌ Número de saques diários excedido.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print(f"\n=== Extrato da Conta {self.numero} ===")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for operacao in self.extrato:
                print(operacao)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("==============================")

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def criar_cliente(self):
        nome = input("Informe o nome do cliente: ")
        cpf = input("Informe o CPF: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Informe o endereço (Rua, nº - Bairro - Cidade/UF): ")
        cliente = Cliente(nome, cpf, data_nascimento, endereco)
        self.clientes.append(cliente)
        print("\n✅ Cliente criado com sucesso!")
        return cliente

    def criar_conta(self, cliente):
        numero = str(len(self.contas) + 1).zfill(4)
        conta = ContaCorrente(numero=numero, cliente=cliente)
        self.contas.append(conta)
        print(f"\n✅ Conta {numero} criada com sucesso para {cliente.nome}!")
        return conta

    def localizar_conta(self, cpf):
        for conta in self.contas:
            if conta.cliente.cpf == cpf:
                return conta
        return None

# ====== Execução ======
banco = Banco()

menu = """
[u] Criar usuário
[cc] Criar conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

while True:
    opcao = input(menu)

    if opcao == "u":
        banco.criar_cliente()

    elif opcao == "cc":
        cpf = input("Informe o CPF do cliente: ")
        cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
        if cliente:
            banco.criar_conta(cliente)
        else:
            print("\n❌ Cliente não encontrado.")

    elif opcao in ["d", "s", "e"]:
        cpf = input("Informe o CPF do titular da conta: ")
        conta = banco.localizar_conta(cpf)
        if not conta:
            print("\n❌ Conta não encontrada.")
            continue

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)

        elif opcao == "e":
            conta.exibir_extrato()

    elif opcao == "q":
        print("\nObrigado por usar nosso sistema bancário! Até logo.")
        break

    else:
        print("\n❌ Opção inválida. Tente novamente.")
