import datetime
import csv

def log(a):
    data = datetime.datetime.now()
    print(f"WARN: {data}: {a}") 


class FuncaoBanco:
    
    def __init__(self):
        pass  
    
    def lista_produto():
        with open('D:\Documentos\\engenharia_dados\\Engenharia_de_dados\\14_atividade\\modules\\dados\\produto.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            dados_produto = []
            for row in spamreader:
                dados_produto.append(row)
                    
        # apagando a primeira linha do cabeçalho        
        dados_produto.pop(0)
        return dados_produto
    
    def lista_funcionarios():        
        log("lendo dados funcionario")
        with open('D:\\Documentos\\engenharia_dados\\Engenharia_de_dados\\14_atividade\\modules\\dados\\funcionario.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            dados_funcionario = []
            for row in spamreader:
                dados_funcionario.append(row)                
        # apagando a primeira linha do cabeçalho        
        dados_funcionario.pop(0)
        return dados_funcionario
          
    def lista_cliente():        
        log("lendo dados cliente")
        with open('D:\\Documentos\\engenharia_dados\\Engenharia_de_dados\\14_atividade\\modules\\dados\\cliente.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            dados_cliente = []
            for row in spamreader:
                dados_cliente.append(row)
                    
        # apagando a primeira linha do cabeçalho        
        dados_cliente.pop(0)
        return dados_cliente
    
    def lista_vendas():        
        log("lendo dados venda")
        with open('D:\\Documentos\\engenharia_dados\\Engenharia_de_dados\\14_atividade\\modules\\dados\\venda.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            dados_venda = []
            for row in spamreader:
                dados_venda.append(row)
                
        # apagando a primeira linha do cabeçalho        
        dados_venda.pop(0)
        return dados_venda         
    