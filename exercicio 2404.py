from datetime import datetime
nome = input('Olá, seja bem vindo(a). Digite o seu nome: ')
while True:
    nasci = input('{}, digite sua data de nascimento (DD/MM/AAAA): '.format(nome))
    try: 
        nasci = datetime.strptime(nasci, '%d/%m/%Y') #strptime converte a data de str para uma data do datetime
        break
    except ValueError: #Caso o usuário não digite a data no formato esperado (causando um ValueError), ele será instruído, em vez de dar erro no código
        print('Formato inválido. Use (DD/MM/AAAA)')
hoje = datetime.today()
idade = hoje.year - nasci.year
aniv = (hoje.day, hoje.month) == (nasci.day, nasci.month)
while True:
    socio = input('{}, você é sócio do Clube Delta?\n a)Sim\n b)Não\n'.format(nome)).lower()
    if socio in ['a', 'b']:
        break
    else:
        print('Resposta inválida.')
val = float(input('Por fim, {}, digite o valor da sua compra: R$'.format(nome)))
if val > 100:
    if socio == 'a' and aniv == False:
        print('Caro {}, você recebeu R$10,00 de desconto. Portanto, o valor final de sua compra é de R${:.2f}.'.format(nome, val - 10))
    elif idade >= 60 and aniv == False:
        print('Caro {}, você recebeu R$10,00 de desconto. Portanto, o valor final de sua compra é de R${:.2f}.'.format(nome, val - 10))
    elif socio == 'a' and aniv:
        print('Caro {}, primeiramente, gostariamos de te desejar um feliz aniversário. Como presente, nós da equipe Delta, te daremos um desconto de  R$15,00. Portanto, o valor final de sua compra é de R${:.2f}.'.format(nome, val - 15))
    else:
        print('Caro {}, nós sentimos muito, mas você não possui direito a descontos.'.format(nome))
else:
    print('Caro {}, nós sentimos muito, mas você não possui direito a descontos.'.format(nome))