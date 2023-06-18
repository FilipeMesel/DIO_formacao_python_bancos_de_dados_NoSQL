#Importando o pymongo

import pymongo as pyM
import datetime

#Connectando ao cluster do mongoDB Atlas
#user -> Nickname do administrador
#password -> Senha de acesso ao administrador
client = pyM.MongoClient("mongodb+srv://<user>:<password>@cluster1.os5a8p6.mongodb.net/?retryWrites=true&w=majority")

#Vamos definir "test" como banco de dados
db = client.test

#Verificando se há uma coleção (Coleções são tabelas de bancos de dados não relacionais)
collection = db.test_collection
print(db.list_collection_names())

#Criando um POST para subir documentos ao banco de dados
#Tags são maneiras de encontrar o post ao realizar uma consulta.
#Importante definir tags
post = {
    "author": "Mike",
    "text": "My first mongoDB application based on Python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

#Preparando para submeter as informações
#Criando uma coleção chamada "posts"
posts = db.posts
#Inserindo/ submetendo o post a coleção posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

#Recuperando as coleções
print("Coleções: ", db.list_collection_names())

#Recuperando informações presentes na coleção "posts"
print("Infos: ", db.posts.find_one())

#bulk inserts: Dois documentos em um mesmo post
new_posts = [
    {
        "author": "Mike",
        "text": "Another post",
        "tags": ["bulk", "post", "insert"],
        "date": datetime.datetime.utcnow()
    },
    {
        "author": "Joao",
        "text": "New post",
        "title": "mongo is fun!",
        "date": datetime.datetime.utcnow()
    }
]

#Submetendo vários posts
result = posts.insert_many(new_posts)
print(result.inserted_ids)

#Recuperando informações presentes na coleção "posts" com especificações
print("New Infos: ", db.posts.find_one({"author": "Joao"}))

#Recuperando todas as informações da coleção "posts"
print("Documentos presentes na coleção posts: ")
for post in posts.find():
    print(post)

#Contando a quantidade de documentos
print("Quantidade de documentos presentes: ", posts.count_documents({}))
print("Quantidade de documentos presentes cujo autor é Mike: ", posts.count_documents({"author": "Mike"}))
print("Quantidade de documentos presentes com a tag python3: ", posts.count_documents({"tags": "python3"}))
print("Infos cuja tag é python3: ", db.posts.find_one({"tags": "python3"}))

#Recuperando múltiplos documentos de forma ordenada
print("Recuperando infos pela data de maneira ordenada do mais antigo ao mais novo: ")
for post in posts.find({}).sort("date"):
    print(post)

#Criando múltiplos documentos pelo índice de forma ascendente na nova coleção "profiles"
result = db.profiles.create_index([('author', pyM.ASCENDING)], unique = True)
print(sorted(list(db.profiles.index_information())))

#Inserido vários documentos de uma só vez em "profile_user":
user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Joao'}
]
result = db.profile_user.insert_many(user_profile_user)

#Printando novamente as coleções
collections = db.list_collection_names()
for collection in collections:
    print(collection)

#Removendo dados na coleção "posts"
db["posts"].drop()

#Outra forma de deletar os dados:
db["profiles"].drop()

#Printando novamente as coleções
collections = db.list_collection_names()
for collection in collections:
    print(collection)

#Deletando o banco de dados:
client.drop_database("test")
print("Não vai conseguir fazer o que vem abaixo: ")
print(db.list_collection_names())