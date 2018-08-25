/** SCRIVERE UN SEMPLICE PROGRAMMA COSTITUITO DA UN'UNICA CLASSE CHE SFRUTTANDO ESCLUSIVAMENTE UN CICLO INFINITO, L'OPERATORE MODULO, DUE COSTRUTTI IF, UN BREAK ED UN
    UN CONTINUE, STAMPI SOLO I PRIMI CINQUE NUMERI PARI
*/

public class Esercizio4A{
public static void main(String args []){

int i = 0;

while (true)
{
i++;
if (i > 10)
break;
if ((i % 2) != 0)
	continue;
System.out.println(i);	
}

}
}
