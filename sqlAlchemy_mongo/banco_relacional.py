from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine("sqlite://")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer,ForeignKey('cliente.id'),nullable=False)
    cliente = relationship('Cliente', back_populates="conta")
    saldo = Column(Float)


    def __repr__(self):
        return f'Conta {self.tipo},\n' \
               f'AG: {self.agencia},\n' \
               f'Num: {self.num},\n' \
               f'Saldo: {self.saldo}'


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer,primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(9))
    conta = relationship(Conta, back_populates="cliente")

    def __repr__(self):
        return f'Cliente {self.nome},\n' \
               f'CPF:{self.cpf},\n' \
               f'Endereço:{self.endereco},\n' \
               f'Conta {self.conta}'



Base.metadata.create_all(engine)

belt1 = Cliente(
    nome = 'Belt1',
    cpf = '123456789',
    endereco = 'Av.Cont'
)
belt1_conta = Conta(
    tipo = 'Corrente',
    agencia = '0001',
    num = 123456987,
    saldo = 800.21,
    cliente = belt1
)

belt2 = Cliente(
    nome = 'Belt2',
    cpf = '123456987',
    endereco = 'Av.Vont'
)
belt1_conta = Conta(
    tipo = 'Corrente',
    agencia = '0001',
    num = 123456964,
    saldo = 800.21,
    cliente = belt2
)

session. add_all([belt1_conta, belt1,belt2,belt1_conta])
session.commit()

#query = session.query(Cliente).filter_by(nome='Belt')

print(f'{belt1} \n \n{belt2}')
