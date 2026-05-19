# Hardware

Zde je úkol na procvičení poznávání hardwaru s tím, že si něco i naprogramujeme u toho.

## 1 - Co hardware dělá?

Vytvořte konzolovou aplikaci, kde uživatel zadá číslo a podle tohoto čísla se mu zobrazí co to je za součástku počítače
a k čemu slouží. To jaké číslo patří k jaké součástce bude stanoveno rozložením součástek které máte poznat po učebně.

Postup by mohl vypadat následovně:

* Vytvoříme si nekonečnou smyčku pomocí `while True:`
* V nekonečé smyčce nejdříve načteme si od uživatele číslo pomocí funkce `int(input())` a uložíme si ho do proměnné
  `cislo`
* Pomocí tohoto čísla se rozhodneme v šesti `if-else` větvých, ve větvých podmínek. Podmínka bude vypadat např. jako:
  `if cislo == 1:`, v tomto případě uživatel zvolil číslo 1 a vytiskneme na obrazovku jednoduše pomocí funkce `print()`
  informace o součástce číslo 1, tyto informace zkuste vymyslet sami, vůbec nevadí když tam budete mít nějakou
  nepřesnost, vše si projdeme a vyladíme. Takto bude podmínka vypadat i pro zbylých 5 čísel tedy 5 součástek.
* Také musíme mít podmínku pro ukončení opakování cyklu, pro ukončení musí uživatel zadat číslo 0, tedy podmínka bude
  `if cislo == 0:`, poté ukončíme cykluse pomocí `break` nebo celou aplikaci pomocí `exit()` (záleží jestli chete
  tisknout rozlučkovou zprávu na konci).