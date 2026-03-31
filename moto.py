from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano_fabricacao: int, cilindradas: int):
        super().init(marca, modelo, ano_fabricacao)
        
        if cilindradas < 0:
               raise ValueError("Numero Invalido")
        self.cilindradas = cilindradas
    
    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano_fabricacao}, Cilindradas: {self.cilindradas}")