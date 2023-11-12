#Programa Notas Escolar

def promedio_notas(nombre, promedio_nota): 
    for i in range(5): 
        nota=[]
        temp1 = input("Ingrese el nombre del estudiante: \n")
        nombre.append(temp1)
        for j in range(3):
            materias = ["Matematicas", "Ciencias", "Historia"]
            nota.append(float(input(f"Ingrese la nota {materias[j]} del estudiante: \n")))
        promedio = sum(nota) / len(nota)
        promedio_nota.append(promedio)

nombre1 = []
promedio_nota1 = []
promedio_notas(nombre1, promedio_nota1)
promedio_maximo = max(promedio_nota1)
promedio_minimo = min(promedio_nota1)

# Imprimir resultados
print("Resultados:")
for Estudiante in range(5):
    print(f"Estudiante: {nombre1[Estudiante]}, Promedio: {promedio_nota1[Estudiante]:.2f}")

print(f'El promedio más alto es: {promedio_maximo:.2f}')
print(f'El promedio más bajo es: {promedio_minimo:.2f}')