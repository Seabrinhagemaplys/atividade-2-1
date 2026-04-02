from caminhao import Caminhao
from moto import Moto
from carro import Carro

caminhao1 = Caminhao("Peugeot", "MD4", 2024, 30)
moto1 = Moto("Mitsubishi", "FZ25", 2010, 10)
carro1 = Carro("Fiat", "Mobi", 2022, 4)

caminhao1.exibir_info()
moto1.exibir_info()
carro1.exibir_info()