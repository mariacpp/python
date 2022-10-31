f = open('aula04/exercicios/arquivo.txt', 'w')
f.write('''O texto dissertativo é um dos estilos de escrita mais exigidos nos concursos, em vestibulares e outras provas.
No Exame Nacional do Ensino Médio (Enem), por exemplo, os candidatos são submetidos à uma redação dissertativo-argumentativa, que é um dos tipos de dissertação.
Escrever um bom texto dissertativo exige domínio da língua portuguesa e capacidade de apresentar as informações seguindo uma linha lógica.
Afinal, o leitor precisa ter clara compreensão sobre o que está sendo transmitido, de forma que não exista ruídos e ou qualquer dificuldade de interpretação.
É, de fato, um desafio.
Por isso, no próprio Enem, são poucos os candidatos que conquistam a nota máxima.
Em 2019, por exemplo, atingiram 1.000 pontos (a nota máxima) apenas 53 dos quase 4 milhões de estudantes que realizaram o exame. 
Mas este dado não serve para te desanimar e, sim, para te incentivar a fazer parte desse seleto grupo de pessoas.
Nas próximas linhas, além de descobrir qual é a estrutura adequada para a redação do Enem, você vai aprender como escrever um texto dissertativo excelente.''')
f.close()


n = int(input('Quantas linhas você que ler? \n'))

try:
    f = open("aula04/exercicios/arquivo.txt", "r")
    linhas = f.readlines()
    for i in range(0,n):
        print(linhas[i])
    f.close()
    '''for l in linhas:
        print(l)        '''
except:
    print('Você não digitou um número inteiro!')