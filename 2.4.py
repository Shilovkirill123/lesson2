answer = {'Как жизнь?': 'Чудесно!',
 'Чем занимаешься?' : 'Учусь программировать' ,
  'Как успехи?' : 'Получается потихоньку'}

while True :
    question=input('Задайте вопрос: ')
    if question in answer:
        print(answer[question])
    elif question == 'Стоп':
        break
    else:
        print('Думаю...')
   