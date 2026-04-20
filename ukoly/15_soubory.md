# Příklady k procvičení (teorie [práce se soubory](../teorie/11_soubory.ipynb)) ale nejen jich.

Tyhle přiklady budeme řešit během kroužku ale můžete si je řešit i doma jakožto další procvičení. Některé budou
jednoduché, jíné velmi složité. U každého se zkuste zamyslet.

Pokud čemukoli v zadání nebudete rozumět tak mi řekněte, rád vám zadání dovysvětlím. Pokud vám nepůjde něco vyřešit tak
si zkuste znovu projít část teorie která by se toho mohla týkat nebo si problém co máte zkuste vyhledat na internetu,
pokud ani pak nebudete tušit, rád vás navedu správným směrem. **Nejdůležitější je se nad každým úkolem/problémem pořádně
zamyslet a zkusit ho vyřešit sám pomocí toho, co jsme probírali**.

## 0

Vytvořte program, který založí nový textový soubor s názvem `tajny_denik.txt`. Program se pomocí funkce `input()` zeptá
na dnešní datum a na to, jaký jste dnes měli den. Obě tyto informace následně zapíše do souboru na samostatné řádky.
Nezapomeňte k zápisu bezpečně použít blok `with open(...)` v režimu pro zápis.

## 1

Vytvořte program, který otevře soubor `tajny_denik.txt` z předchozí úlohy v režimu pro čtení. Program přečte celý jeho
obsah a vypíše ho na obrazovku.

## 2

Představte si, že organizujete oslavu a zapisujete si hosty do souboru `hoste.txt`. Napište program, který poběží v
nekonečném cyklu a bude se ptát na jména dalších hostů. Každé zadané jméno ihned připíše na konec souboru na nový
řádek (pozor, abyste si nepřepsali ty předchozí – budete potřebovat režim přidávání). Cyklus a celý program se ukončí,
když uživatel napíše slovo `"konec"`. Zápis je mód číslo jedna, vytvořte i mód číslo dva, kdy se vypíše na obrazovku jen 
celkový počet hostů a prohram skončí. Rozhodnutí jaký mód se má provést provede uživatel hned na začátku programu, program
se ho zeptá.

## 3

Nejprve si ručně vytvořte textový soubor `inventar.txt` a pod sebe do něj napište několik věcí, které si berete na
výpravu (např. meč, jablko, lano, mapa). Následně vytvořte program, který tento soubor otevře a postupně projde všechny
položky řádek po řádku. Program musí vypsat každou věc na obrazovku, ale přidá k ní i její pořadové číslo (např.
`"1. meč"`, `"2. jablko"`). Na konci program vypíše zprávu s celkovým počtem věcí v batohu.

## 4

Vytvořte si soubor `vsechny_lektvary.txt` a dejte do něj seznam různých lektvarů. Některé budou jedovaté (obsahují ve
jméně slovo `"jed"`) a jiné léčivé (např. *"jedový lektvar"*, *"léčivý lektvar"*, *"silný jed"*, *"lektvar
neviditelnosti"*). Napište program, který tento soubor přečte. Pokud načtený řádek NEobsahuje slovo `"jed"`, program
tento lektvar bezpečně zapíše do zbrusu nového souboru s názvem `bezpecne_lektvary.txt`. Jedovaté lektvary bude
ignorovat. Budete muset chytře využít čtení a zápis dohromady.