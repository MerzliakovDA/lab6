def move_first_to_last(word):

    if not isinstance(word, str):
        print("Ошибка: Введите строку.")
        return word  
    if not word:
      print("Ошибка: Введена пустая строка.")
      return word 
    
    if len(word) == 1:
        return word 
    
    if not word.isalpha():
      print("Ошибка: Введена строка содержащая не только буквы")
      return word 
    
    first_char = word[0]
    rest_of_word = word[1:]
    modified_word = rest_of_word + first_char

    return modified_word


if __name__ == "__main__":
    input_word = input("Введите слово: ")
    result = move_first_to_last(input_word)
    print(f"Модифицированное слово: {result}")
