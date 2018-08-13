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

	public SimpleMatrix()
	{
		righe = colonne = 4;
		data = new double[4][4]; /* INIZIALIZZA L'ARRAY DI ARRAY DATA AD UN ARRAY 4 X 4 CON ISTRUZIONE NEW */
	}

	
	public SimpleMatrix(int n , int m)
	{
		righe = n;
		colonne = m;
		data = new double[n][m];
	}


	/* CREA UNA MATRICE DI ZERI @PARAM N NUMERO DI RIGHE @PARAM M NUMERO DI COLONNE */
	
	public SimpleMatrix(double[][] initdata)
	{
	int i,j;
	
		righe = initdata.length; /* INIZIALIZZA RIGHE ALLA LUNGHEZZA DELL'ARRAY INITDATA */
		colonne = initdata[0].length; /* STESSA COSA PER LE COLONNE */
		data = new double[righe][colonne]; /* INIZIALIZZA DATA ALLA DIMENSIONE DELL'ARRAY BIDIMENSIONALE INITDATA CHE VERRA' PASSATO AL METODO SIMPLEMATRIX */

	
		for (i=0; i < righe; i++)
			for (j=0; j < colonne; j++)
				data[i][j]=initdata[i][j];

	}

	


	/** METODI PUBBLICI  */

	/** SOMMA DI DUE MATRICI @PARAM X IL SECONDO OPERANDO DELLA SOMMA @RETURN UNA MATRICE IL CUI VALORE È THIS+X */

	public SimpleMatrix add(SimpleMatrix x)
	{
		SimpleMatrix ris; // OGGETTO SIMPLEMATRIX
		int i,j;

		if ((righe != x.righe) || (colonne != x.colonne))
			throw new ArithmeticException ("Incompatible Matrix");
		ris = new SimpleMatrix(righe,colonne);
		for(i=0 ;i<righe;i++)
			for(j=0;j<colonne; j++)
				ris.data[i][j] = data[i][j]+x.data[i][j];
		return ris;
	}

	/** MOLTIPLICA DUE MATRICI  @PARAM X IL SECONDO OPERANDO DELLA MOLTIPLICAZIONE @RETURN UNA MATRICE IL CUI VALORE E' THIS*X */

	public SimpleMatrix multiply(SimpleMatrix x)
	{
		SimpleMatrix ris;
		double temp;
		int i,j,k;

		if((righe != x.righe) || (colonne != x.colonne))
			throw new ArithmeticException ("Incompatible Matrix");

		ris = new SimpleMatrix(righe,colonne);
		for(i=0; i<righe; i++)	
			for(j=0;j<colonne;j++){
				temp=0.0;
				for(k=0; k<righe; k++) temp = temp + data[i][k]*x.data[k][j];
				ris.data[i][j] = temp;
				}
		return ris;
	}
		
	/** MOLTIPLICA UNA MATRICE PER UNO SCALARE DI TIPO DOUBLE @PARAM X IL VALORE SCALARE @RETURN UNA MATRICE IL CUI VALORE È X*THIS */

	public SimpleMatrix scalar (double x)
	{
		SimpleMatrix ris;
		int i, j;

		ris =new SimpleMatrix(righe, colonne);
		
		for(i=0; i< righe; i++)
			for(j=0; j <colonne; j++)
				data[i][j]*=x;
		return ris;
	}
		
	/** CONVERTE UN NUMERO COMPLESSO IN UNA STRINGA @RETURN UNA STRINGA CHE RAPPRESENTA  IL NUMERO COMPLESSO */

	public String toString()
	{
		String matrep = "[";
		int i,j;
		
		for(i=0; i<righe ; i++)
		{
			matrep += "[";
			for(j=0; j<colonne; j++)
			{
				matrep = matrep + String.valueOf (data[i][j]);
				if (j != colonne - 1)
					matrep += ",";

			}

			matrep += "]";
		}
			return matrep;
	} 

	/** METODO PRINCIPALE */

	public static void main (String[] args)
	{

		SimpleMatrix mat1, mat2, mat3;
		double[][] a={{1.2 , -0.75 ,1.8},
			      {-0.99 , 3.45 , -4.89},
			      {-9.8 , 0.08 , 1.98}};

		double[][] a1={{1.0 , 0.0 , 0.0},
			       {0.0 , 1.0 , 0.0},
			       {0.0 , 0.0 , 1.0}};
		
		mat1 = new SimpleMatrix(a1);
		System.out.println (mat1.toString());
		mat2 = new SimpleMatrix(a);
		System.out.println (mat2.toString());
		mat3 = mat2.add (mat1);
		System.out.println (mat3.toString());
		mat3 = mat2.multiply (mat1);
		System.out.println (mat3.toString());
		
	}

} /* END OF CLASS SIMPLE MATRIX */ 
