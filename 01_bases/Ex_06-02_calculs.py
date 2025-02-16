a = int(input('Entrez le nombre a:'))
b = int(input('Entrez le nombre b:'))
puissance_string = str(a**b)
print(f"a + b = {a+b}\na * b = {a*b} \nL'élévation de a à la puissance b est {a**b}")
#Correction
print(f"L'élévation de a à la puissance b est {puissance_string[:3]}...{puissance_string[-3:]}.")
print(f"Ce nombre s'écrit avec {len(puissance_string)} chiffres et contient {puissance_string.count('1')} fois le chiffre 1.")
