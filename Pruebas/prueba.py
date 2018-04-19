import pprint, json
from openpyxl import Workbook
from openpyxl import load_workbook



palabra= "arbag | arbagge | arbaggegwa. a escondidas, a espaldas, a hurtadillas."
nueva_palabra=palabra.split(". ")
nueva_palabra[0]=nueva_palabra[0].split(" | ")
nueva_palabra[1]=nueva_palabra[1].split(", ")
x=0

print(nueva_palabra[0][0])
x=0
y=0
s=0
z=0
palabras = {}
palabras['id']=z
palabras['palabra']=''
palabras['sininimos'] = []
palabras['definicion']=[]

for x in range(len(nueva_palabra)):
	if x == 0: 
		for y in range(len(nueva_palabra[0])):
			if y == 0:
				palabras['palabra']=nueva_palabra[0][0]
			else:
				palabras['sininimos'].append(nueva_palabra[0][y])
			y+=1
	elif x==1:
		y=0
		for y in range(len(nueva_palabra[1])):
				print(nueva_palabra[1][y])
				palabras['definicion'].append(nueva_palabra[1][y])



print(palabras)

#for x in range(len(nueva_palabra)):
#    if x==0:
#        if len(nueva_palabra[x])              	
#    elif x==1:
#        for y in range(len(nueva_palabra[x])): 
#                palabras['definicion#'+str(y+1)] = str(nueva_palabra[x][y])
#z+=1
#print(palabras)


#pprint.pprint(diccionario)
#with open('palabras.json', 'w') as outfile:  
#json.dump(diccionario, outfile)