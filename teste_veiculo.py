from veiculo import veiculo

minhalenda = veiculo('Chrysler', 'PT Cruiser', 'Prata', 0)

# Exibindo a minha caranga
print('\n\t\t\t -- Minha Lenda -- \n')
print(minhalenda)

# Acelerando minha caranga
for i in range(1, 201):
 minhalenda.acelerar()

# acelerada
print('\n\t\t\t -- Minha Lenda Acelerada -- \n')
print(minhalenda)

# Freia
for i in range(1, 201):
 minhalenda.freia()

print('\n\t\t\t -- Minha Lenda Freia -- \n')
print(minhalenda)
