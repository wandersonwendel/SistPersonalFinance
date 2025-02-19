# Biblioteca para criar modelos de banco de dados e de definir campos
from sqlmodel import SQLModel, Field, create_engine, Relationship
from datetime import date
# Criar enumeradores(valores pré-definidos)
from enum import Enum

class Bancos(Enum):
  NUBANK = 'Nubank'
  SANTANDER = 'Santander'
  INTER = 'Inter'

class Status(Enum):
  ATIVO = 'Ativo'
  INATIVO = 'Inativo'

class Tipos(Enum):
  ENTRADA = 'Entrada'
  SAIDA = 'Saida'

# Herda de SQLModel e representa uma tabela no banco
class Conta(SQLModel, table=True):
  id: int = Field(primary_key=True)
  saldo: float
  banco: Bancos = Field(default=Bancos.NUBANK)
  status: Status = Field(default=Status.ATIVO)

class Historico(SQLModel, table=True):
  id: int = Field(primary_key=True)
  conta_id: int = Field(foreign_key='conta.id') # Relação com a classe Conta
  conta: Conta = Relationship()
  tipo: Tipos = Field(default=Tipos.ENTRADA)
  valor: float
  data: date

# Configurando o banco de dados
sqlite_file_name = 'database.db'
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Conexão com o banco
engine = create_engine(sqlite_url)


if __name__ == "__main__":
  SQLModel.metadata.create_all(engine)


