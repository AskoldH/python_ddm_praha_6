# Příklady k procvičení (teorie [slovníky](../teorie/10_slovniky.ipynb)) ale nejen jich.

Tyhle přiklady budeme řešit během kroužku ale můžete si je řešit i doma jakožto další procvičení. Některé budou jednoduché, jíné velmi složité. U každého se zkuste zamyslet.

Pokud čemukoli v zadání nebudete rozumět tak mi řekněte, rád vám zadání dovysvětlím. Pokud vám nepůjde něco vyřešit tak si zkuste znovu projít část teorie která by se toho mohla týkat nebo si problém co máte zkuste vyhledat na internetu, pokud ani pak nebudete tušit, rád vás navedu správným směrem. **Nejdůležitější je se nad každým úkolem/problémem pořádně zamyslet a zkusit ho vyřešit sám pomocí toho, co jsme probírali**.  

## 0
Vytvořte si anglicko-český slovník, který bude obsahovat minimálně 15 párů anglických slov a jejich českých překladů. Tedy načtěte od uživatele anglické slovo a pokud slovo bude ve slovníku tak vytiskněte uživateli jeho český překlad, pokud ve slovníku slovo nebude tak vyprintěte něco jako `"Bohužel tohle slovo nenáme ve slovníku, vyberte jiné: "`.

## 1
Vytvořte program, který bude sloužit pro výpis vzorečků pro počítání obvodů a obsahů geometrických útvarů. Uživatel zadá požadavek jako např. *obsah-ctverec* a měl by se mu vyprintit správný vzoreček pro obsah čtverce. Podporujte minimálně 4 útvary, ale čím více tím lépe. Rozšíření 1: přidejte i možnost zobrazování objemů pro kvádr, pro krychly, kouli, ... . Rozšíření 2: přidejte i možnost nápovědy, tedy pokud uživatel zada *pomoc* místo správného příkazu, tak se mu vyprintí návod jak by měl psát příkazy, tedy např.: *Příkazy piš ve formátu coTěZajímá-proJakýObrazec*. 

## 2
Vytvořte program na hraní hry *Kámen, nůžky, papír*. Mějme tuto hru pro pět kol, hrajeme proti počítači. Vyhraje ten, kdo získá jako první 3 výhry v jednotlivch kolech. Kolo probíhá tak, že necháme uživatele (hráče) vybrat kámen, nůžky nebo papír a následně si vybere náhodně (bude se hodit knihovna *random*) počítač, následně se vyhodnotí výsledek kola (podle klasických pravidel této hry) a pokud již někdo nevyhrál 3 kola tak startuje další kolo.

## 3
Vytvořte program *sledovač známek*. Tedy program do které si budeme moci nahrát naše známky ze školy, program si je uloží a dovolí nám si vybrat nějakou funkci, tedy například průměr všch známek, nejlepší známku v předmětu, nejhorší... Když zadáme nejdřív známky z matematiky a následně známky z češtiny, tak pak thle funkce budeme moci dělat pro oba dva předměty. Budou se hodit slovníky a funkce `min(), max(), sum(), len()`.

Budeme pokračovat s následujícím kódem, rozšíříme ho o zapisování do souboru: 
```python
def vrat_prumer(list_znamek):
    soucet = 0
    for znamka in list_znamek:
        soucet += znamka
    return soucet / len(list_znamek)

def vrat_nejlepsi(list_znamek):
    return min(list_znamek)

def vrat_nejhorsi(list_znamek):
    return max(list_znamek)

########################################################
nazev_predmetu = input("Zadejte název předmětu: ")
znamky_text = input("Zadejte známky oddělené mezerami: ")

list_znamek = []
for znamka in znamky_text.split():
    list_znamek.append(int(znamka))

volba = int(input("Zadejte co chcete (průměr(1), nejlepší známka(2), nejhorší známka(3)): "))

if volba == 1:
    print(vrat_prumer(list_znamek))
elif volba == 2:
    print(vrat_nejlepsi(list_znamek))
elif volba == 3:
    print(vrat_nejhorsi(list_znamek))
```

## 4 
Palindrom je slovo (či věta a nás budou prozatím zajímat jen slova), které se čte zepředu i zezadu stejně, tedy například *abba* nebo *bararab* jsou palindromy. Vytvořte program pro detekci palindromů, tedy na vstupu zadáme slovo a program vypíše zda je slvovo palindrom či ne.
