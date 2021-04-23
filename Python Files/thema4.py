#Λίστα με ascii αριθμούς που πρέπει να αποφεύχθουν
avoid = [32,10,13,33,34,44,59,45]

#Διαβάζει ένα αρχείο του οποίου το όνομα δέχεται ως όρισμα
def read_from_file(file_name):
    try:
        file1 = open(file_name, "r+",encoding="utf8")
        print("The file text is:")
        text = file1.read()
        return text
    except OSError as e:
        print("File does not exist.")

#Γράφει τα αποτελέσματα σε ένα txt αρχείο
def write_file(result):
    file = open("lexical_analysis.txt", "w")
    for i in range(len(result)):
        file.write(str(result[i]) + '\n')

#Μετατρέπει κείμενο σε λίστα με ascii αριθμούς
def text_to_ascii_list(text):
    return ([ord(c) for c in text])

#Μετατρέπει κείμενο σε μόνο μικρά γράμματα
def text_to_lower(text):
    return text.lower()

#Επιστρέφει μια λέξη από τη λίστα με τους ascii χαρακτήρες
def one_word(ascii_list):
    word = []
    while True:
        if ascii_list[0] == 46:
            return ''.join(chr(i) for i in word), ascii_list
        if (ascii_list[0] in avoid) and not word:
            ascii_list.pop(0)
            continue
        if ascii_list[0] in avoid:
            return ''.join(chr(i) for i in word),ascii_list
        word.append(ascii_list[0])
        ascii_list.pop(0)
        #print(word)
    return ''.join(chr(i) for i in word),ascii_list

#Επιστρέφει μια πρόσταση όταν βρεθεί η τελεία στη λίστα με τους ascii χαρακτήρες
#ή όταν η λίστα αδειάσει
def one_sentence(ascii_list):
    sentence_words = []
    while True:
        if ascii_list[0] == 46:
            ascii_list.pop(0)
            break
        if not ascii_list:
            break
        a_word,ascii_list = one_word(ascii_list)
        sentence_words.append(a_word)
        #print(sentence_words)
    return sentence_words,ascii_list

#Επιστρέφει λίστα με προτάσεις όπου κάθε πρόταση είναι μια λίστα από λέξεις
#όταν αδειάσει η λίστα με τους ascii αριθμούς
def tokenize(remaining_ascii_ls):
    sentences = []
    while True:
        a_sentence,remaining_ascii_ls = one_sentence(remaining_ascii_ls)
        sentences.append(a_sentence)
        #print(sentences)
        if not remaining_ascii_ls:
            break
    return sentences

#Υλοποίηση λεκτικού αναλυτή
def lexical_analyse(text_file):
    text = read_from_file(text_file)
    text = text_to_lower(text)
    print(text)
    result = tokenize(text_to_ascii_list(text))
    print(result)
    return result

fl = input("Input the file name:")
result = lexical_analyse(fl)
write_file(result)