frase = 'Curso em Video Python'
print(frase)
print('Formatted phrase (position 9):', frase[9])
print('Formatted phrase (position 9 to 13):', frase[9:13])
print('Formatted phrase (position 9 to 21 with the interval of 2):', frase[9:21:2])
print('Formatted phrase (position 0 to 5):', frase[:5])
print('Formatted phrase (position 15 until the end):', frase[15:])
print('Formatted phrase (position 9 to the end with the interval of 3):', frase[9::3])
print('Length:', len(frase))
print('How many times does the letter \'o\' appears in the phrase?')
print('{} times'.format(frase.count('o')))
print('{} time between 0 and 13 position'.format(frase.count('o', 0, 13)))
print('Where does the letters \'deo\' from the phrase begin? ')
print('They begin on the {} position '.format(frase.find('deo')))
print('Does the \'Android\' word is in the phrase? ')
print(frase.find('Android'))
print('Is there the \'Curso\' word in the phrase? ')
print('Curso' in frase)
print('Replace the \'Python\' word in the phrase for the \'Android\' word!')
print(frase.replace('Python', 'Android'))
print('Put the phrase in Uppercase letters!')
print(':', frase.upper())
print('Put the phrase in lowercase letters!')
print(':', frase.lower())
print('Put only the first letter of the phrase in Uppercase letters format!')
print(frase.capitalize())
print('Capitalize the entire phrase!')
print(frase.title())
frase = '   Aprenda Python  '
print('\n', frase)
print('Please refactor the phrase above!')
print(frase.strip())
print('Give another example of the refactored phrase!')
print(frase.rstrip())
print(frase.lstrip())
frase = 'Curso em Video Python'
print('Divide the string \'Curso em Video Python\' into a list!')
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[0][1])
print(dividido[1][0])
print('Turn the list(string) into an entire phrase again!')
print(' '.join(dividido))

print("""\nSoneto de fidelidade\n
De tudo ao meu amor serei atento
Antes, e com tal zelo, e sempre, e tanto
Que mesmo em face do maior encanto
Dele se encante mais meu pensamento.

Quero vivê-lo em cada vão momento
E em seu louvor hei de espalhar meu canto
E rir meu riso e derramar meu pranto
Ao seu pesar ou seu contentamento

E assim, quando mais tarde me procure
Quem sabe a morte, angústia de quem vive
Quem sabe a solidão, fim de quem ama

Eu possa me dizer do amor (que tive):
Que não seja imortal, posto que é chama
Mas que seja infinito enquanto dure.\n\nVinicius de Moraes""")
