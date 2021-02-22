valor = float(input('\033[4;36m Qual e o valor da casa:\033[m R$'))
salario = float(input('\033[4;33m Qual e o seu salario?:\033[m R$'))
anos = float(input('\033[4;35m Quantos anos de finansiamento\033[m? '))
prestaçao = valor / (anos * 12)
minimo = salario * 30 / 100
print('\033[4;34m para pagar uma casa de R${:.2f} em {} anos\033[m'.format(valor, anos))
print('\033[4;33m a prestaçao sera de R${:.2f}\033[m'.format(prestaçao))
if prestaçao <= minimo:
    print('\033[4;32mEmprestimo pode ser CONCEDIDO\033[m')
else:
    print('\033[4;31;44mEmprestimo NEGADO!')

