Naprogramujte **geometrikcou kalkulačku**, tedy program, co bude obsahovat následující funkce pro jednotlivé útvary:

* Čtverec: `obvod_ctverce(a)`, `obsah_ctverce(a)`
* Obdélník: `obvod_obdelniku(a, b)`, `obsah_obdelniku(a, b)`
* Kruh: `obvod_kruhu(r)`, `obsah_kruhu(r)` (použij $\pi \approx 3.14$)
* Krychle: `delka_hran_krychle(a)`, `povrch_krychle(a)`, `objem_krychle(a)`
* Kvádr: `delka_hran_kvadr(a, b , c)`, `povrch_kvadru(a, b, c)`, `objem_kvadru(a, b, c)`
* Válec: `povrch_valce(r, v)`, `objem_valce(r, v)`
* Koule: `objem_koule(r)`

Pokud neznáte nějaké vzorečky, tak si je jednoduše vyhledejte nebo se zeptejte vaší oblíbené umělé inteligence.

Každá funkce bude vracet jen jedno číslo (vypočtený výsledek) pomocí `return`. 

Nechte uživatele vybrat co chce počítat například pomocí čísel (1 = obvod čtverce, 2 = obsah čtverce, ...) nebo pomocí zkratek (obvč = obvoc čtverce, obsč = obsah čverce, ...). Program neskončí dokud uživatel nezadá místo příkazu co chce počítat slovo `exit`. Tedy bude možné vypočítat obvod čtverce, pak obsah, pak objem kvádru ... 

Ukážeme si i jak naše pomocné funkce na výpočty vložit do samostatného souboru. Na to se podíváme společně.

Práce s programem by mohla vypadat následovně:

```=== GEOMETRICKÁ KALKULAČKA ===
Dostupné tvary:
2D: ctv (Čtverec), obd (Obdélník), kru (Kruh)
3D: kry (Krychle), kva (Kvádr), val (Válec), kou (Koule)
-------------------------------------------------------
Pro ukončení napiš: exit

Co chceš počítat? (zkratka tvaru): kva
Vybral jsi Kvádr. Co chceš zjistit? (h = délka hran, p = povrch, o = objem): o
Zadej stranu a: 5
Zadej stranu b: 4
Zadej stranu c: 10

> Objem kvádru je: 200.0

Co chceš počítat? (zkratka tvaru): kru
Vybral jsi Kruh. Co chceš zjistit? (o = obvod, s = obsah): s
Zadej poloměr r: 3

> Obsah kruhu je: 28.26

Co chceš počítat? (zkratka tvaru): exit
Ukončuji!
```