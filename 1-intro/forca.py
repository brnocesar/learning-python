import random as rd

def jogar():
    print_banner("Bem vindo ao jogo de Forca!")

    word            = getWord()
    max_attempts    = 6
    guessed_letters = ["_" for letra in word]

    while (max_attempts > 0):
        guess   = input("\nAdivinhe uma letra da palavra: ").strip().upper()

        if (guess in guessed_letters):
            print("Essa letra já foi revelada, perde dois pontos!!\n")
        elif (guess in word):
            guessed_letters = add_guessed_letter(word, guess, guessed_letters)
        else:
            max_attempts -= 1

        print(guessed_letters)

        if ( "_" not in guessed_letters ):
            print("\nParabéns, você acertou a palavra: {}".format(word))
            return

    print("\n=> Fim de jogo! Você esgotou suas tentativas.\nA palavra era: {}".format(word))

def print_banner(phrase: str):
    print("\n " + (len(phrase) + 2)*"=")
    print("| {} |".format(phrase))
    print(" " + (len(phrase) + 2)*"=")
    return None

def getWord()-> str:
    with open("words.txt", "r") as file:
        list_content = [row.strip() for row in file]
    
    return list_content[rd.randrange(0, len(list_content))].upper()

def getConfig():
    pass

def add_guessed_letter(word:str, guess:str, guessed_letters:list):
    index = 0
    for letter in word:
        if (guess == letter):
            guessed_letters[index] = letter
        index += 1
    
    return guessed_letters

def choseAction():
    print("\n    /////////////////////////////////")
    print("   // Agora escolha uma ação:     //")
    print("  //  (1) jogar                  //")
    print(" //   (2) adicionar palavra     //")
    print("/////////////////////////////////")
    print("                  //")
    print("                 //")
    print("                //")
    print("       (\__/)  //")
    print("       (•ㅅ•) //")
    print("       ( 　 づ||")

    action = int(input("Action: "))
    if ( action == 1):
        jogar()
    elif ( action == 2 ):
        addWord()
    else:
        print("Opção inválida!")

def addWord():
    new_words = input("Adicione palavras para o jogo da Forca:\n(Separe-as por espaço)\n")

    file = open("words.txt", "r+")
    file_content = [row.strip() for row in file]

    for word in new_words.split():
        if (word not in file_content):
            file.write(word + "\n")
    
    file.close()
    return None

if ( __name__ == "__main__"):
    jogar()
