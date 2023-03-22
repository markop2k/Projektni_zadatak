from datetime import date
korisnik = {}
korisnik['ime'] = input("Unesite ime korisnik: ").capitalize()
korisnik['prezime'] = input("Unesite prezime korisnik: ").capitalize()
korisnik['telefon'] = int(input("Unesite telefon korisnika: "))
korisnik['email'] = input("Unesite email korisnika: ").strip()

artikl = {}
artikl['naslov'] = input("Unesite naslov artikla: ")
artikl['opis'] = input("Unesite opis artikla: ")
artikl['cijena'] = float(input("Unesite cijenu artikla: "))


prodaja = {}
prodaja['korisnik'] = korisnik
prodaja['artikl'] = artikl
dan= int(input("Unesite dan isteka prodaje: "))
mjesec= int(input("Unesite mjesec isteka prodaje: "))
godina= int(input("Unesite godinu isteka prodaje: "))
prodaja['datum'] = date(godina,mjesec,dan)

print(f"Informacije o artiklu: "
      f"\n\t\tNaslov: {prodaja['artikl']['naslov']} "
      f"\n\t\tOpis: {prodaja['artikl']['opis']} "
      f"\n\t\tCijena: {prodaja['artikl']['cijena']} "
      f"\nDatum isteka prodaje: "
      f"\n\t\tDan: {prodaja['datum'].day}"
      f"\n\t\tMjesec: {prodaja['datum'].month} "
      f"\n\t\tGodina: {prodaja['datum'].year} "
      f"\nInformacije o korisniku: "
      f"\n\t\t{prodaja['korisnik']['ime']} {prodaja['korisnik']['prezime']}"
      f"\n\t\tTelefon: {prodaja['korisnik']['telefon']}"
      f"\n\t\tEmail: {prodaja['korisnik']['email']}")