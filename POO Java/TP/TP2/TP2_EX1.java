package TP2;

import java.util.Scanner;

public class Livre {
	// Attributs
	private String titre;
	private String auteur;
	private double prix;
	
	// Constructeur
	public Livre(String titre, String auteur, double prix) {
		this.titre = titre;
		this.auteur = auteur;
		this.prix = prix;
	}
	
	// Méthode d'accès (getters)
	public String getTitre() {
		return titre;
	}
	
	public String getAuteur() {
		return auteur;
	}
	
	public double getPrix() {
		return prix;
	}
	
	// Méthode Afficher
	public void afficher() {
		System.out.println("Titre : " + titre);
		System.out.println("Auteur : " + auteur);
		System.out.println("Prix : " + prix);
		System.out.println("Titre : " + titre + " ,Auteur : " + auteur + " ,Prix : " + prix);
	}
	
	public static void main(String[] args) {
		// Création d'un objet Livre en utilisant le constructeur
		Scanner scanner = new Scanner(System.in);
		
		// Saisie des informations du livre par utilisateur
		System.out.println("Livre 1 : ");
		System.out.print("Enter le titre de livre : ");
		String titre =  scanner.nextLine();
		
		System.out.print("Enter l'auteur du livre (Nom complet) : ");
		String auteur = scanner.nextLine();
		
		System.out.print("Enter le prix du livre : ");
		double prix = scanner.nextDouble();
		
		// Création de l'objet Livre avec les information saisie
		Livre livre1 = new Livre(titre, auteur, prix);
		
		// Affichage des information du livre
		System.out.println("\nInformations du livre : ");
		livre1.afficher();
		
		scanner.close();
		
		
	}
}
