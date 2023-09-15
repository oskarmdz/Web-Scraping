import requests, bs4, sys, ipcalc
from bs4 import BeautifulSoup

def generar_diccionario(bloques_de_red):
	print("Generando diccionario...")
	with open("ips.txt","a+") as f:
		for bloque_de_red in bloques_de_red:
			for ip in ipcalc.Network(bloque_de_red):
				f.write(str(ip)+"\n")
	print("DICCIONARIO GENERADO CON EXITO")

def obtener_bloques_de_red(country):
	r = requests.get(country)
	data = BeautifulSoup(r.text,"html.parser")
	with open("tmp.txt","w+") as f:
		f.write(str(data))
	print(f"\nBLOQUES DE RED DE {country} OBTENIDOS CON EXITO")
	bloques_de_red = []
	with open("tmp.txt","r+") as f:
		for bloque_de_red in f.read().splitlines():
			bloques_de_red.append(bloque_de_red)
	generar_diccionario(bloques_de_red)

def main():
	print("""
		Instrucciones de uso:

		Selecciona el país del cual quieres generar un
		diccionario que contenga todas las direcciones IP del mismo.
		Puedes consultar todos los paises disponible en: 
		https://www.ipdeny.com/ipblocks/data/aggregated

		Ejemplo de uso:
		Selecciona un país => https://www.ipdeny.com/ipblocks/data/aggregated/ad-aggregated.zone

		Nota: Es recomendable que no haya ningún archivo de texto
		en la carpeta donde se ejecute el script.

		""")
	country = input("Selecciona un país => ")
	obtener_bloques_de_red(country)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()