#Exercicio 3

#Cria uma função chamada soma que recebe dois números e retorna a soma deles.
#Depois, pede ao utilizador para inserir dois números e mostra o resultado.

def soma(x,y):        #Função
    return x + y

n1=int(input("Insira um número: "))
n2=int(input("Insira outro número: "))
print("A soma é ", soma(n1,n2))
