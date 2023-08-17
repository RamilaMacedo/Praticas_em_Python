'''print('\33[7mRâmila\33[m')
nome = input('qual seu nome? ')
print('Prazer em te conhecer, {}{}{}!'.format('\33[4;35m', nome, '\33[m'))'''
#dicionário
nome = input('qual seu nome? ')
cores = {'pretoebranco':'\33[7m',
         'azul' : '\33[34m',
         'limpa' : '\33[m'}
print('Prazer em te conhecer, {}{}{}!'.format(cores['azul'], nome, cores['limpa']))


#CORES NO TERMINAL

"""
Estilo - 0 / 1(negrito) / 4(sublinhado) / 7 (inverte a cor)
"""
"""
Text - 30 (branco)/ 31(vermelho)/ 32(verde)/ 33(amarelo)/ 34(azul)/ 35(roxo)/ 36(azul)/ 37(cinza)/
"""
"""
Back/fundo - 40/ 41/ 42/ 43/ 44/ 45/ 46/ 47/
"""
#\033[m

print("\033[1;31;46m Râmila\033[m")
