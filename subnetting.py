# Passo 1 - Receber input do utilizador
ip = input("Introduza o IP: ")
mascara = input("Introduza a máscara: ")

# Passo 2 - Separar os octetos
octetos_ip = ip.split(".")
octetos_mascara = mascara.split(".")

# Passo 3 - Converter para inteiro e fazer AND
rede_oct1 = int(octetos_ip[0]) & int(octetos_mascara[0])
rede_oct2 = int(octetos_ip[1]) & int(octetos_mascara[1])
rede_oct3 = int(octetos_ip[2]) & int(octetos_mascara[2])
rede_oct4 = int(octetos_ip[3]) & int(octetos_mascara[3])

# Passo 4 - Mostrar o resultado
print(f"Rede: {rede_oct1}.{rede_oct2}.{rede_oct3}.{rede_oct4}")