import random	# IMPORTA IL MODULO RANDOM GENERATORE DI NUMERI CASUALI

from urllib.request import urlopen # DALLA LIBRERIA URLLIB IMPORTA URLOPEN PER SCARICARE DELLE PAROLE DALLA RETE

import sys # IMPORTA IL MODULO SYS PER L'ACCESSO A SPECIFICI PARAMETRI E FUNZIONI DEL SISTEMA

WORD_URL = "http://learncodethehardway.org/words.txt" 

WORDS = []

PHRASES = {
	"class %%%(%%%):" :
	"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	"class %%% has-a __init__ that takes self and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	"class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
	"Set *** to an instance of class %%%.",
	"***.***(@@@)":
	"From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
}

# DO THEY WANT TO DRILL PHRASES FIRST

if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST  = True
else:
	PHRASE_FIRST = False

# LOAD UP THE WORDS FROM THE WEBSITE

for word in urlopen(WORD_URL).readlines():  # LEGGE PAROLA PER PAROLA CON FOR LINEA PER LINEA
	WORDS.append(str(word.strip(), encoding="utf-8")) # ACCODA NELLA LISTA VUOTA WORDS LA CONVERSIONE IN STRINGHE DELLE PAROLE LETTE

def convert(snippet, phrase): # FUNZIONE CONVERT
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))] # RANDOM.SAMPLE(LIST, COUNT) RESTITUISCE UN INTERVALLO UNICO NELLA LISTA
	other_names = random.sample(WORDS, snippet.count("***")) 

	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count))) # JOIN COMBINA PIU STRINGHE INSIEME ES STR.JOIN(("A", "B", "C"), ".") RISULTA "A.B.C"
	
	for sentence in snippet, phrase:
		result = sentence[:] # COPIA LA LISTA IN RESULT

		# FAKE CLASS NAMES
		for word in class_names:
			result  = result.replace("%%%", word, 1)

		# FAKE OTHER NAMES
		for word in other_names:
			result = result.replace("***", word, 1)
	
		# FAKE PARAMETER LISTS
		for word in param_names:
			result = result.replace("@@@", word, 1)
	
		results.append(result)

	return results

# KEEP GOING UNTIL THEY HIT CTRL-D

try:
	while True:
	
		snippets = list(PHRASES.keys()) # RESTITUISCE UNA LISTA COMPOSTA DALLE CHIAVI KEYS() DEL DIZIONARIO PHRASES
		random.shuffle(snippets)  # RANDOM.SHUFFLE(snippets) MISCHIA CASUALMENTE GLI ELEMENTI DELLA LISTA

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question


			print(question)

			input("> ")
			print(f"ANSWER: {answer}\n\n")
except EOFError:
	print("\nBye")
