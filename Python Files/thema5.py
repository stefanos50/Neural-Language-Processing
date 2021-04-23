import nltk as nltk
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
import ast

#Γράφει το αποτέλεσμα σε ένα txt αρχείο
def write_file(trees):
    file = open("syntax_trees.txt", "w")
    for i in range(len(trees)):
        file.write(str(trees[i]) + '\n')

#Δέχεται το input που δόθηκε ελέγχεται και το επιστέφει
#σε μορφή λίστας
def check_and_return_input(input):
    try:
        input_sentences = ast.literal_eval(input)
    except ValueError:
        print("Not a list")
        exit(1)
    for i in range(len(input_sentences)):
        test = isinstance(input_sentences[i], list)
        if test == False:
            print("Not a list in a list")
            exit(1)
    return input_sentences

#Δήλωση της γραμματικής όπως στο πρωτότυπο πρόγραμμα
groucho_grammar = nltk.CFG.fromstring("""
 s -> np vp
 np -> pn | det n | n
 vp -> iv | iv adv | av adj | tv np np | v np
 iv -> 'runs' | 'run' | 'running' | 'hurts' | 'hurt' | 'hurting' | 'walks' | 'walk' | 'walking' | 'jumps' | 'jump' | 'jumping' | 'shoots' | 'shoot' | 'shooting'
 av -> 'is' | 'does' | 'are' | 'do'
 tv -> 'gives' | 'give' | 'gave' | 'giving'
 v -> 'chased' | 'chase' | 'needs' | 'need' | 'hates' | 'hate' | 'has' | 'have' | 'loves' | 'love' | 'kicks' | 'kick' | 'jumps' | 'jump'
 adj -> 'scary' | 'tall' | 'short' | 'blonde' | 'slim' | 'fat'
 adv -> 'quickly' | 'slowly' | 'independently'
 n -> 'food' | 'cat' | 'cats' | 'dog' | 'dogs' | 'book' | 'books' | 'feather' | 'feathers' | 'baby' | 'babies' | 'boy' | 'boys' | 'girl' | 'girls' | 'icecream' | 'icecreams'
 pn -> 'mary' | 'john' | 'tomy'
 det -> 'the' | 'a' | 'an' 
 """)
#Είσοδος λίστας με προτάσεις όπου κάθε πρόταση είναι μια λίστα από λέξεις από τον χρήστη
input_sentences =  input("Takes as input a list of sentences and produces their syntax trees \nExample input [['the','dog','chased','the','cat'],['mary','loves','the','cats'],['the','dog','needs','food']]\nInput:")
input_sentences = check_and_return_input(input_sentences)
parser = nltk.ChartParser(groucho_grammar)
results = []
#Για κάθε πρόταση που δόθηκε ως input
for i in range(len(input_sentences)):
    #Γίνεται parse
    for tree in parser.parse(input_sentences[i]):
        print("Syntactic tree "+str(i+1))
        print(tree)
        results.append(tree)
        #Γραφική αναπαράσταση των συντακτικών δέντρων σε ένα canvas και αποθήκευση
        #σε .ps αρχεία
        cf = CanvasFrame()
        tc = TreeWidget(cf.canvas(),tree)
        cf.add_widget(tc,10,10) # (10,10) offsets
        cf.print_to_file("tree"+str(i)+".ps")
        cf.destroy()
print("Result =",results)
write_file(results)