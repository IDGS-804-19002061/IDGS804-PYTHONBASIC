miDiccionario={"Matricula":123456, "Apellidos": "Cardiel"}

print(miDiccionario["Apellidos"])
miDiccionario["Materia"]="DWP"
miDiccionario["Matricula"]=98765
print(miDiccionario)
del miDiccionario["Apellidos"]
print(miDiccionario)