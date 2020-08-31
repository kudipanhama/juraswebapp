"""

File: Savings.py
***
The objective is to create a terminal application that is able to simulate the core logic when saving money within an Angolan
savings account. It will demonstrate using relevant numbers for one bank and product, subsequently, it will scale up to being a
Web App with ability to compare various products from various banks.
"""
ANO = 365
TAC = 0.10

def main():
    tanb = 0.045
    prazo = 30

    capital = print_intro()

    print()
    jurosb = calc_juros_brutos(capital, tanb, prazo)
    jurosl = calc_juros_liquidos(jurosb)
    print("Os seus juros brutos recebíveis são: " + str(jurosb))
    print("Os seus juros líquidos recebíveis são: " + str(jurosl))
    print()

    print("O seu retorno total será de: " + str(capital + jurosl))

def calc_juros_liquidos(jurosb):
    jurosl = jurosb * (1 - TAC)
    return jurosl

def calc_juros_brutos(capital, tanb, prazo):
    jurosb = (capital * tanb * prazo)/ANO
    return jurosb

def get_capital():
    capital = float(input("Introduza o seu capital inicial: ")) #error catching needed: spaces, commas
    return capital

def print_intro():
    print()
    print("Bem vindo ao simulador de dépositos à prazo, Juras?!\nEste simulador permite-lhe deduzir uma estimativa do retorno numa aplicação depósito à prazo,\ncom base no capital introduzido pelo cliente.")
    print()
    capital = get_capital() #function used to collect usergen capital data
    return capital

if __name__ == '__main__':
    main()