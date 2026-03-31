from veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__ (self, marca: str, modelo: str, ano_fabricacao: int, capacidade_carga_toneladas: int):
        super().__init__(marca, modelo, ano_fabricacao)
        self.capacidade_carga_toneladas = capacidade_carga_toneladas

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano_fabricacao}, Capacidade Toneldas {self.capacidade_carga_toneladas}")
