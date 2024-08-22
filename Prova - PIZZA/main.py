from models.pizza_especial import PizzaEspecial
from utils.input_utils import obter_sabor, obter_adicionais, obter_tamanho

def main():
    numero_pedido = 123
    pizzas = []

    while True:

        nome = obter_sabor()
        adicionais = obter_adicionais()
        tamanho = obter_tamanho()

        pizza = PizzaEspecial(nome, tamanho, adicionais)

        pizzas.append(pizza)

        adicionar_mais = input('Deseja adicionar mais pizzas ao pedido? (s/n): ').lower()
        if adicionar_mais != 's':
            break

    print(f'\nNúmero do Pedido: {numero_pedido}')
    for i, pizza in enumerate(pizzas, 1):
        print(f'\nPizza {i}:')
        pizza.detalhes()

if __name__ == "__main__":
    main()
