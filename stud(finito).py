def inserisci(stud, cognome, nome, matricola, listaesami, note=""):
    if isinstance(stud, dict) and isinstance(cognome, str) and isinstance(nome, str) and isinstance(matricola, int) and matricola > 0 \
            and isinstance(listaesami, list) and len(listaesami) <= 1 and isinstance(note, str):  # controllo di tutti i tipi dei parametri con una catena di condizioni
        if (len(listaesami) == 0) or (isinstance(listaesami[0][0], str) and isinstance(listaesami[0][1], int) and listaesami[0][1] >= 18 and listaesami[0][1] <= 33):
            stud[matricola] = cognome, nome, matricola, listaesami, note
            return True
    return False


def serializza(stud):
    stringa = ""
    for valori in stud.values():  # considero tutte le possibili combinazioni di note si/no e listaesami piena/vuota
        if valori[3] == [] and valori[4] == '':
            stringa += f'{valori[1]} {valori[0]} mat: {valori[2]} esami: no note = no\n'
        elif valori[3] == [] and valori[4] != '':
            stringa += f'{valori[1]} {valori[0]} mat: {valori[2]} esami: no note = {valori[4]}\n'
        elif valori[3] != [] and valori[4] == '':
            stringa += f'{valori[1]} {valori[0]} mat: {valori[2]} esami: {valori[3]} note = no\n'
        elif valori[3] != [] and valori[4] != '':
            stringa += f'{valori[1]} {valori[0]} mat: {valori[2]} esami: {valori[3]} note = {valori[4]}\n'
    return stringa


def studente(stud, matricola):
    # restituisce i valori di uno studente con una certa matricola (matricola è chiave del dizionario)
    return stud.get(matricola)


def registra_esame(stud, matricola, codice, voto):
    if matricola in stud.keys():
        # aggiunge alla lista listaesami una nuova tupla con codice e voto
        stud[matricola][3].append((codice, voto))
        return True
    else:
        return False


def media(stud, matricola):
    if matricola in stud.keys():
        lista_esami = stud.get(matricola)[3]  # ritorna la lista degli esami
        somma_voti = 0
        for a in lista_esami:
            somma_voti += a[1]
        # calcola la media e la converte in un numero decimale
        return float(somma_voti/len(lista_esami))


def modifica_voto(stud, matricola, codice, voto):  # def modifica voto RIVISTA
    if matricola in stud.keys():
        for valori in stud.values():
            # scorre l'indice di tutti gli elementi in listaesami
            for i in range(len(valori[3])):
                # controlla se il nostro parametro è uguale al codice di un certo esame
                if valori[3][i][0] == codice:
                    #  assegnamento di una nuova tupla
                    valori[3][i] = (codice, voto)
                    return True
        else:
            return False  # restituisce False se il codice non è presente nei valori
    else:
        return False  # restituisce False se la matricola non è presente nelle chiavi


def cancella_esame(stud, matricola, codice):
    if matricola in stud.keys():
        for elementi in stud.values():
            for i in range(len(elementi[3])):
                if elementi[3][i][0] == codice:
                    # cancella la tupla dove c'è l'esame con indice i
                    del elementi[3][i]
                    return True
        else:
            return False
    else:
        return False


def lista_studenti_promossi(stud, codice, soglia=18):
    studenti_promossi = []
    for elementi in stud.values():
        for i in range(len(elementi[3])):
            # controlla se il voto è maggiore o uguale rispetto alla soglia e se il parametro 'codice' è uguale a quello dell'esame
            if elementi[3][i][1] >= soglia and elementi[3][i][0] == codice:
                # aggiunge alla lista cognome, nome e matricola dello studente
                studenti_promossi.append(
                    (elementi[0], elementi[1], elementi[2]))
    return studenti_promossi


def conta_studenti_promossi(stud, codice, soglia=18):
    # richiamo la funzione qui sopra per restituire il numero di studenti promossi
    return len(lista_studenti_promossi(stud, codice, soglia))


def lista_studenti_media(stud, soglia=18):
    soglia_studenti_promossi = []
    for elementi in stud.values():
        somma_voti_studente = 0  # variabile che sarà resettata a zero per ogni nuovo studente
        for i in range(len(elementi[3])):
            # incrementa la variabile con il voto
            somma_voti_studente += elementi[3][i][1]
            if somma_voti_studente/len(elementi[3]) >= soglia:
                # aggiunge lo studente alla lista solo se la media è superiore o uguale alla soglia indicata sopra
                soglia_studenti_promossi.append((elementi[0], elementi[1]))
    return soglia_studenti_promossi


