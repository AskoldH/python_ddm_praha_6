Naprogramujte 3x3 piškvorky, budou proti sobě hrát dva hráči, pole na které chtějí zadat x/o budou vybírat podle sloupce a řádku. Tedy pro usmítění dopřostřed zadám sloupec 2, řádek 2. Hra by měla automaticky detekovat zda někdo vyhrál. Jako rozšíření přidejte větší pole. Hrací pole pro nějaký stav ve hře by mohlo vypadat například:

```
|x|x|o|
|o| | |
| |x| |
```

Jak na to? Pojďme si to rozebrat:

### 1. Příprava herního pole (s listy)

* **Prázdné pole:** Vytvoř si seznam, který obsahuje tři další seznamy. Každý vnitřní seznam bude jeden řádek se třemi mezerami: `pole = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]`.
* **Souřadnice:** Pamatuj, že k prvnímu políčku se dostaneš přes `pole[0][0]`. První číslo v závorce je řádek, druhé je sloupec, pomocí indexů 0-2 pro řádky a sloupce se tedy dostaneš k libovolnému políčku.

### 2. Hlavní herní smyčka (s cyklem `while`)

* **Hra běží, dokud se hraje:** Použij cyklus `while True:`. Ten bude neustále opakovat kroky: vykreslení pole -> update hráče 'x' -> kontrola výhry -> update hráče 'o'.

### 3. Jak vykreslit pole (s cyklem `for`)

* Použij `for radek in pole:` cyklus, který projde tvůj hlavní seznam (hrací pole) a pro každý řádek vypíše jeho obsah. Aby to vypadalo jako v zadání, můžeš použít `print("|" + radek[0] + "|" + radek[1] + "|" + ... )`.

### 4. Tah hráče (Vstup a podmínky)

* Pomocí `input()` se zeptej na řádek a sloupec.
* **Důležitá kontrola:** Než tam hráčův symbol zapíšeš, musíš pomocí `if` zkontrolovat, jestli na tom místě už náhodou není `"x"` nebo `"o"`. Pokud ano, napiš "Obsazeno!" a vypiš že vyhrál druhý hráč protože tento se snažil podvádět.

### 5. Kontrola vítěze (Podmínky)

Tohle bude v programu vypadat jako dlouhý blok `if` a `elif` podmínek pod sebou. Musíš zkontrolovat všechny možnosti, jak vyhrát, těch možností je 8:

* **Kontrola řádků:** Například `if pole[0][0] == pole[0][1] == pole[0][2]` kontroluje 1. řádek (na indexu 0) obsahuje stejné znaky.
* **Kontrola sloupců:** Například `if pole[0][0] == pole[1][0] == pole[2][0]` kontroluje 1. sloupec (na indexu 0) obsahuje stejné znaky.
* **Kontrola diagonál:** Kontrola šikmo z rohů do rohů (celkem dvě možnosti), vymysli jak budou vypadat indexy.
* Pokud je některá podmínka splněná, vypiš vítěze a ukonči hru pomocí příkazu `break`, ten ukončí cyklus a tedy celý program.
* Pozor na možnost kdy jsou v řádku, sloupci nebo diagonále samé mezery, to je počáteční stav, ten tedy nemůžeme značit jako výhru, k podmínkám výše tedy musíme přidat například `and pole[0][0] != " "`.

---

Tohle řešení se dá rozšířit o větší hrací pole, pokud už máš 3x3 verzi tak to zkus!