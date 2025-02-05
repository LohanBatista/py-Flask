pip3 ou pip -r indica um arquivo
pip3 ou pip install Flask==2.3.0 indica uma lib

flask shell =
db.drop_all() = irá limpar todas as tabelas e cria do zero
db.create_all() = irá criar todos os models em tabelas
db.session.commit() = comando para efetivar as mudanças do banco
exit() = sair

os mesmo comando do código posso usar no flask shell
ex:
user = User(username="admin", password="admin")
db.session.add(user)
db.session.commit()
