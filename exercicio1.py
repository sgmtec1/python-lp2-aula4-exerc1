'''
Nesta questão você deve identificar as partes problemáticas do código e reescrevê-lo utilizando
tratamento de exceções.
Ou seja, devem ser i dentificadas todas as exceções que podem ser geradas e, para cada uma,
deve ser dado o tratamento adequado que, nesse exercício, significa alertar o usuário quanto ao
problema.
x = int( input ( 'Primeiro valor:' ))
y = int( input ( 'Segundo valor:' ))
z = x / y
print ( 'O resultado da divisão é:' , z)
'''
try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y
    print('O resultado da divisão é:', z)
except ZeroDivisionError:
    print('Ocorreu uma divisão por zero.')
except ValueError:
    print('Ocorreu um erro de conversão de tipos. O valor informado deve ser inteiro.')
except Exception:
    print('Ocorreu um erro inesperado.')
else:
    print('Programa finalizado com sucesso')