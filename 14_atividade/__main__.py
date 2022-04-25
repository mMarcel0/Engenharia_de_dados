
from modules.postgres import Conector_postgres
from modules.teste import FuncaoBanco, log

def conectando_bd():
    log("Conectando com o BD")
    banco = Conector_postgres (host="127.0.0.1", db="atividade_14",user="postgres",password="postgres")
    return banco


def inserir_produto(banco, dados_produto):
    log("Inserindo dados produto no banco")
    for dado in dados_produto:            
        banco.inserir(f"INSERT INTO produto (nome_produto, preço_produto, quantidade_estoque) VALUES('{dado[0]}',{dado[1]}, {dado[2]})")
        
        
def inserir_funcionario(banco, dados_funcionario):    
    log("Inserindo dados funcionario no banco")
    for dado in dados_funcionario:
        banco.inserir(f"INSERT INTO funcionario (nome_funcionario) VALUES('{dado[0]}')")
        
        
def inserir_cliente(banco, dados_cliente):
    log("Inserindo dados funcionario no banco")
    for dado in dados_cliente:
        banco.inserir(f"INSERT INTO cliente (nome_cliente) VALUES('{dado[0]}')")    
        
        
def inserir_vendas(banco, dados_venda):        
    log("Inserindo dados venda no banco")
    for dado in dados_venda:
        banco.inserir(f"INSERT INTO venda (id_cliente, id_funcionario, id_produto, quantidade_vendida) VALUES({dado[0]}, {dado[1]},{dado[2]}, {dado[3]})")    
    
        
def main():
    log("Iniciando o sistema")    
    try:
        dados_produto = FuncaoBanco.lista_produto()
        dados_funcionario = FuncaoBanco.lista_funcionarios()
        dados_cliente = FuncaoBanco.lista_cliente()
        dados_venda = FuncaoBanco.lista_vendas()
        
        banco = conectando_bd()
        inserir_produto(banco, dados_produto)
        inserir_funcionario(banco, dados_funcionario)
        inserir_cliente(banco, dados_cliente)
        inserir_vendas(banco, dados_venda)
        
        log('Finalizado com sucesso')    
    except Exception as e:
        print(str(e))


if __name__=="__main__":
    main()

   
 # pesquisar solid   
 # while True:
            
        #     print('''                  ------------------------------------------
        #           Digite 1 -  para inserir novos Produtos 
        #           Digite 2  - para insereri um funcionario 
        #           Digite 3  - para insereri um cliente  
        #           Digite 4  - para insereri uma nova venda
        #           Digite 0  - para sair
        #           -------------------------------------------''')            
                 
            # opcao= int(input("Digite a ação desejada "))
            # if opcao == 0:
            #     break
            # if opcao == 1:
            #     # minha idéia seira montar aqui a parte de orientação a objeto e conforme a opcao
            #     # selecionada iria chamar a classe correspondente  
            #     pass
            # if opcao == 2:
            #     # exemplo
            #     # inserir Funcionaro () -- chamaria a classe 
            #     # que iria pedir os inputs correspondentes e fazer a insercao no banco 
                
            #     pass
            # if opcao == 3:
            #     pass
            # if opcao == 4:
            #     pass
                    