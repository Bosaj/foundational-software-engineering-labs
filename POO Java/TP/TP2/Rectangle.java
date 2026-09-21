package TP2;

import java.util.Scanner;
 
public class Rectangle {
	// Attributs
	private double longueur;
	private double largeur;
	
	// Constructeur d'initialisation
	public Rectangle(double longueur, double largeur) {
		this.longueur = longueur;
		this.largeur = largeur;
	}
	
	// Methodes d'accès
	public double getLongueur() {
		return longueur;
	}
	
	public void setLongeur(double longueur) {
		this.longueur = longueur;
	}
	
	public double getLargeur() {
		return largeur;
	}
	
	public void setLargeur(double largeur) {
		this.largeur = largeur;
	}
	
	// Methode
	public double calculerPerimetre() {
		return 2 * (longueur + largeur);
	}
	
	public double calculerAire() {
		return longueur * largeur;
	}
	
	public boolean estCarre() {
		return longueur == largeur;
	}
	
	public void afficherRectangle() {
		System.out.println("Longueur : " + longueur + " - Largeur : " + largeur + " - Périmètre : " + calculerPerimetre() + " - Aire : " + calculerAire() + " \n- " + (estCarre() ? "il s'agit d'un carré" : "il ne s'agit pas d'un carré"));
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Rectangle 1");
		System.out.print("Donner la longeur du rectangle : ");
		double longueur1 = scanner.nextDouble();
		System.out.print("Donner la largeur du rectangle : ");
		double largeur1 = scanner.nextDouble();
		Rectangle rect1 = new Rectangle(longueur1, largeur1);
		System.out.println("Le périmétre est : " + rect1.calculerPerimetre());
		System.out.println("La surface est : " + rect1.calculerAire());
		rect1.afficherRectangle();
		
		System.out.println("\nRectangle 2 : ");
		System.out.print("Donner la longeur du rectangle : ");
		double largueur2 = scanner.nextDouble();
		System.out.print("Donner la largeur du rectangle : ");
		double largeur2 = scanner.nextDouble();
		Rectangle rect2 = new Rectangle(largueur2, largeur2);
		System.out.println("Le périmétre est : " + rect2.calculerPerimetre());
		System.out.println("La surface est : " + rect2.calculerAire());
		
		rect2.afficherRectangle();
		scanner.close();
	}
	
}
