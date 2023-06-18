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
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)