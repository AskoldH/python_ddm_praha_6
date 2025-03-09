Tento úkol naváže na kódování textu do jedniček a nul. Vytvoříme program co testuje uživatele zda zvládne převést zakódované písmena a celá slova zpět do čitelného textu. 

# Úvodní příprava
Připravte si **tři zakódované** "šifry". Vemte libovolné věty či jen slova, a **převeďte je na číselné kódy**, jak jsme řešili kdysi dříve, texty kódujeme podle **ASCII tabulky** znak po znaku, vytvořte tedy pro každou z šifer posloupnost čísel. Například tedy pro slovo `Ahoj` bude tato posloupnost čísel `01000001
01101000
01101111
01101010`, pro větu `Ahoj Pepo!` to bude `65 104 111 106` a pro větu `Python je super jazyk!` pak `80 121 116 104 111 110 32 106 101 32 115 117 112 101 114 32 106 97 122 121 107 33`. Tyhle šifry, tedy posloupnosti čísel si někam zapište budeme je potřebovat dále.

# Programování
Vytvořte program, který otestuje zda umí uživatel přeložit šifru v binárním kódu zpět do textu. Podrobněji: Vytvořte program, který se nejdřív zeptá jakou šifru chce uživatel řešit (jsou na výběr tři). Po výběru šifry se uživateli zobrazí šifra, tedy posloupnost čísel reprezentující text (připomeňme, že máme posloupnost čísel v desítkové soustatavě, tedy např. `65 104 111 106` pro `Ahoj` a tu mějte uloženou jako list čísel), šifru ale budeme chtít vytisknout v binární soustavě, k tomuto převodu použíjeme funkci `format(x, '08b')`, kde `x` je proměnná obsahující číslo (tedy můžeme použít `print(format(x, '08b'))` pro tisk binárního zápisu čísla do konzole). Po tisku šifry do konzole pak nechme uživatele zadat řešení šifry, tedy převod do textu, pokud odpoví správně, tak uživateli vypište *Dobrá práce!* a nechte ho vybrat jinou šifru. Pokud odpoví špatně, tak vypište *Nezvládl jsi to, běž se to doučit.* a program nechte skončit.

Poznámky: Budou se určitě hodit listy, funkce a cykly. Správné řešení šifry můžeme mít uložené v jednoduše v promenné tedy např. `sifra1_text = "Ahoj"`. Funkce se pak bude hodit k např. k výpisu šifry jako jedničky a nuly.

Příklad jak by mohla vypadat interakce programu (P) a uživatele (U): 
```
P: Vyber si šifru k řešení (napiš 1/2/3): 
U: 2
P: Šifra je: 01000001 01101000 01101111 01101010
P: Jak zní šifra jako text? :
U: Ahoj
P: Dobrá práce! Vyber si další šifru k řešení (napiš 1/2/3):
U: 1
...
```

# Testování
Nejdříve svůj program pořádně otestujte, následně už nezbývá nic jiného, než to přimo otestovat kolegy z křoužku, nebo spíš otestovat kolegy zda umí převádět jedničky a nuly na text!

Jedno z možných řešení úkolu:
```python
def vypis_sifru(sifra_list):
    print()
    for cislo in sifra_list:
        print(format(cislo, '08b'), end=" ")
    print()

def zpracuj_sifru(sifra_list, sifra_text):
    vypis_sifru(sifra_list)
    reseni_od_uzivatele = input("Zadej text který představují binární čísla: ")
    if reseni_od_uzivatele == sifra_text:
        print("Správná odpověď! Dobrá práce. Zkus další šifru...\n")
        return True
    else: 
        print("Špatná odpověď, běž potrénovat a mrknout se jak to funguje.")
        return False

##############################################################################

sifra_1 = [65, 104, 111, 106, 49]
sifra_1_text = "Ahoj1"

sifra_2 = [65, 104, 111, 106, 50]
sifra_2_text = "Ahoj2"

sifra_3 = [65, 104, 111, 106, 51]
sifra_3_text = "Ahoj3"

uspech = True

while uspech:
    vyber_uzivatele = int(input("Zadejtej číslo šifry, kterou chceš řešit: " ))
    if vyber_uzivatele == 1: 
        uspech = zpracuj_sifru(sifra_1, sifra_1_text)
    elif vyber_uzivatele == 2: 
        uspech = zpracuj_sifru(sifra_2, sifra_2_text)
    elif vyber_uzivatele == 3: 
        uspech = zpracuj_sifru(sifra_3, sifra_3_text)
```