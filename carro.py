from veiculo import Veiculo

class Carro(Veiculo):
    numeros_de_porta_aceitavel = [1, 2, 3, 4]
    
    def __init__(self, marca: str, modelo: str, ano_fabricacao: int, numero_portas: int ):
        
        try:
            super().__init__(marca, modelo, ano_fabricacao)
        except Exception as e:
            raise e
    
        if numero_portas not in self.numeros_de_porta_aceitavel:
            raise ValueError("Número de portas inaceitável")

        self.numero_portas = numero_portas

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano_fabricacao}, N de portas: {self.numero_portas}")



