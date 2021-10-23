from Material import Material
from Distriburion_Center import Distribuition_Center

itens = []
itens.append(Material('123456', 'Cafe teste', 30000))
itens.append(Material('654321', 'Cafe inicial', 50000))

cd = Distribuition_Center('ne', itens, 5000, 6)

input()


