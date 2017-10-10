import turtle
import random

pen = turtle.Pen()

#Definindo uma função para gerar cores

def gerando_cores():
    colors = ['red','green','blue','orange']
    return random.choice(colors)

print(""" use F + - para fazer seu desenho
      Exemplo:
      regra inicial: F-F-F-F-F
      Regra de producao: F F-F+F+FF-F-F+F
      Interação: 2 (recomendamos numeros entre 2 e 5)
      """)

condicao_inicial = input("condicao inicial: ")
regra_de_producao = input("regra de producao: ")
interacao =int(input("interacao: "))
regra_final = ""
regra_de_producao = regra_de_producao.split(' ')

# 1. aplicar regra de producao

i = 0
while i < interacao:
    regra_final = condicao_inicial.replace(regra_de_producao[0], regra_de_producao[1])
    condicao_inicial = regra_final
    i=i+1
    
print(regra_final)
turtle.speed('fast')

# 2. exibir regra final com a tartaruga

obj= turtle.Turtle()
for i in regra_final.upper():
    if i == 'F':
        turtle.pendown()
        turtle.forward(10)
    elif i == '-': 
        turtle.left(90)
    elif i == '+':
        turtle.right(90)
    elif i== 'R':
        turtle.color('red')
    elif i== 'G':
        turtle.color('green')
    elif i== 'B':
        turtle.color('blue')
    elif i== 'G':
        turtle.color('orange')
    elif i=='X':
        turtle.color(gerando_cores())
