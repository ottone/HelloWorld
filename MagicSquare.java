/** IMPLEMENTAZIONE DEL QUADRATO MAGICO */

public class MagicSquare{
	
	int dim; // DIMENSIONE DEL QUADRATO
	int[] celle; // VETTORE CHE MEMORIZZA I VALORI DELLE CELLE. E' COMPOSTO DA DIM X DIM ELEMENTI E LA CELLA IN POSIZIONE I,J E' INDICIZZATA DA DIM I + J
	
	// CONSTRUCTORS

	/** CREA UN QUADRATO MAGICO CON DIMENSIONE DEFINITA DAL PARAMETRO E VALORI TUTTI NULLI @PARAM  N LA DIMENSIONE DEL QUADRATO */ 

	public MagicSquare(int n){
		int i,j; // indici di cella

		dim = n;
		celle = new int[n * n];

		// INIZIALIZZAZIONE A ZERO

		for(i=0; i < n ; i++)
			for(j=0; j < n; j++) celle[n * i + j] = 0;
	}

	// METODI PRIVATI

	// CALCOLA IL SUCCESSORE PER UN INDICE 1
		
	private int succIndex(int l){
		if(l==dim-1) return 0;
		else return l+1;
	} 
	
	// CALCOLA IL PREDECESSORE PER UN INDICE l

	private int predIndex(int l){
		if(l==0) return  dim-1;
		else return l-1;
	}

		
	// METODI PUBBLICI
	
	// GENERA I VALORI MAGICI @RETURN L'OGGETTO STESSO THIS
	
	public MagicSquare makeMagic(){
		
		int i,j; // INDICI DI CELLA
		int k; 	 // INDICE PER IL VETTORE CELLE (VA DA 1 A DIM X DIM)

		i = dim / 2 +1; j = dim / 2;
		for(k=1; k<= dim*dim; k++) {
			celle[dim*i +j] = k;
			
			// RICERCA SUCCESSIVA CELLA LIBERA SE NON è L'ULTIMA

		if ( k != dim*dim ) {
			i = succIndex(i); j=succIndex(j);
			while(celle[dim*i+j] != 0) {
				i = succIndex(i); j=predIndex(j);
			}
		}
		}
		return this;

		}

		// CALCOLA LA COSTANTE MAGICA @RETURN IL VALORE DELLA COSTANTE
	
		public int magicConst()
		{
			int i,j;
			int magicnum;
			int temp;
			boolean notmagic;
			
			magicnum = 0;
			
			for (i=0; i< dim; i++) magicnum += celle[i]; // SOMMA PRIMA RIGA
			
			if (magicnum <= 1) return -1; // NON PUO' ESSERE MAGICO

			// CONTROLLA SE IL VALORE DI MAGICNUM E' UGUALE DAPPERTUTTO
				
			notmagic = false;
			for(i=1; i<dim; i++) // CONTROLLA RIGHE
			{	
					for(temp=0,j=0; j<dim ; j++) temp += celle[dim*i+j];
					if(notmagic=notmagic || (magicnum!=temp)) break;
				}
			for(temp=0,i=0,j=0;i<dim;i++,j++) // CONTROLLA DIAGONALE
				temp += celle[dim*i+j];
			notmagic=notmagic || (magicnum!=temp);
			
			for(temp=0,i=0,j=dim-1;i<dim;i++,j--) // CONTROLLA ALTRA DIAGONALE
				temp += celle[dim*i+j];
			notmagic=notmagic || (magicnum!=temp);
			
			if(notmagic) return -1;
			else return magicnum;
			}


			/** STAMPA LA DIMENSIONE, I VALORI E LA COSTANTE MAGICA DEL QUADRATO MAGICO @RETURN L'OGGETTO STESSO (THIS) */
			
			public MagicSquare display() {
				
			int i,j,k; // CONTATORI
			String value;
			

			System.out.println("Dimensione: "+dim);
			
			for(i=0;i<dim;i++){
				for(j=0; j<dim ; j++){
					value = String.valueOf(celle[dim * i + j]);
					for(k=0;k<3-value.length();k++) System.out.print(" ");
					System.out.print(value);
				}
				System.out.println();
			}
			System.out.println("Costante magica: " + magicConst());
			System.out.println();
			return this;
			}

			/** METODO PRINCIPALE */
			public static void main(String[] args) {
				
				MagicSquare square1 = new MagicSquare(5);
				MagicSquare square2 = new MagicSquare(9);
				

				square1.display();
				square1.makeMagic();
				square1.display();
			
				square2.makeMagic().display();
			}

		} // END OF CLASS MAGICSQUARE
		
	


