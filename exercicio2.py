from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///clientes.db")
Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    cidade = Column(String)


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
with Session() as session:
    session.add_all(
        [
            Cliente(id_cliente=6767, nome="samuel", cidade="Ribeirao"),
            Cliente(id_cliente=4242, nome="kaio", cidade="inferno"),
            Cliente(id_cliente=6969, nome="pedrin", cidade="uganda"),
        ]
    )
    session.commit()

    clientes = session.query(
        Cliente.id_cliente, Cliente.nome, Cliente.cidade
    ).all()
    print(clientes)