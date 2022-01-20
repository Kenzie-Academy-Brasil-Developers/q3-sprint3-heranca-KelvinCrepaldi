from .recipiente import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho:float, conteudo:float = 0, limpo:bool = True, bebida = None) -> None:
        super().__init__(tamanho, conteudo=conteudo, limpo=limpo)
        self.bebida = bebida
    
    def encher(self, bebida:str = "água"):
        if not self.limpo:
            return "Não se pode encher um copo sujo"
        self.limpo = False
        self.conteudo = self.tamanho
        self.bebida = bebida
        return None

    def beber(self, quantidade:float):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        elif quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        else:
            self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True

    def __str__(self) -> str:
        if self.conteudo == 0:
            return f"Um copo vazio de {self.tamanho}ml"
        else:
            return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"

    def __repr__(self) -> str:
        if self.conteudo == 0:
            return f"Um copo vazio de {self.tamanho}ml"
        else:
            return f"Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}"        