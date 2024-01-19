#randomQuizGenerator - Cria provas com pergunats e respostas em ordem aleatória

import random   #para deixar as perguntas aleatórias 

#dados para as provas, as chaves são os estados e os valores as capitais

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':
'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
 'Rhode Island': 'Providence', 'South Carolina':'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington':
'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
capitalsItems = list(capitals.items())

#gera 35 arquivos de provas
for quizNum in range(35):
    #cria os arquivos com as provas e os gabaritos das respostas
    quizFile = open('capitalsquiz%s.txt' %(quizNum+1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' %(quizNum+1),'w')
    #escreve cabeçalho da prova
    quizFile.write('Nome:\n\nData:__/__/__\n\nPeriodo:\n\n')
    quizFile.write((' '*20)+ 'Quiz de Capitais de Estados (Prova %s)' %(quizNum+1))
    quizFile.write('\n\n')
    #embaralha a ordem dos estados
    states = list(capitals.keys())
    random.shuffle(states)
    #percorre todos os 50 estados em um loop, criando perguntas para cada um
    for questionNum in range(50):
        #obtem respostas corretas e incorretas
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        
        #grava a pergunta e as opções no arquivo de prova
        quizFile.write('%s. Qual a capital de %s?\n' %(questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' %('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        #TODO: grava o gabarito com as respostas em um arquivo
        answerKeyFile.write('%s. %s\n' %(questionNum +1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()