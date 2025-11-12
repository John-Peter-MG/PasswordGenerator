import random as rd
import time

MINUSCULAS = 'abcdefghijklmnopqrstuvwxyz'
MAIUSCULAS = MINUSCULAS.upper()
ESPECIAIS = '*()_-!@#$%&+=;:'
NUMEROS = '1234567890'
STRINGS = [MINUSCULAS, MAIUSCULAS, ESPECIAIS, NUMEROS]

def initialize_seed():
    seed_input = input('Insira a senha que você quer transformar: ')
    if seed_input == '':
        seed_input = time.time()
    else:
        seed_input = seed_converter(seed_input)
    rd.seed(hash(seed_input))

def seed_converter(string):
    bin =''.join(format(ord(char), '08b') for char in string)
    return int(bin)

def gerar_senha():
    senha = [rd.choice(MINUSCULAS), rd.choice(MAIUSCULAS), rd.choice(ESPECIAIS), rd.choice(NUMEROS)]
    for i in range(8):
        selecao = rd.choice(STRINGS)
        selecao = selecao[rd.randint(0,len(selecao)-1)]
        senha.append(selecao)
    rd.shuffle(senha)
    return ''.join(senha)

def main():
    initialize_seed()
    senha = gerar_senha()
    print(f'Essa é a sua senha: {senha}\nGuarde-a bem')

if __name__ == '__main__':
    main()