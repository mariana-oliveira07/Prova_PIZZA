class Pizza:
    def __init__(self, nome: str, tamanho: str):
        self.nome = nome
        self.tamanho = tamanho.upper()
        self.preco = 0.0

    def valor(self) -> float:
        if self.tamanho == 'P':
            self.preco = 30.0
        elif self.tamanho == 'M':
            self.preco = 40.0
        elif self.tamanho == 'G':
            self.preco = 55.0
        else:
            raise ValueError(f"Tamanho inválido: {self.tamanho}")
        return self.preco

    def detalhes(self):
        print(f'Pizza: {self.nome}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Valor base: ${self.valor():.2f}')