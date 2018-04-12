import json, pprint
json_data=open("palabras.json").read()
data = json.loads(json_data)


def buscar_palabra(palabra):
	json_data=open("palabras.json").read()
	data = json.loads(json_data)
	x=0
	respuesta=""
	#palabra= input("Inserta una palbra para buscarla: ")
	for x in range(len(data)):
		for key, value in data[x].items():
			if value == palabra:
				y=0
				for key, value in data[x].items():
					if "definicion" in key:
						respuesta = respuesta + value
						print("Definiciones:\n" + respuesta)
			#elif type(value) is list:
				
		x+=1

		

palabra = "abbalalla"	
print (buscar_palabra(palabra))

