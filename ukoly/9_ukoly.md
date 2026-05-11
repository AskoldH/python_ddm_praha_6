# Příklady k procvičení (teorie [slovníky](../teorie/10_slovniky.ipynb)) ale nejen jich.

Tyhle přiklady budeme řešit během kroužku ale můžete si je řešit i doma jakožto další procvičení. Některé budou
jednoduché, jíné velmi složité. U každého se zkuste zamyslet.

Pokud čemukoli v zadání nebudete rozumět tak mi řekněte, rád vám zadání dovysvětlím. Pokud vám nepůjde něco vyřešit tak
si zkuste znovu projít část teorie která by se toho mohla týkat nebo si problém co máte zkuste vyhledat na internetu,
pokud ani pak nebudete tušit, rád vás navedu správným směrem. **Nejdůležitější je se nad každým úkolem/problémem pořádně
zamyslet a zkusit ho vyřešit sám pomocí toho, co jsme probírali**.

## 0

Vytvořte si anglicko-český slovník, který bude obsahovat minimálně 15 párů anglických slov a jejich českých překladů.
Tedy načtěte od uživatele anglické slovo a pokud slovo bude ve slovníku tak vytiskněte uživateli jeho český překlad,
pokud ve slovníku slovo nebude tak vyprintěte něco jako `"Bohužel tohle slovo nenáme ve slovníku, vyberte jiné: "`.

## 1

Vytvořte program, který bude sloužit pro výpis vzorečků pro počítání obvodů a obsahů geometrických útvarů. Uživatel zadá
požadavek jako např. *obsah-ctverec* a měl by se mu vyprintit správný vzoreček pro obsah čtverce. Podporujte minimálně 4
útvary, ale čím více tím lépe. Rozšíření 1: přidejte i možnost zobrazování objemů pro kvádr, pro krychly, kouli, ... .
Rozšíření 2: přidejte i možnost nápovědy, tedy pokud uživatel zada *pomoc* místo správného příkazu, tak se mu vyprintí
návod jak by měl psát příkazy, tedy např.: *Příkazy piš ve formátu coTěZajímá-proJakýObrazec*.

## 2

Vytvořte program na hraní hry *Kámen, nůžky, papír*. Mějme tuto hru pro pět kol, hrajeme proti počítači. Vyhraje ten,
kdo získá jako první 3 výhry v jednotlivch kolech. Kolo probíhá tak, že necháme uživatele (hráče) vybrat kámen, nůžky
nebo papír a následně si vybere náhodně (bude se hodit knihovna *random*) počítač, následně se vyhodnotí výsledek kola (
podle klasických pravidel této hry) a pokud již někdo nevyhrál 3 kola tak startuje další kolo.

## 3

Vytvořte program *sledovač známek*. Tedy program do které si budeme moci nahrát naše známky ze školy, program si je
uloží a dovolí nám si vybrat nějakou funkci, tedy například průměr všech známek, nejlepší známku v předmětu, nejhorší...
Když zadáme nejdřív známky z matematiky a následně známky z češtiny, tak pak thle funkce budeme moci dělat pro oba dva
předměty. Budou se hodit slovníky a funkce `min(), max(), sum(), len()`.

## 4

Palindrom je slovo (či věta a nás budou prozatím zajímat jen slova), které se čte zepředu i zezadu stejně, tedy
například *abba* nebo *bararab* jsou palindromy. Vytvořte program pro detekci palindromů, tedy na vstupu zadáme slovo a
program vypíše zda je slvovo palindrom či ne.

# Postupy úkolů 3

Vytvořte program *sledovač známek*. Tedy program do které si budeme moci nahrát naše známky ze školy, program si je
uloží a dovolí nám si vybrat nějakou funkci, tedy například průměr všech známek, nejlepší známku v předmětu, nejhorší...
Když zadáme nejdřív známky z matematiky a následně známky z češtiny, tak pak thle funkce budeme moci dělat pro oba dva
předměty. Budou se hodit slovníky a funkce `min(), max(), sum(), len()`.

### Postup:

1. Nejdříve si vytvoříme prázdný slovník (např. `znamky = {}`), do kterého budeme ukládat data.
   Klíčem bude název předmětu a hodnotou bude seznam jeho známek, tedy například `"cestina": [1, 2, 2, 1]`.
2. Pomocí funkce `input()` se zeptáme na název předmětu a následně na známky. Známky od uživatele
   přijdou jako jeden text (např. `"1 5 2"`).
3. Abychom mohli se známkami počítat, musíme text rozdělit na jednotlivé kousky pomocí
   `.split()` a každý kousek převést na celé číslo pomocí `int()`. Tato čísla si uložíme do seznamu.
4. Tento seznam čísel uložíme do našeho slovníku pod klíčem s názvem předmětu, použijeme
   `znamky[nazev_predmetu] = seznam_znamek`.
5. Takto to provedeme pro libovolně předmětů, které chce uživatel přidat, končíme pokud uživatel zadá místo
   názvu předmětu `stop`.
6. Výpis statistic záleží na tom, co uživatel chce, takže se ho zeptáme, samozřejmě pomocí funkce `input()`, vyberem
   podle toho zna učivatel zadá `nejlepsi`, `nejhorsi` nebo `prumer`. U statistik se pak ještě musíme zeptat uživatele
   jaký předmět ho zajímá, například `cestina`, to bude i klíčem do slovníku abychom získali seznam známek.
7. Jednotlivé statistiky vypočítáme pomocí funkcí `min(seznam_znamek)` pro nejlepší známku, `max(senzma_znamek)` pro
   nejhorší a průměr vypočítáme jako součet vydělený počtem známek (`sum(seznam_znamek) / len(seznam_znamek)`) a
   výsledky vypíšeme uživateli.

Rozšíření pro ukládání do souboru a následné načítání z něj:

* Úplně na začátek přidáme otázku na uživatele, zda chce přečíst data ze souboru, data v něm budou mít strukturu
  `predmet,znamka_1,znamka_2,...` tedy například `matika,1,2,3,1`, to bude jeden řádek souboru, takových řádků tam může
  být několik. Pokud uživatel chce načíst data ze souboru, tak si otevřeme soubor pomocí
  `with open("data.txt", "r") as soubor:` a přečteme a zpracujeme řádky, řádky zpracujeme tak, že si je přidáme do
  slovníku stejně jako data načtená od uživatele.
* Před ukončením programu musíme data zase uložit, to uděláme pomocí `with open("data.txt" "w") as soubor:` a pomocí
  průchodu slovníku s daty pomocí `for nazev, seznam_znamek in znamky.items():` a pomocí `soubor.write()` je uložíme do
  souboru.