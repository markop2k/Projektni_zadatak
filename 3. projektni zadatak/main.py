from kategorija import unos_kategorije
from korisnik import unos_korisnika
from prodaja import unos_prodaje, ispis_prodaje

korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input('Unesite broj korisnika: '))

for i in range(1, broj_korisnika+1):
    korisnici.append(unos_korisnika(i))

broj_kategorija = int(input('Unesite broj kategorija: '))

for i in range(1, broj_kategorija+1):
    kategorije.append(unos_kategorije(i))

broj_prodaja = int(input('Unesite broj prodaja: '))

for i in range(1, broj_prodaja+1):
    prodaje.append(unos_prodaje(korisnici, kategorije, i))

for i, prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}: ")
    ispis_prodaje(prodaja)
