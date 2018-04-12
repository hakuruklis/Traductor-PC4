import pprint, json
from openpyxl import Workbook
from openpyxl import load_workbook



palabra= "abgayala | abga. hacer a tiempo, enseguida, oportunamente, inmediatamente."
nueva_palabra=palabra.split(". ")
nueva_palabra[0]=nueva_palabra[0].split(" | ")
nueva_palabra[1]=nueva_palabra[1].split("; ")
x=0
for x in range(len(nueva_palabra[0])):
    if "/" in nueva_palabra[0][x]:
        nueva_palabra[0][x]=nueva_palabra[0][x].split(" / ")
print(nueva_palabra[0][0])
x=0
y=0
s=0
z=0
palabras = {}
palabras['id']=z
palabras['sininimos'] = []
for x in range(len(nueva_palabra)):
    if x==0:
        for y in range(len(nueva_palabra[x])): 
                if y==0:
                	if type(nueva_palabra[x][y]) is list:
                		palabras['palabra'] = nueva_palabra[x][y][0]
                		palabras['sininimos'].insert(len(palabras['sininimos']),nueva_palabra[x][y])
                	else:
                		palabras['palabra'] = nueva_palabra[x][y]
                	if type(nueva_palabra[x][y]) is list:
                		for s in range(len(nueva_palabra[x][y])):
                			palabras['sininimos'].insert(len(palabras['sininimos']),nueva_palabra[x][y][s])
                			s+=1
                else:
                	if type(nueva_palabra[x][y]) is list:
                		for s in range(len(nueva_palabra[x][y])):
                			palabras['sininimos'].insert(len(palabras['sininimos']),nueva_palabra[x][y][s])
                			s+=1               	
    elif x==1:
        for y in range(len(nueva_palabra[x])): 
                palabras['definicion#'+str(y+1)] = str(nueva_palabra[x][y])
z+=1
print(palabras)


#pprint.pprint(diccionario)
#with open('palabras.json', 'w') as outfile:  
#json.dump(diccionario, outfile)