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
print(len(nueva_palabra[0]))
x=0
y=0
s=0
z=0
palabras = {}
palabras['id']=z
palabras['sininimos'] = []
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