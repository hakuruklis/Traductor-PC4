import json, pprint, requests
json_data=open("palabras.json").read()
data = json.loads(json_data)



def buscar_palabra(palabra):
	#json_data=open("palabras.json").read()
#	data = json.loads(json_data)
	response = requests.request("GET", "http://127.0.0.1:5000/diccionarioguna/api/v1.0/palabras")
	data = json.loads(response.text)
	x=0
	respuesta=""
	sinonimos=[]
	definicones=[]
	#palabra= input("Inserta una palbra para buscarla: ")
	for x in range(len(data)):
		if data[x]['palabra'] == palabra:
			if len(data[x]['sinonimos']) > 0:
				y=0
				for y in range(len(data[x]['sinonimos'])):
					sinonimos = data[x]['sinonimos']
			y=0
			for y in range(len(data[x]['definicion'])):
				definicones = data[x]['definicion']
		x+=1
	if len(sinonimos) > 0:
		print('Sinonimos: ')
		for y in sinonimos:
			print('- '+y)
		print('\n')
	print('Definicones: ')
	for y in definicones:
		print('- '+y)

		

palabra = "wardummad"	
print (buscar_palabra(palabra))

