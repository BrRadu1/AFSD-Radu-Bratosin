elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
#A
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
notmax = max(note)
notmin = min(note)
print(f"Nota maxima este {notmax}.")
print(f"Nota minimca este {notmin}.")
print ("Elevii cu nota maxima")
for i in range(len(note)):
    if note[i] == notmax:
        print(f"- {elevi[i]}")
        print("Elevii cu nota minima")
for i in range(len(note)):
    if note[i] == notmin:
        print(f"-{elevi[i]}")

media = sum(note) / len(note)
print(f"Media clasei este {media:.2f}")
for i in range (len(note)):
    if note[i] >= 5:
        print( elevi[i])
#B
for i in range(len(note)):
     note[i] = note[i] + 1
     if note[i] > 10:
         note[i] = 10
print("Noile note:" , note)
elevi.append(elev_nou)
note.append(nota_elev_nou)
print("Lista elevilor:", elevi)
print("Lista notelor:", note)

indice_elev_de_sters=elevi.index(elev_de_sters)
elevi.remove(elev_de_sters)
nota_elev_sters=note[indice_elev_de_sters]
note.remove(nota_elev_sters)
print(elevi,note)

for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
#C
promovati = 0
respinsi = 0
for i in range(len(note)):
    if note[i] >= 5:
        promovati = promovati + 1
    else:
        respinsi = respini + 1
print(respinsi,promovati)

