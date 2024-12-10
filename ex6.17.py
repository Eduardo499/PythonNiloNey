estoque={ "tomate": [ 1000, 2.30],
"alface": [ 500, 0.45],
"batata": [ 2001, 1.20],
"feijão": [ 100, 1.50] }

venda = []

while True:
    produto = str(input('Digite o nome do produto (fim para sair): ')).lower()
    
    if produto == 'fim':
        break
    if produto in estoque:
        quantidade = int(input('Digite a quantidade do produto: '))
        if quantidade <= estoque[produto][0]:
            venda.append([produto, quantidade])
        else:
            print('Essa quantidade não está disponível.')
    else:
        print('Digite um produto válido.')

total = 0

print("Vendas:\n")

for operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
(produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo

print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")

for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])