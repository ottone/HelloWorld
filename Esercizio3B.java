/** SCRIVERE UN PROGRAMMA CON I SEGUENTI REQUISITI: 
	
    UTILIZZA UNA CLASSE PERSONA CHE DICHIARA LE VARIABILI NOME, COGNOME ETA. SI DICHIARI INOLTRE UN METODO DETTAGLI() CHE RESTITUISCA UN UNA STRIGA LE INFORMAZIONI
    SULLA PERSONA IN QUESTIONE. UTILIZZA UNA CLASSE PRINCIPALE CHE NEL METODO MAIN(), ISTANZIA DUE OGGETTI CHIAMATI PERSONA1 E PERSONA2 DELA CLASSEPERSONA INIZIALIZ
    ZANDO PER OGNIUNO DI ESSI I RELATIVI CAMPI ADOPERANDO L'OPERATORE  DOT. DICHIARARE UN TERZO REFERENCE (PERSONA3) CHE PUNTI AD UNO DEGLI OGGETTI GIA' ISTANZIATI
    COMMENTARE ADEGUATAMENTE LE CLASSI REALIZZATE  SFRUTTANDO LO STRUMENTO JAVADOC PER PRODURRE LA RELATIVA DOCUMENTAZIONE.
*/



/** Classe principale si chiama come il file altrimenti java non compila */

public class Esercizio3B{
public static void main(String[] args){

/** Istanze e inizializzazioni di persona1 e persona2 */
Persona persona1 = new Persona();
Persona persona2 = new Persona();
persona1.nome = "Mario";
persona1.cognome = "Rossi";
persona1.eta = 30;
System.out.println("persona1 " + persona1.dettagli());

persona2.nome = "Giuseppe";
persona2.cognome = "Verdi";
persona2.eta = 40;
System.out.println("persona2 " + persona2.dettagli());

/** Dichiarazione di persona3 che referenzia persona1 */

Persona persona3 = persona1;
System.out.println("persona3 " + persona3.dettagli());
}
}
