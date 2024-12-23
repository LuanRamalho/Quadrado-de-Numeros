# Solicita o tamanho do quadrado
tamanho = int(input("Digite o tamanho do quadrado: "))

# Exibe o quadrado de números
for i in range(tamanho):
    for j in range(tamanho):
        print(j + 1, end=" ")
    print()  # Quebra de linha após cada linha do quadrado
input()