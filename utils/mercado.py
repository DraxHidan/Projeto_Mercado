from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:

    print("="*30)
    print("="*8, "Bem-Vindo(a)", "="*8)
    print("="*6, "Mercado Campeão", "="*7)

    print("Selecione a opção abaixo:")
    print("1- Cadastrar Produto")
    print("2- Listar Produto")
    print("3- Comprar Produto")
    print("4- Visualizar Carrinho")
    print("5- Fechar Pedido")
    print("6- Sair do sistema")

    opcao = int(input("Digite:"))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Volte Sempre!")
        sleep(2)
        exit()
    else:
        print("Opção inválida")
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('='*19)
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    produto = Produto(nome, preco)
    produtos.append(produto)
    print(f'O produto {nome} foi cadastrado com sucesso')
    sleep(1)
    menu()


def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('='*20)
        for produto in produtos:
            print(produto)
            print('-'*20)
            sleep(1)
    else:
        print('Ainda nao existem produtos cadastrados')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar no carrinho: ')
        print('-'*15)
        print('='*9, 'Produtos Disponíveis', '='*9)
        for produto in produtos:
            print(produto)
            print('-'*15)
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado no carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender.')
        sleep(2)
        menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-'*15)
                sleep(1)
        menu()

    else:
        print('Ainda não existem produtos no carrinho')
        sleep(2)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-'*20)
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(3)
        exit()
    else:
        print('Ainda não existem produtos no carrinho')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p
    sleep(2)
    menu()


if __name__ == '__main__':
    main()

