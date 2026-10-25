
print("========== BUN VENIT LA BANCA GEORGE! ==========")
print("=" * 50)

nume_user = input("Cum te numesti ?  --  ")
nastere_user = int(input("Care este anul nasteri ?  --  "))

# Setăm o valoare inițială pentru sold
sold_user = 0 

parola_user = input("Alegeti o parola  --  ")

while parola_user == "1234" or parola_user == str(nastere_user):
    print("Parola nu este destul de puternica")
    parola_user = input("Alegeti o parola  --  ")

parola_confirmata = input("Confirma parola  --  ")

if parola_confirmata == parola_user:
    print("Perfect, sa trecem la pasul urmator")
else:
    print("Parolele nu coincid")
    parola_confirmata = input("Reintrodu parola  --  ")

print("=" * 50)
# .lower() transformă totul în litere mici (funcționează și la Adult, ADULT, etc.)
cont_ales = input("Ce cont alegeti (adult/junior)  --  ").lower()

varsta = 2026 - nastere_user

if varsta < 18 and cont_ales == "adult":
    print("Va rugam sa alegeti contul junior deoarece aveti mai putin de 18 ani")
elif varsta >= 18 and cont_ales == "junior":
    print("Aveti varsta prea mare pentru contul junior")
    print("Va rugam sa alegeti contul pentru adulti")
else:
    print("Aveti varsta necesara")

print("=" * 50)
# .lower() rezolvă problema și pentru "Da", "DA", etc.
optiune_user = input("Doriti sa depuneti bani in cont ? (da/nu)  --  ").lower()

if optiune_user == "da":
    sold_user = input("Alegeti suma  --  ")
else:
    print("Nu este nicio problema")

print("=" * 50)
print(f"Soldul dumneavoastra este de -- {sold_user}")
print("Felicitari, ati finalizat toti pasii!")
print("=" * 50)
print("========== LA REVEDERE! ==========")
