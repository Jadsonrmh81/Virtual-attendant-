while True:

   u = input('Digite "go" para iniciar: ').lower()

   if not 'go' in u:
      print('Erro. Tente novamente.')
      break

   else: 
         
       print('Olá! Serei sua assistente virtual. Abaixo estão suas opções de escolha. Como posso ajudá-lo(a)?')
       print()
       print('1 - Saldo da conta')
       print('2 - Fazer depósito')
       print('3 - Efetuar pagamento')
       print('4 - Fazer emprestimo')
       print('5 - Finalizar atendimento')
       print()   

   while True:
       user = input('Escolha: ')
 
       if user.isdigit():
        
        if (user) == 5: # always define 'int' for the variable, not for the number.
            print('Atendimento encerrado. Agradecemos a preferencia!')
            break
        elif int(user) == 1: 
             print('Seu saldo atual é: R$ 1049,00')

        elif int(user) == 2:             
             num = input('Insira o número da conta bancária: ')
             value = input('Insira o valor desejado: ')

             if not num.isdigit() or not value.isdigit():
                print('Algo deu errado. Tente novamente. ')
             else:
                print(f'Depósito de {value} feito com sucesso na conta {num}')

        elif int(user) == 3:
            
             print('Pic Pay')
             print('Cartão de crédito')
             print('Boleto')
             pay = input('Informe a forma de pagamento: ')

        elif int(user) == 4:
            insert = input('Insira o valor do imprestimo: ')
            if not insert.isdigit():
                print('Algo errado. Tente novamente.')
            else:
                print(f'Emprestimo de R${insert},00 feito com sucesso.')
         
      

# entender e testar primeiro. Melhorar depois.
# intenção conta muito em programação
# a ordem dos códigos muda tudo
# validar antes de usar

#break NUNCA sai de dois loops ao mesmo tempo.
#Ele só quebra um nível.