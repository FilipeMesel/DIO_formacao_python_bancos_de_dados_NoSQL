#Importando o pymongo

import pymongo as pyM

#Connectando ao cluster do mongoDB Atlas
#user -> Nickname do administrador
#password -> Senha de acesso ao administrador
client = pyM.MongoClient("mongodb+srv://<user>:<password>@cluster1.os5a8p6.mongodb.net/?retryWrites=true&w=majority")

#Vamos definir "test" como banco de dados
db = client.test

#Verificando se há uma coleção (Coleções são tabelas de bancos de dados não relacionais)
collection = db.test_collection
print(db.list_collection_names())