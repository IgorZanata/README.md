#Projeto: Sistema de Cadastro de Funcionários
#objetivo Cadastrar funcionários, calcular pagamento e mostrar dados.
#Regras Todo funcionário tem:
#nome salario_base Todo funcionário tem o método:
#calcular_pagamento()
#Classes Classe base
#Funcionario, Classes filha, CLT
#PJ, Horista, Regras de cálculo
#CLT → salário fixo
#PJ → salário - 10% de imposto
#Horista → horas × valor hora
#Funcionalidades
#Cadastrar funcionário
#Listar funcionários
#Calcular pagamento
#Usar herança e polimorfismo

from abc import ABC, abstractmethod


# ===== CLASSES =====
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_pagamento(self):
        pass


class Funcionario_clt(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome)
        self.salario_base = salario_base

    def calcular_pagamento(self):
        return self.salario_base


class Funcionario_horista(Funcionario):
    def __init__(self, nome, horas, valor_hora):
        super().__init__(nome)
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.horas * self.valor_hora


class Funcionario_pj(Funcionario):
    def __init__(self, nome, salario_base, imposto):
        super().__init__(nome)
        self.salario_base = salario_base
        self.imposto = imposto

    def calcular_pagamento(self):
        return self.salario_base - self.imposto



clt = []
horista = []
pj = []



while True:
    try:
        menu = int(input(
            "\n1 Cadastrar\n"
            "2 Exibir\n"
            "3 Exibir todos\n"
            "4 Sair\n--->>> "
        ))
    except ValueError:
        print("Digite apenas números.")
        continue


    if menu == 1:
        try:
            tipo = int(input("1 CLT\n2 Horista\n3 PJ\n--->>> "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if tipo == 1:
            try:
                nome = input("Nome: ").strip().upper()
                salario = float(input("Salário R$: "))
                clt.append(Funcionario_clt(nome, salario))
                print("CLT cadastrado com sucesso!")
            except ValueError:
                print("Erro nos valores.")

        elif tipo == 2:
            try:
                nome = input("Nome: ").strip().upper()
                horas = int(input("Horas trabalhadas: "))
                valor = float(input("Valor da hora R$: "))
                horista.append(Funcionario_horista(nome, horas, valor))
                print("Horista cadastrado com sucesso!")
            except ValueError:
                print("Erro nos valores.")

        elif tipo == 3:
            try:
                nome = input("Nome: ").strip().upper()
                salario = float(input("Salário R$: "))
                imposto = float(input("Imposto R$: "))
                pj.append(Funcionario_pj(nome, salario, imposto))
                print("PJ cadastrado com sucesso!")
            except ValueError:
                print("Erro nos valores.")

        else:
            print("Opção inválida.")


    elif menu == 2:
        try:
            tipo = int(input("1 CLT\n2 Horista\n3 PJ\n--->>> "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if tipo == 1:
            for f in clt:
                print(f.nome, f.calcular_pagamento())

        elif tipo == 2:
            for f in horista:
                print(f.nome, f.calcular_pagamento())

        elif tipo == 3:
            for f in pj:
                print(f.nome, "-", f.calcular_pagamento())

        else:
            print("Opção inválida.")


    elif menu == 3:
        for lista in (clt, horista, pj):
            for f in lista:
                print(f.nome, "-", f.calcular_pagamento())


    elif menu == 4:
        print("Finalizando sistema...")
        break

    else:
        print("Opção inválida.")

