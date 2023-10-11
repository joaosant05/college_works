# Tabela de itens
table = [
    [1, 'Calça',  20, 112.00],
    [2, 'Camisa', 18, 95.00],
    [3, 'Bermuda', 23, 49.90],
    [4, 'Saia', 12, 169.00],
    [5, 'Blusa', 9, 120.00],
    [6, 'Moletom', 4, 135.00],
    [7, 'Meia', 17, 12.99],
    [8, 'Tênis', 8, 183.00],
    [9, 'Bota', 3, 219.90]
]

# Funções do programa
itens = []

def selec_codigo():
    global itens
    itens = []
    while True:
        try:
            global code
            code = int(input('Digite um código de produto: '))
            if code < 1 or code > 9:
                print('Digite um dos códigos disponíveis.')
            else:
                itens.append(code)
                x = input('Deseja comprar mais algum item? (s/n) ').lower()
                if x != 's':
                    break
        except ValueError:
            print('Digite um código válido.')

# Gerar pedido
clientes = {}

def cadastro_compra():
    nome = input('\nInforme o nome do cliente: ')
    if nome not in clientes:
        clientes[nome] = []

    selec_codigo()

    total_soma = 0

    for code in itens:
        found = False

        while not found:
            quantidade = int(input(f'\nQuantas unidades do código {code} deseja comprar? '))
            for item in table:
                if item[0] == code:
                    if quantidade <= item[2]:
                        item[2] -= quantidade
                        clientes[nome].append((code, quantidade))
                        valor_item = item[3]
                        total_item = valor_item * quantidade
                        total_soma += total_item
                        found = True
                    else:
                        print('Quantidade não disponível em estoque. Estoque atual:', item[2])

    print(f'\n{nome}, o valor do seu pedido deu R${total_soma:.2f}')

# Lista de vendas
def vendas_realizadas():
    print("\nVendas Realizadas:")
    for cliente, vendas in clientes.items():
        print(f"Cliente: {cliente}")
        for code, quantidade in vendas:
            for item in table:
                if item[0] == code:
                    valor_unitario = item[3]
                    total_produto = valor_unitario * quantidade
                    print(f"   Produto: {item[1]}, Quantidade: {quantidade}, Valor Unitário: R${valor_unitario:.2f}, Total: R${total_produto:.2f}")
# Maior venda
def maior_venda_registrada():
    maior_venda = 0
    cliente_maior_venda = ""

    for cliente, vendas in clientes.items():
        total_venda_cliente = 0
        for code, quantidade in vendas:
            for item in table:
                if item[0] == code:
                    valor_unitario = item[3]
                    total_produto = valor_unitario * quantidade
                    total_venda_cliente += total_produto

        if total_venda_cliente > maior_venda:
            maior_venda = total_venda_cliente
            cliente_maior_venda = cliente

    if cliente_maior_venda:
        print(f"A maior venda registrada foi de {cliente_maior_venda} no valor de R${maior_venda:.2f}")
    else:
        print("Nenhuma venda registrada no sistema.")

# Mostrar estoque
def estoque():
    print("\nEstoque:")
    print("Código | Item       | Estoque")
    for item in table:
        print(f"{item[0]:<6} | {item[1]:<10} | {item[2]:<7}")

# Repor estoque
def repor_estoque():
    while True:
        try:
            code = int(input('Digite o código do item que você deseja repor: '))
            rep = int(input('Informe a quantidade que você quer repor: '))
            found = False

            for item in table:
                if item[0] == code:
                    item[2] += rep
                    found = True
                    break

            if not found:
                print('Código não encontrado na tabela.')

            print('\nQuantidade em estoque foi atualizada!')
            x = input('Deseja repor mais algum item? (s/n) ').lower()
            if x != 's':
                break
        except ValueError:
            print('Digite um código e quantidade válidos.')

# Função do menu
def lobby():
  global menu
  menu = int(input('\nInsira o número da opção desejada '))
  while menu > 5 or menu == '' :
    menu = int(input('Insira uma opção válida ou (sair) para sair do sistema '))
    if menu == 'sair':
      break

# Menu do software
while True:
  print('\nOlá, seja bem vindo!')
  print('\nOpção 1: Registrar Venda')
  print('Opção 2: Mostrar estoque')
  print('Opção 3: Repor estoque')
  print('Opção 4: Mostrar vendas realizadas')
  print('Opção 5: Maior venda')

  lobby()
  match menu:
    case 1:
      for item in table:
        print(f"{item[0]:<6} | {item[1]:<10} | {item[2]:<7} | R${item[3]:.2f}")
      cadastro_compra()
      x = input('\nVoltar para o menu? (s/n) ')
      if x == 's':
        continue
      elif x == 'n':
        break
    case 2:
      estoque()
      x = input('\nVoltar para o menu? (s/n) ')
      if x == 's':
        continue
      elif x == 'n':
        break
    case 3:
      estoque()
      repor_estoque()
      x = input('\nVoltar para o menu? (s/n) ')
      if x == 's':
        continue
      elif x == 'n':
        break
    case 4:
      vendas_realizadas()
      x = input('\nVoltar para o menu? (s/n) ')
      if x == 's':
        continue
      elif x == 'n':
        break
    case 5:
      maior_venda_registrada()
      x = input('\nVoltar para o menu? (s/n) ')
      if x == 's':
          continue
      elif x == 'n':
          break