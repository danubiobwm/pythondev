from sqlalchemy import create_engine, Column, Integer, String, Float # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from   sqlalchemy.orm  import sessionmaker # type: ignore

enginer = create_engine('sqlite:///banco.db', echo=True)
Base = declarative_base()

class Filme(Base):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(enginer)


#insereção de dados
def adicionar_filme(nome: str, ano: int, nota: float):
    Session = sessionmaker(bind=enginer)
    session = Session()
    novo_filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(novo_filme)
    session.commit()
    session.close()

# adicionar_filme('O Senhor dos Anéis: A Sociedade do Anel', 2001, 8.8)
# adicionar_filme('O Senhor dos Anéis: As Duas Torres', 2002, 8.7)
# adicionar_filme('O Senhor dos Anéis: O Retorno do Rei', 2003, 8.9)
# adicionar_filme('Harry Potter e a Pedra Filosofal', 2001, 7.6)
# adicionar_filme('Harry Potter e a Câmara Secreta', 2002, 7.4)
# adicionar_filme('Harry Potter e o Prisioneiro de Azkaban', 2004, 7.8)
# adicionar_filme('Harry Potter e o Cálice de Fogo', 2005, 7.7)


def atualizar_filme(id: int, nome: str, ano: int, nota: float):
    Session = sessionmaker(bind=enginer)
    session = Session()
    filme = session.query(Filme).filter(Filme.id == id).first()
    if filme:
        filme.nome = nome
        filme.ano = ano
        filme.nota = nota
        session.commit()
    session.close()


#atualizar_filme(1, 'O Senhor dos Anéis: A Sociedade do Anel x', 2001, 9.0)


def deletar_filme(id: int):
    Session = sessionmaker(bind=enginer)
    session = Session()
    filme = session.query(Filme).filter(Filme.id == id).first()
    if filme:
        session.delete(filme)
        session.commit()
    session.close()

#deletar_filme(1)


def listar_filmes():
    Session = sessionmaker(bind=enginer)
    session = Session()
    filmes = session.query(Filme).all()
    for filme in filmes:
        print(f'ID: {filme.id}, Nome: {filme.nome}, Ano: {filme.ano}, Nota: {filme.nota}')
    session.close()

listar_filmes()

