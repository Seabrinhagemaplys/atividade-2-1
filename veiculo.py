from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca: str, modelo: str, ano_fabricacao: int):
        if ano_fabricacao not in range(1960, 2027):
            raise ValueError("Ano Inválido")
        self.ano_fabricacao = ano_fabricacao   
        
        if not modelo.strip():
            raise TypeError("Modelo Vazia")   
        self.modelo = modelo
        
        self.marca = marca
        
    @abstractmethod
    def exibir_info(self):
        pass