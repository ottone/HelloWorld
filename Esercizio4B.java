/** SCRIVERE UN APPLICAZIONE CHE STAMPI I 26 CARATTERI DELL'ALFABETO INGLESE CON UN CICLO */

public class Esercizio4B{
public static void main(String argv[]){
char c = 'a';
int i;
for(i = 0; i < 26; i++) {
	c = (char) (c + i);
	System.out.println(c);
}
}
}
