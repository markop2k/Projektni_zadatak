from datetime import date
korisnik = {}
korisnik['ime'] = input("Unesite ime korisnik:").capitalize()
korisnik['prezime'] = input("Unesite prezime korisnik:").capitalize()
korisnik['telefon'] = int(input("Unesite telefon korisnika: "))
korisnik['email'] = input("Unesite email korisnika:").strip()
#print("Kolegij",kolegij['predmet'],"nosi",kolegij['ects'],"ECTS bodova.")

artikl = {}
artikl['naslov'] = input("Unesite naslov artikla:")
artikl['opis'] = input("Unesite opis artikla:")
artikl['cijena'] = float(input("Unesite cijenu artikla:"))


prodaja = {}
prodaja['korisnik'] = korisnik
prodaja['artikl'] = artikl
dan= int(input("Unesite dan isteka prodaje:"))
mjesec= int(input("Unesite mjesec isteka prodaje:"))
godina= int(input("Unesite godinu isteka prodaje: "))
prodaja['datum'] = date(godina,mjesec,dan)

print(f"Informacije o artiklu: "
      f"\nNaslov:{prodaja['artikl']['naslov']} "
      f"\nOpis:{prodaja['artikl']['opis']} "
      f"\nCijena:{prodaja['artikl']['cijena']} "
      f"\nDatum isteka prodaje: "
      f"\nDan:{prodaja['datum'].day}"
      f"\nMjesec:{prodaja['datum'].month} "
      f"\nGodina:{prodaja['datum'].year} "
      f"\nInformacije o korisniku: "
      f"\n{prodaja['korisnik']['ime']} {prodaja['korisnik']['prezime']}"
      f"\nTelefon:{prodaja['korisnik']['telefon']}"
      f"\nEmail:{prodaja['korisnik']['email']}")