def fibonacci(nombre):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < nombre:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence[:nombre]


while True:
    try:
        n = int(
            input(
                "Entrez un nombre entier positif pour le nombre de termes de la séquence de Fibonacci : "
            )
        )
        if n <= 0:
            raise ValueError("Le nombre doit être positif.")
        break  # Sortir de la boucle si l'entrée est valide
    except ValueError as ve:
        print(ve)

sequence_fibonacci = fibonacci(n)
print("Les premiers", n, "termes de la séquence de Fibonacci sont:", sequence_fibonacci)
