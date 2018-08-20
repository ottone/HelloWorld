import sys # IL MODULO SYS DA ACCESSO AD ALCUNE VARIABILI COME ARGS

script, input_encoding, errors = sys.argv  # LISTA DEGLI ARGOMENTI PASSATI ALLO SCRIPT PYTHON

def main(language_file, encoding, errors ):  # LA FUNZIONE MAIN RICEVE COME PARAMETRI L'OGGETTO FILE LA CODIFICA E IL TIPO DI ERRORE DELLA CODIFICA. SUCCESSIVAMENTE LEGGE UNA LINEA DAL FILE E SE LA LETTURA 
	line = language_file.readline()	     # è ANDATA A BUON FINE RICHIAMA LA FUNZIONE PRINT_LINE E SUCCESSIVAMENTE RICHIAMA SE STESSA (RICORSIONE) PROSEGUENDO COSI NELLA LETTURA DELLE LINEE DEL FILE	

	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)

	
def print_line(line, encoding, errors):				   # LA FUNZIONE PRINT_LINE RICEVE LA LINEA LETTA PASSATA DA MAIN() INSIEME ALLA CODIFICA E AD ERRORS. ASSEGNA A NEXT_LANG UNA COPIA DELLA STRINGA CON I CARATTERI
	next_lang = line.strip()                                   # DI INIZIO E FINE RIGA RIMOSSI
	raw_bytes = next_lang.encode(encoding, errors=errors)      # ASSEGNA A RAW_BYTES LA STRINGA CODIFICATA SECONDO LA CODIFICA PASSATA IN ARGOMENTO
	cooked_string = raw_bytes.decode(encoding, errors=errors)  
	
	print(raw_bytes, "<===>", cooked_string)

	
languages = open("languages.txt", encoding="utf-8") # NELLA FUNZIONE OPEN è POSSIBILE FORNIRE IL PARAMETRO ENCODING ED ERRORS. ENCODINGS è IL NOME DELLA CODIFICA UTILIZZATA
						    # PER DECODIFICARE IL FILE. ERRORS è UN PARAMETRO OPZIONALE CHE SPECIFICA COME GESTIRE GLI ERRORI DI CODIFICA PASSANDO 
						    # 'STRICT' PER ATTIVARE UN VALUE ERROR  SE INCONTRA ERRORI O IGNORE PER IGNORARE L'ERRORE. 	

main(languages, input_encoding, errors)

