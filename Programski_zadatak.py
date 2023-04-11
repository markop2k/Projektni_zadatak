from datetime import date

korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input('Unesite broj korisnika: '))
for i in range(1, broj_korisnika+1):
    korisnik = {}
    korisnik['ime'] = input(f'Unesite ime {i}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {i}. korisnika: ').capitalize()
    korisnik['telefon'] = int(input(f'Unesite telefon {i}. korisnika: '))
    korisnik['email'] = input(f'Unesite email {i}. korisnika: ').strip()
    korisnici.append(korisnik)
#
br_osobnih = int(input('Unesite broj osobnih iskaznica: '))
osobne_iskaznice = []
for i in range(1, br_osobnih+1):
    osobna_iskaznica = {}
    osobna_iskaznica['broj'] = int(input(f'Unesite broj {i}. osobne: '))
    osobna_iskaznica['oib'] = int(input(f'Unesite oib {i}. osobne: '))
    osobna_iskaznica['prbivaliste'] =input(f'Unesite prebivaliste {i}.: ').capitalize()
    osobne_iskaznice.append(osobna_iskaznica)

broj_korisnika = int(input('Unesite broj korisnika: '))

for i in range(1, broj_korisnika+1):
    korisnik = {}
    korisnik['ime'] = input(f'Unesite ime {i}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {i}. korisnika: ').capitalize()
    korisnik['telefon'] = int(input(f'Unesite telefon {i}. korisnika: '))
    korisnik['email'] = input(f'Unesite email {i}. korisnika: ').strip()
    for j, osobna_iskaznica in enumerate(osobne_iskaznice, start=1):
        print(f"\t{j}. {osobna_iskaznica['oib']} ")
    odabrana_osobna = int(input("Odaberi osobnu iskaznicu"))
    korisnik['osobna_iskaznica'] = osobne_iskaznice[odabrana_osobna-1]
    korisnici.append(korisnik)

#
broj_kategorija = int(input('Unesite broj kategorija: '))

for i in range(1, broj_kategorija+1):
    kategorija = {}
    kategorija['naziv'] = input(f'Unesite naziv {i}. kategorije: ')

    artikli = []
    kategorija['artikli'] = artikli
    broj_artikala = int(input(f"Unesite broj artikala za {i} kategoriju: "))

    for j in range(1, broj_artikala + 1):
        artikl = {}
        artikl['naslov'] = input(f'Unesite naslov {j}. artikla: ')
        artikl['opis'] = input(f'Unesite opis {j}. artikla: ')
        artikl['cijena'] = float(input(f'Unesite cijenu {j}. artikla: '))
        artikli.append(artikl)

    kategorije.append(kategorija)


broj_prodaja = int(input('Unesite broj prodaja: '))

for i in range(1, broj_prodaja+1):
    prodaja = {}
    prodaja['artikl'] = artikl
    prodaja['korisnik'] = korisnik
    dan = int(input(f'Unesite dan isteka {i}. prodaje: '))
    mjesec = int(input(f'Unesite mjesec isteka {i}. prodaje: '))
    godina = int(input(f'Unesite godinu isteka {i}. prodaje: '))
    prodaja['datum'] = date(godina, mjesec, dan)

    print(f"Odaberite korisnika {i}. prodaje")

    for j, korisnik in enumerate(korisnici, start=1):
        print(f"\t{j}. {korisnik['ime']} {korisnik['prezime']}")

    okorisnik = int(input('Odabrani korisnik: '))
    prodaja['korisnik'] = korisnici[okorisnik-1]

    print(f"Odaberite kategoriju {i}. prodaje: ")

    for k, kategorija in enumerate(kategorije, start=1):
        print(f"\t{k}. {kategorija['naziv']}")

    okategorija = int(input('Odabrana kategorija: '))
    artikli = kategorije[okategorija - 1]['artikli']

    print(f"Odaberite artikl {i}. prodaje: ")

    for m, artikl in enumerate(artikli, start=1):
        print(f"\t{m}. {artikl['naslov']}")

    oartikl = int(input('Odabrani artikl: '))
    prodaja['artikl'] = kategorije[okategorija-1]['artikli'][oartikl - 1]
    prodaje.append(prodaja)

for i, prodaja in enumerate(prodaje):
    print(f"Prodaja {i+1}: ",
          f"\nInformacije o korisniku: ",
          f"\n\tIme: {prodaja['korisnik']['ime']}",
          f"\n\tPrezime: {prodaja['korisnik']['prezime']}",
          f"\n\tTelefon: {prodaja['korisnik']['telefon']}",
          f"\n\tEmail: {prodaja['korisnik']['email']}",
          f"\nInformacije o artiklu: ",
          f"\n\tnaslov: {prodaja['artikl']['naslov']}",
          f"\n\topis: {prodaja['artikl']['opis']}",
          f"\n\tcijena: {prodaja['artikl']['cijena']}",
          f"\nDatum isteka: ",
          f"\n\tDan: {prodaja['datum'].day}",
          f"\n\tMjesec: {prodaja['datum'].month}",
          f"\n\tGodina: {prodaja['datum'].year}\n",
          f"\n{prodaja['korisnik']['osobna_iskaznica']['oib']}",
          f"\n{prodaja['korisnik']['osobna_iskaznica']['broj']}",
          f"\n{prodaja['korisnik']['osobna_iskaznica']['prbivaliste']}",
          f"-"*40)