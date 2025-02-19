from models import *
from views import *
from datetime import datetime

class UI:
  def start(self):
    while True:
      print('''
      [1] -> Criar conta
      [2] -> Desativar conta
      [3] -> Transferir dinheiro
      [4] -> Movimentar dinheiro
      [5] -> Total contas
      [6] -> Filtrar histórico
      [7] -> Gráfico
            ''')
      
      choice = int(input("Escolha uma opção: "))
      match choice:
        case 1:
          self._criar_conta()
        case 2:
          self._desativar_conta()
        case 3:
          self._transferir_saldo()
        case 4:
          self._movimentar_dinheiro()
        case 5:
          self._total_contas()
        case 6:
          self._filtrar_movimentacoes()
        case 7:
          self._criar_grafico()

  def _criar_conta(self):
    print("Digite o nome de algum dos bancos abaixo:")

    for banco in Bancos:
      print(f"---{banco.value}---")

    banco = input().title()
    valor = float(input("Digite o valor em sua conta: "))

    conta = Conta(banco=Bancos(banco), valor=valor)
    criar_conta(conta)

  def _desativar_conta(self):
    print("Escolha a conta que deseja desativar: ")

    for i in listar_contas():
      if i.saldo == 0:
        print(f"{i.id} -> {i.banco.value} -> R${i.saldo}")
      
      id_conta = int(input())

      try:
        desativar_conta(id_conta)
        print("Conta desativada com sucesso!")
      except ValueError:
        print("Esta conta ainda possui saldo. Faça uma transferência!")

  def _transferir_saldo(self):
    print("Escolha uma conta para retirar o dinheiro:")
    for i in listar_contas():
      if i.status == Status.ATIVO:
        print(f"{i.id} -> {i.banco.value} -> R${i.saldo}")

    conta_retirar_id = int(input())

    print("Escolha a conta para enviar o dinheiro:")
    for i in listar_contas():
      if i.id != conta_retirar_id and i.status == Status.ATIVO:
        print(f"{i.id} -> {i.banco.value} -> R${i.saldo}")

    conta_enviar_id = int(input())

    valor = float(input("Digite o valor para transferir: "))
    transferir_saldo(conta_retirar_id, conta_enviar_id, valor)

  def _movimentar_dinheiro(self):
    print("Escolha a conta:")
    for i in listar_contas():
      if i.status == Status.ATIVO:
        print(f"{i.id} -> {i.banco.value} -> R${i.saldo}")

    conta_id = int(input())
    valor = int(input("Digite o valor movimentado: "))

    print("Selecione o tipo de movimentação:")
    for tipo in Tipos:
      print(f"---{tipo.value}---")

    tipo = input().title()
    historico = Historico(conta_id=conta_id, tipo=Tipos(tipo), valor=valor, data=date.today())
    
    movimentar_dinheiro(historico)

  def _total_contas(self):
    print(f"R${total_contas()}")

  def _filtrar_movimentacoes(self):
    data_inicio = input("Digite a data de início: ")
    data_fim = input("Digite a data de fim: ")

    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
    data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()

    for i in buscar_historico_entre_datas(data_inicio, data_fim):
      print(f"{i.valor} - {i.tipo.value}")

  def _criar_grafico(self):
    criar_grafico_por_contas()

UI().start()

