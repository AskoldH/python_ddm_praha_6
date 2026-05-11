# Tyhle příklady slouží k procvičení základních konceptů algoritmizace a implementace těchto algoritmů v Pythonu

Tyhle příklady budeme řešit během kroužku ale můžete si je řešit i doma jakožto další procvičení. Některé budou
jednoduché, jíné velmi složité. U každého se zkuste zamyslet.

Příklady slouží k procvičení algoritmizace, tedy není špatným nápadem nejdřív zkusit vymyslet postup řešení tento
algoritmus zkusit naprogramovat.

## 0 - Ukázkový

Vymyslete algoritmus, který určí, kolik je v zadaním textu písmen a kolik čísel. Budou se hodit funkce `isalpha()` (
určí, zda je znak písmeno) a `isdigit()` (určí, zda je text číslice).

Příklady:

* vstup: `mám 79 let`, výstup: `písmen: 6, číslic: 2`
* vstup: `333 stříbrných`, výstup: `písmen: 10, číslic: 3`

## 1 - Nejdelší slovo

Vymyslete algoritmus, který na vstupu dostane text a na výstup vytiskne nejdelší slovo v tomto textu, nejdelších slov
může být více a tedy v základní verzi vytiskněte jen to první nalezené a následně rešení rozšiřte o vytisknutí všech
nejdelších slov.

Příklady:

* vstup: `ahoj Arabelo toto tamto je vážně přehezké`, výstup: `přehezké`
* vstup: `adam je fakt fraja`, výstup: `fraja`
* vstup: `rozbil se mi reprák`, výstup: `rozbil reprák`

## 2 - Hledání slova

Vymyslete algoritmus, který na vstupu dostane text a slovo, na výstup vytiskne `true` pokud se slovo nachází v textu a
`false` pokud nikoli.

Příklady:

* vstup: `ahoj Arabelo toto tamto je vážně přehezké` a `ahoj`, výstup: `true`
* vstup: `ahoj Arabelo toto tamto je vážně přehezké` a `Pepa`, výstup: `false`
* vstup: `adam je fakt fraja` a `fakt`, výstup: `true`

## 3 - Hledání genu

Vymyslete algoritmus, který zpracuje genetický kód, neboli projde řetězec genetického kódu (dostal ho na vstupu) a
hledá, jestli se v něm nachází nějaký gen (zadaný na vstupu), pokud se tam nachází tak vytiskne `true`, jinak vytiskne
`false`. Genetický kód se skládá ze znaků `A`, `T`, `C` a `G`.

Příklady:

* vstup: `ATCGATCATCGAT` a `ATC`, výstup: `true`
* vstup: `ATCGATCATCGAT` a `TCAA`, výstup: `false`
* vstup: `GCATATCGTAA` a `GTAA`, výstup: `true`
* vstup: `GCATATCGTAA` a `GCAA`, výstup: `false`

## 4 - Statistiky textu

Vymyslete algoritmus, který projde text zadaný na vstupu a následně vytiskne statistiky o tomto textu, konkrétně nás
zajímá počet opakování znaků v textu, tedy počítáme např. počet `a`, `b`, `1`, `2`, ...

Příklady:

* vstup: `andula`, výstup: `a: 2, n:1, d:1, u:1, l:1`
* vstup: `barbora a barbar`, výstup: `b:4, a:5, r:4, o:1`
* vstup: `anakonda`, výstup: `a:3, n:2, k:1, o:1, d:1`

# Postupy úkolů 3 a 4 v Pythonu

## 3 - Hledání genu

Vymyslete algoritmus, který zpracuje genetický kód, neboli projde řetězec genetického kódu (dostal ho na vstupu) a
hledá, jestli se v něm nachází nějaký gen (zadaný na vstupu), pokud se tam nachází tak vytiskne `true`, jinak vytiskne
`false`. Genetický kód se skládá ze znaků `A`, `T`, `C` a `G`.

Příklady:

* vstup: `ATCGATCATCGAT` a `ATC`, výstup: `true`
* vstup: `ATCGATCATCGAT` a `TCAA`, výstup: `false`
* vstup: `GCATATCGTAA` a `GTAA`, výstup: `true`
* vstup: `GCATATCGTAA` a `GCAA`, výstup: `false`

Postup:

1. Nejdříve potřebujeme načíst genetický kód a gen (obojí jako text) pomocí `input()`. Tyto funkce tedy použijeme dvě a
   výsledek si uložíme do proměnných.
2. Dále už můžeme pokročit k zjištění, jestli je gen v genetickém kódu. Použijeme `for` cyklus. Projdeme genetický kód
   postupně po znaku.
3. V každém kroku musíme kontrolovat zda aktuální znak není začátkem našeho genu. Například pokud je aktuální znak `A` a
   náše genu je `ATC`, tak jsme zjistili, že to sedí a musíme se podívat zda sedí druhý znak. Budeme to kontrolovat
   pomocí `if` podmínky, konkrétně pomocí `znak == gen[i]`, zda se aktuální znak rovná znaku na indexu `i` v genu.
4. Pokud sedí všechny znaky z genu a gen již neosahuje žádné další znaky, tak jsme zjistili že gen se v genetickém kódu
   nachází a tedy vytiskneme `true`. Pokud dojdeme na konec genetického kódu a ještě jsme nenašli gen, můžeme vytisknout
   `false`.

## 4 - Statistiky textu

Vymyslete algoritmus, který projde text zadaný na vstupu a následně vytiskne statistiky o tomto textu, konkrétně nás
zajímá počet opakování znaků v textu, tedy počítáme např. počet `a`, `b`, `1`, `2`, ...

Příklady:

* vstup: `andula`, výstup: `a: 2, n:1, d:1, u:1, l:1`
* vstup: `barbora a barbar`, výstup: `b:4, a:5, r:4, o:1`
* vstup: `anakonda`, výstup: `a:3, n:2, k:1, o:1, d:1`

Postup:

1. Nejdříve musíme načíst text pomocí funkce `input()` a uložíme si ho proměnné.
2. Budeme procházet text pomocí `for` cyklu po znaku, budeme zkracovávat každý znak samostatně.
3. Vytvoříme si slovník do kterého si budeme ukládat informace o počtech písmen ve formátu `klíč:hodnota` tedy
   `písmeno:počet`, tedy například `a:2`.
4. V každém kroku `for` cyklu pro aktuální písmenko zkontrolujeme zda písmenko už máme jako klíč ve slovníku pomocí
   podmínky `if pismeno in slovnik`, pokud ano, tak k jeho hodnotě přičteme 1, pokud ne, tak si pro něj vytvoříme záznam
   pomocí `slovnik[pismeno] = 1`.
5. Po průchodu celého vstupního textu vytiskneme statistuku textu a to pomocí `for` cyklu, kterým projdeme dokončený
   slovník. Tedy `for pismeno, pocet in slovnik.items(): print(f"{pismeno}: {pocet}"),`


