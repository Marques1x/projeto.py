nascimento = 1997
anoAtual = 2023
nascimentoJovem = 2006


def calculoIdade(nascimento, anoAtual):
    idade = anoAtual-nascimento
    return idade
idade = calculoIdade(nascimento,anoAtual)
idadejovem = calculoIdade(nascimentoJovem,anoAtual)
print('Idade é '+ str(idade))
print('idadeJovem '+ str(idadejovem))