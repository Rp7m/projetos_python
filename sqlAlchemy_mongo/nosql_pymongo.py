import pymongo as bdM

client = bdM.MongoClient("Coloque seu link de conexao com mongodb contendo sua senha e login")
db = client.banco
collection = db.banco_collection

post1 = {
    "cliente": "Fulano",
    "cpf": "123456987",
    "endereco": "Av.Eduard Mont n°10",
    "conta_tipo": "Corrente",
    "agencia": "0001",
    "conta_numero": 123456964,
    "saldo": 800.21,
    "tags": ["mongodb","cliente"]
}

post = db.posts
post_id = post.insert_one(post1).inserted_id

print(post_id)
print(db.posts.find_one())

posts = [
    {
        "cliente": "Fulano Belt",
        "cpf": "123453989",
        "endereco": "Av.Eduard Mont n°10",
        "conta_tipo": "Corrente",
        "agencia": "0001",
        "conta_numero": 123456364,
        "saldo": 1000.21,
        "tags": ["mongodb","cliente"]
    },
    {
        "cliente": "Rob Dev",
        "cpf": "123456582",
        "endereco": "Av.Eduard Mont n°10",
        "conta_tipo": "Corrente",
        "agencia": "0001",
        "conta_numero": 123456764,
        "saldo": 900.21,
        "tags": ["mongodb","cliente"]
    }

]

dados = post.insert_many(posts)
#dados.inserted_ids
print(dados.inserted_ids)
print(db.posts.find_one({"cliente":"Fulano Belt"}))

for post in post.find():
    print(post)