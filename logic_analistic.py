import random

def ayuda():
    var0 = "Ahorrar agua para evitar su desperdicio."
    var1 = "Reciclar los residuos para cuidar el planeta."
    var2 = "Reducir el uso de bolsas y botellas de plástico."
    var3 = "Apagar las luces cuando no sean necesarias."
    var4 = "Plantar árboles para mejorar la calidad del aire."
    var5 = "No tirar basura en las calles ni en los ríos."
    var6 = "Utilizar bicicleta o caminar para reducir la contaminación."
    var7 = "Cuidar los animales y proteger sus hábitats naturales."
    
    op = random.randint(1, 8)

    if op == 1:
        return var0

    if op == 2:
        return var1

    if op == 3:
        return var2
    
    if op == 4:
        return var3
    
    if op == 5:
        return var4
    
    if op == 6:
        return var5
    
    if op == 7:
        return var6
    
    if op == 8:
        return var7
    
print(ayuda())