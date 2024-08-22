from .pizza import Pizza

class PizzaEspecial(Pizza):
    SABORES = {
        '1': 'Pizza de Calabresa',
        '2': 'Pizza de Frango com Catupiry',
        '3': 'Pizza Moda da Casa',
        '4': 'Pizza de Atum'
    }

    ADICIONAIS = {
        '1': 'Cheddar',
        '2': 'Bacon'
    }
    
    PRECO_ADICIONAL = 5.0

    def __init__(self, nome: str, tamanho: str, adicionais: list):
        super().__init__(nome, tamanho)
        self.adicionais = adicionais

    def valor(self) -> float:
        valor_base = super().valor()
        valor_total = valor_base + (len(self.adicionais) * self.PRECO_ADICIONAL)
        return valor_total

    def detalhes(self):
        sabor = self.SABORES.get(self.nome, 'Sabor não encontrado')
        print(f'Pizza: {sabor}')
        
        if self.adicionais:
            for adicional in self.adicionais:
                descricao_adicional = self.ADICIONAIS.get(adicional, 'Nenhum adicional')
                if descricao_adicional != 'Nenhum adicional':
                    print(f'Adicional de {descricao_adicional} ${self.PRECO_ADICIONAL}')
        else:
            print('Nenhum adicional')
        
        print(f'Tamanho: {self.tamanho}')
        print(f'Valor total: ${self.valor()}')