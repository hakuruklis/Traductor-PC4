import pprint, json
from openpyxl import Workbook
from openpyxl import load_workbook



wb = load_workbook(filename = 'Palabras.xlsx')
ws=wb.active
diccionario=[]
z=0
for z in range(181):
	palabra=ws['A'+str(z+1)].value
	nueva_palabra=palabra.split(". ")
	nueva_palabra[0]=nueva_palabra[0].split(" | ")
	nueva_palabra[1]=nueva_palabra[1].split("; ")
	x=0
	for x in range(len(nueva_palabra[0])):
	    if "/" in nueva_palabra[0][x]:
	        nueva_palabra[0][x]=nueva_palabra[0][x].split(" / ")
	x=0
	y=0
	s=0
	palabras = {}
	palabras['id']=z
	for x in range(len(nueva_palabra)):
	    if x==0:
	        for y in range(len(nueva_palabra[x])): 
	                if y==0:
	                	palabras['palabra#'] = nueva_palabra[x][y]
	                else:
	                	palabras['sininimo#'+ str(s+1)] = nueva_palabra[x][y]
	                	s+=1
	    elif x==1:
	        for y in range(len(nueva_palabra[x])): 
	                palabras['definicion#'+str(y+1)] = nueva_palabra[x][y]
	z+=1
	diccionario.append(palabras)

#pprint.pprint(diccionario)

#with open('palabras.json', 'w') as outfile:  
    json.dump(diccionario, outfile)










