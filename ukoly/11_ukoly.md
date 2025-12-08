# Tyhle příklady slouží k procvičení bitových operací v Pythonu

## 0 Teplotní senzor
Máme teplotní senzor co s námi komunikuje bitově, posílá nám jen nuly a jedničky. Chceme zpracovat zprávy co posílá. Zpráva vypadá následovně: 
* [1.] byte je SYNC blok který slouží k označení začátku zprávy, je vždy `0b10101010`
* [2.] byte je ID senoru, je to tedy číslo od 0 do 255, např. id=13=`0b00001101`
* [3.] byte je složený ze dvou informací (každá bude zabírat 4 bity), z typu hodnoty (hodnota 1 je teplota, hodnota 2 je tlak, 3 je vlhkost, ..., my budeme používat jen teplotu, tedy `0b0001`), další informací je počet měření, tedy počet hodnot co následně máme očekávat, tedy například `0b0100` pro 4 měření (máme na toto číslo 4 bity, tedy maximálně můžeme mít 15 měření)
* [4.] až [počet měření] byty jsou čísla z rozsahu [-128, 127] používající pro záporná čísla dvojkový doplněk. Např. 16˚C = `0b00010000` nebo -5˚C = `0b11111011`
* [-1] Posledním bytem je kontrolní informace o počtu jedniček co se objevil ve zprávě (bez tohoto posledního bytu), pokud se liší od skutečného počtu jedniček tak je zpráva poškozena.

Celá zpráva může vypadat tedy například jako: [SYNC, senzor_id, typ_hodnoty, pocet_mereni, val1, val2, kontrola] pro 2 měření.

Dostanete soubory `duben.bin`, `prosinec.bin` a `leden.bin`, které budete analyzovat, každý jeden řádek souboru je jedna zpráva (jeden packet), který budete muset zpracovat.

Zjistěte pro daný měsíc měření (pro jeden soubor s daty) průměrnou teplotu, nejmenší a nejvyšší teplotu. Poškozené zprávy zahoďte, nezpracovávejte je. 

Může se hodit tento snippet kódu pro čtení binárně ze souboru:
```python
packets = []
with open("duben.bin", "rb") as file:
    for line in file:
        packet = list(line.strip())
        print(packet)
        
        packets.append(packet)
```
V listu packets je na konci cyklu celý soubor hodnot, je to list listů, kde každá položka je jedna zpráva ke zpracování.

Můžou se taky hodit [informace o dvojkovém doplňku](https://cs.wikipedia.org/wiki/Dvojkov%C3%BD_dopln%C4%9Bk) nebo [informace o bitových operátorech](https://www.geeksforgeeks.org/python/python-bitwise-operators/), zejméne o bitovému and, not či posunu. 

