Už toho umíme z Pytohnu hodně, v tomto větším úkolu si to vše zkusíme procvičit abychom viděli, že nám to k něčemu je. Řešení tohoto úkolu budeme postupně vylepšovat, začneme s jednodušší verzí a dostaneme se postupným vylepšováním až k složitějším verzím. Budeme programovat minihru:

# Minihra potápění lodí
Jedná se o minihru, kde hráč má za úkol potopit lodě nepřítele rozmístěné na moři reprezentované mřížkou postupným posílání torpén na určité pozice v této mřížče. Tahle mřížka tedy obsahuje políčka, každé políčko má svou souřadnici pro řádek a pro sloupce. Lodě tedy musí být umístěny na nějakých souřadnicích. Cílem je tedy co nejrychleji potopit všechny lodě nepřítele. Jak už bylo zmíněno budeme mít několik verzí této minihry.

## Verze 0 - DEMO
Mějme mřížku o rozměrech 5x5 políček (tedy 25 políček). Loď bude mít velikost jen jednoho políčka a budeme ji mít prozatím jen jednu na moři (v mřížce), pozici lodi v mřížce zvolte napevno při programování. Naprogramujte tuhle verzi minihry kdy uživatele donekončena hádá kde je loď pomocí dvou souřadnic (řádku a sloupce), jakmile uhodne kde je loď tak ji potomí (vypíšeme uživateli že uspěl) a hra končí. Také kontrolujte zda uživatel zadává validní souřadnice do mřížky, pokud zadá nějakou nevalidní např. 8 (což je větší než rozsah mřížky) tak ho informujte, že máme mřížku velkou jen 5x5 políček.

Tady je kód pro základní verzy, projdeme si ho společně:
```python
sloupec_lodi = 4
radek_lodi = 2
max_sloupec = max_radek = 5

print(f"Vítej ve hře, tvým úkolem je potopit loď!")
print(f"Hádej její souřadnice řádku (0 až {max_radek-1}) a sloupce {max_sloupec-1}...")

while True:
    print("===================================================")
    
    nacteny_radek = int(input("Zadejte číslo řádku: "))
    if nacteny_radek < 0 or nacteny_radek > max_radek - 1:
        print(f"Špatně jsi zadal souřadnici řádku, rozsah je 0 až {max_radek-1}")
        continue
    
    nacteny_sloupec = int(input("Zadejte číslo sloupce: "))
    if nacteny_sloupec < 0 or nacteny_sloupec > max_sloupec- 1:
        print(f"Špatně jsi zadal souřadnici sloupce, rozsah je 0 až {max_sloupec-1}")
        
    if (nacteny_radek == radek_lodi) and (nacteny_sloupec == sloupec_lodi):
        print("Potopil jsi loď!")
        break
    else:
        print("Netrefil ses!")
```

## Verze 1
Rozšíříme verzi 0 o další 2 lodě, tedy budeme mít celkem 3 lodě na moři, hra tedy končí až uživatel potopí všechny tři lodě. Také uživateli vypište na kolikáte torpédo (na kolikátý pokus) potopil všechny lodě. Rozměry mřížky zůstávají stejné.

## Verze 2
Rozšíříme stávající verzi o tisknutí na obrazovku hracího pole. Budeme rozlišovat několik typů políček a to: Již hádané políčko kde nebyla loď (označení např. 'x'), políčko kde byla loď a je potopena (např. '!') a dosud nehádané políčko kde může být prázdné moře nebo loď (např. '?'). Hlavní je vypisování hracího pole udělat tak, aby se v něm uživatel vyznal, tedy udělejte to podle toho, jak vám to dává smysl. Hint: Budou se hodit listy listů pro reprezentaci hracího pole a jejcih proházení. 