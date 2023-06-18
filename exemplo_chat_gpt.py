import pymongo

def conectar():
    # Substitua <SUA_STRING_DE_CONEXAO> pela sua própria string de conexão do MongoDB Atlas
    client = pymongo.MongoClient("mongodb+srv://<user>:<password>@cluster1.os5a8p6.mongodb.net/?retryWrites=true&w=majority")
    
    # Retorna a instância do cliente MongoDB
    return client

def inserir_dado():
    # Conecte-se ao MongoDB Atlas
    client = conectar()
    
    # Acesse o banco de dados desejado
    db = client['seu_banco_de_dados']
    
    # Acesse a coleção desejada
    colecao = db['sua_colecao']
    
    # Crie um documento para ser inserido na coleção
    dado = {
        "chave": "1",
        "outra_chave": "2"
    }
    
    # Insira o documento na coleção
    resultado = colecao.insert_one(dado)
    
    # Imprima o ID do documento inserido
    print("ID do documento inserido:", resultado.inserted_id)

inserir_dado()
