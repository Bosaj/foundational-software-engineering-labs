package TP2;

import java.util.Scanner;

	public class Complexe {
		// Attributs
		private double partieReelle;
		private double partieImaginaire;
		
		// Constructeur par défaut
		public Complexe() {
			this.partieReelle = 0;
			this.partieImaginaire = 0;
		}
		
		//Construction d'initialisation
		public Complexe(double partieReelle, double partieImaginaire) {
			this.partieReelle = partieReelle;
			this.partieImaginaire = partieImaginaire;
		}
		
		// Méthode d'accèes (getters)
		public double getPartieReelle() {
			return partieReelle;
		}
		public double getPartieImaginaire() {
			return partieImaginaire;
		}
		
		//Méthode pour ajouter un nombre complexe
		public Complexe plus(Complexe autre) {
			double nouvellePartieReelle = this.partieReelle + autre.partieReelle;
			double nouvellePartieImaginiaire = this.partieImaginaire + autre.partieImaginaire;
			return new Complexe(nouvellePartieReelle, nouvellePartieImaginiaire);
		}
		
		// Méthode pour soustraire un nombre complexe
		public Complexe moins(Complexe autre) {
			double nouvellePartieReelle = this.partieReelle - autre.partieReelle;
			double nouvellePartieImaginiaire = this.partieImaginaire - autre.partieImaginaire;
			return new Complexe(nouvellePartieReelle, nouvellePartieImaginiaire);
		}
		
		//Méthode pour afficher le nombre complexe
		public void afficher() {
			System.out.println(partieReelle + ( partieImaginaire >= 0 ? "+" : "" ) + partieImaginaire + "*i" );
		}
		public static void main(String[] args) {
			Scanner scanner = new Scanner(System.in);
			
			// Saisie des partie réelle et imaginaire pour le 1er nombre complexe
			System.out.println("Nombre Complexe 1 : ");
			System.out.print("Donner la partie reeélle : ");
			double partieReelle1 = scanner.nextDouble();
			System.out.print("Donner la partie imaginiare : ");
			double partieImaginaire1 = scanner.nextDouble();
			Complexe complexe1 = new Complexe(partieReelle1, partieImaginaire1);
			
			// Saisie des partie réelle et imaginaire pour le 2eme nombre complexe
			System.out.println("Nombre Complexe 2 : ");
			System.out.print("Donner la partie reélle : ");
			double partieReelle2 = scanner.nextDouble();
			System.out.print("Donner la partie Imaginiaire : ");
			double partieImaginaire2 = scanner.nextDouble();
			Complexe complexe2 = new Complexe(partieReelle2, partieImaginaire2);
		
		
			// Afffichage des nombre complexe
			System.out.print("\n Nombre complexe 1 : ");
			complexe1.afficher();
		
			System.out.print("\n Nombre complexe 2 : ");
			complexe2.afficher();
		
			// Test d'addition et de soustraction
			Complexe somme = complexe1.plus(complexe2);
			Complexe difference = complexe1.moins(complexe2);
		
			// Affichage des resultats
			System.out.print("\nLa somme : ");
			somme.afficher();
			System.out.print("\nLa defférence : ");
			difference.afficher();
		
			scanner.close();
		}
}