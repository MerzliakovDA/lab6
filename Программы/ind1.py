def print_characters_vertically(sentence):

  if not isinstance(sentence, str):
        print("Ошибка: Введите строку.")
        return
    
  if not sentence: # Проверка пустой строки
    print("Ошибка: Строка пустая.")
    return
    
  indices = [1, 2, 5, 6]  # Начальные индексы

  i = 0
  char_count = 0
  while char_count < len(sentence):
    if i < len(indices):
        index_to_use = indices[i] - 1
        if index_to_use < len(sentence): # защита от выхода индекса за границы строки
            print(sentence[index_to_use])
            char_count = index_to_use+1
        else:
            char_count +=1  
        i+=1 
    else:
      # Добавляем следующие пары индексов
        indices.append(indices[-2] + 4)
        indices.append(indices[-2] + 4)
        
  
if __name__ == "__main__":
    sentence = input("Введите предложение: ")
    print_characters_vertically(sentence)

