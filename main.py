# Da completare con il codice

#CLASSE Studente
"""#STATO:
cognome: cognome dello studente (stringa)
nome: nome dello studente (stringa)
matricola: numero di matricola (intero positivo)
listaesami: lista di tuple (codice -- str, voto--int positivo >= 18 e <33)
"""

"""METODI da aggiungere oltre a quelli presenti:

- Costrutture: metodo che inizializza lo studente con cognome, nome e matricola presi come argomenti e inizializza listaesami con lista vuota,
    controllando che i tipi dei parametri attuali abbiano il tipo corretto altrimenti solleva un'eccezione TypeError
- Getters: metodi che restituiscono il valore di una variabile di istanza, es: get_cognome() --> restituisce il cognome
- Setters: metodi che modificano il valore di una variabile di istanza, es: set_cognome(cognome) --> modifica il cognome
    controllare che i valori inseriti siano del tipo e del valore corretto altrimenti sollevare un'eccezione TypeError o ValueError

"""

class Studente:

    def __init__(self, cognome, nome, matricola, listaesami):
        if type(cognome) != str or type(nome) != str:
            raise TypeError(f'Il parametro nome/cognome deve essere una stringa')
        if type(matricola) != int:
            raise TypeError(f'Il parametro matricola deve essere un numero intero')
        if type(listaesami[0][0]) != str or (type(listaesami[0][1]) != int and listaesami[0][1] < 18 and listaesami[0][1] >= 33):
            raise TypeError(
                f'Il parametro listaesami deve essere una tupla formata da una stringa e un intero (maggiore o uguale di 18 e minore di 33)'

    self.cognome = cognome
    self.nome = nome
    self.matricola = matricola
    self.listaesami = listaesami

stud1 = Studente("Ergoli", "Salvatore", 660527, [("Programmazione e analisi dati", 18)])
print(stud1)
