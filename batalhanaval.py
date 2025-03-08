from random import randint

tabela = []

for x in range(4):
    tabela.append(["O"] * 4)

def print_tabela(tabela):
    for linha in tabela:
      print (" ".join(linha))
      
      
print_tabela(tabela)

def random_tabela(tabela):
    return randint(0, len(tabela) - 1)

def random_coluna(tabela):
    return randint(0, len(tabela[0]) - 1)

navio_linha = random_tabela(tabela)
navio_coluna = random_coluna(tabela)


for turn in range(4):
    linha = int(input("Escolha uma linha:"))
    coluna = int(input("Escolha uma coluna:"))

    if linha == navio_linha and coluna == navio_coluna:
        print ("Parabéns! Você acertou meu navio!")
        break
    else:
        if (linha < 0 or linha > 3) or (coluna < 0 or coluna > 3):
            print ("Isso não está nem perto do mar!")
        elif(tabela[linha][coluna] == "X"):
            print ("Você já falou isso.")
        else:
            print ("Você errou minha nave.")
            tabela[linha][coluna] = "X"
        print (turn + 1)
        print_tabela(tabela)
        if turn>4:
            print ("Game overr")
print ("O navio está em", linha)
print (coluna) 
