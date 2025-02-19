from models import Conta, engine, Bancos, Status, Historico, Tipos
from sqlmodel import Session, select
from datetime import date, timedelta
import matplotlib.pyplot as plt

def criar_conta(conta: Conta):
  with Session(engine) as session:
    statement = select(Conta).where(Conta.banco==conta.banco)
    results = session.exec(statement).all()
    print(results)

    if results:
      print("Já existe uma conta neste banco.")
      return

    session.add(conta)
    session.commit()
    return conta

def listar_contas():
  with Session(engine) as session:
    statement = select(Conta)
    results = session.exec(statement).all()
  return results

def desativar_conta(id):
  with Session(engine) as session:
    statement = select(Conta).where(Conta.id == id)
    conta = session.exec(statement).first()
    if conta.saldo > 0:
      raise ValueError("Esta conta ainda possui saldo!")
    conta.status = Status.INATIVO
    session.commit()

def transferir_saldo(id_conta_saida, id_conta_entrada, valor):
  with Session(engine) as session:
    statement = select(Conta).where(Conta.id == id_conta_saida)
    conta_saida = session.exec(statement).first()
    if conta_saida.saldo < valor:
      raise ValueError("Saldo insuficiente!")
    statement = select(Conta).where(Conta.id == id_conta_entrada)
    conta_entrada = session.exec(statement).first()

    conta_saida.saldo -= valor
    conta_entrada.saldo += valor

    session.commit()

def movimentar_dinheiro(historico: Historico):
  with Session(engine) as session:
    statement = select(Conta).where(Conta.id == historico.conta_id)
    conta = session.exec(statement).first() 

    if historico.tipo == Tipos.ENTRADA:
      conta.saldo += historico.valor
    else:
      if conta.saldo < historico.valor:
        raise ValueError("Saldo insuficiente!")
      conta.saldo -= historico.valor

      session.add(historico)
      session.commit()
      return historico
    
def total_contas():
  with Session(engine) as session:
    statement = select(Conta)
    contas = session.exec(statement).all()

  total = 0
  for conta in contas:
    print(f"{conta.banco} = {conta.saldo}")
    total += conta.saldo
  return float(total)

def buscar_historico_entre_datas(data_inicio: date, data_fim: date):
  with Session(engine) as session:
    statement = select(Historico).where(
      Historico.data >= data_inicio,
      Historico.data <= data_fim
    )
    results = session.exec(statement).all()
    return results

def criar_grafico_por_contas():
  with Session(engine) as session:
    statement = select(Conta).where(Conta.status == Status.ATIVO)
    contas = session.exec(statement).all()

    bancos = [i.banco.value for i in contas]
    total = [i.saldo for i in contas]

    plt.bar(bancos, total)
    plt.show()

    print(total)
    print(bancos)
