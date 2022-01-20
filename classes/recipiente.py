# Desenvolva sua classe Recipiente aqui.

class Recipiente: 
    def __init__(self, tamanho:float, conteudo:float = 0, limpo:bool = True) -> None:
        if tamanho < 0:
            tamanho = 0
        self.tamanho = float(tamanho)
        self.conteudo = float(conteudo)
        self.limpo = limpo
    
    def esvaziar(self):
        self.conteudo = 0
    
    def esta_vazio(self) -> bool:
        return self.conteudo == 0

    def lavar(self) -> None:
        self.esvaziar()
        self.limpo = True

    def esta_limpo(self) -> bool:
        return self.limpo == True

    def estado(self) -> str:
        if self.limpo == True:
            return "limpo"
        else:
            return "sujo"
    
    def sujar(self) -> None:
        self.limpo = False

    def __str__(self) -> str:
        status = self.estado();
        return f"Um recipiente {status} não especificado"

    def __repr__(self) -> str:
        status = self.estado();
        return f"Um recipiente {status} não especificado"