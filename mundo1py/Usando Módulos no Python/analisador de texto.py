nome = 'Râmila Oliveira de Macêdo dos Santos'
print('Analisando seu nome: ')
print('todo seu nome em letra maiúscula', nome.upper())
print('todo seu nome em letra minúscula', nome.lower())
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome contem {} letras'.format(nome.find(' ')))

print('tambem pode ser feito assim...')
nome1 = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(nome1[0], (len(nome1[0]))))
