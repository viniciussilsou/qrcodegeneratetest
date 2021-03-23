import pyqrcode
from pyqrcode import QRCode


print("Digite texto:\n")

texto = input(": ")

print("Digite o nome da imagem:\n")

imagem = input(": ")
d = imagem+".png"

url = pyqrcode.create(texto)

url.show()
url.png(d, scale =6)