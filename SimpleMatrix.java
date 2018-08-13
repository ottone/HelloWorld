/**
* NUMERI COMPLESSI
*/

public class SimpleMatrix
{
	int righe;	/* NUMERO DI RIGHE */
	int colonne;	/* NUMERO DI COLONNE*/
	double[][] data;	/* MATRICE */

	/* CONSTRUCTORS */

	/* IL CONSTRUCTORS CREA UNA MATRICE 4 X 4 E SETTA I VALORI DI RIGHE E COLONNE */

	public SimpleMatrix ()
	{
		righe = colonne = 4;
		data = new double[4][4]; /* INIZIALIZZA L'ARRAY DI ARRAY DATA AD UN ARRAY 4 X 4 CON ISTRUZIONE NEW */
	}

	/* CREA UNA MATRICE DI ZERI @PARAM N NUMERO DI RIGHE @PARAM M NUMERO DI COLONNE */
	
	public SimpleMatrix (double[][] initdata)
	{
	int i,j;
	
		righe = initdata.length /* INIZIALIZZA RIGHE ALLA LUNGHEZZA DELL'ARRAY INITDATA */
		colonne = initdata[0].length /* STESSA COSA PER LE COLONNE */
		data = new double[righe][colonne]; /* INIZIALIZZA DATA ALLA DIMENSIONE DELL'ARRAY BIDIMENSIONALE INITDATA CHE VERRA' PASSATO AL METODO SIMPLEMATRIX */


