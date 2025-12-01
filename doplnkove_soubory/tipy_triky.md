1. For na jeden řádek: 
    ```python 
    mocniny = [x**2 for x in range(10)]
    ```

2. Podmínka ve for cyklu na jeden řádek:
    ```python
    mocniny_sudych = [x**2 for x in range(10) if x % 2 == 0]
    ```

3. Ternární operátor neboli jednořádkový if:
    ```python
    is_adult = True

    status = "dospělý" if is_adult else "nezletilý"
    ```

4. Přiřazení více hodnot na jendom řádku:
    ``` 
    a, b, c = 1, 2, 3
    ```

5. Získání indexu i položky pomocí enumarate:
    ```python 
    names = ["Alice", "Bob", "Charlie"]

    for index, name in enumerate(names):
        print(f"Index {index}: {name}")
    ```

6. Průchod více seznamy najednou pomocí zip:
    ```python  
    names = ["Alice", "Bob"]
    ages = [25, 30]

    for name, age in zip(names, ages):
        print(f"{name} je starý {age} let.")
    ```

7. Získání defaultní hodnoty pokud není daná položka v dictionary:
    ```python
    data = {"name": "Jana", "age": 30}

    city = data.get("city", "Neznámé")
    name = data.get("name", "Neznáme")
    ```

8. Používání f-stringů:
    ```python
    name = "Karel"
    age = 42
    message = f"{name} má {age} let."
    ```

9. Kontrola zda je list prázdný:
    ```python
    list_1 = [1, 2]
    list_2 = []

    if list_1:
        print("Seznam není prázdný")
    else:
        print("Seznam je prázdný")
    
    if not list_2:
        print("Seznam je prázdný")
    ```

10. Spojování řetězců pomocí .join:
    ```python
    words = ["Ahoj", "svět", "z", "Pythonu"]

    sentence = " ".join(words)
    print(sentence)

    # nebo třeba

    csv_data = ",".join(["1", "2", "3"])
    print(csv_data)
    ```

11. Používání _:
    ```python
    user_info = ("Anna", 28, "Česko")

    name, _, country = user_info # nepotřebujeme věk
    ```

12. Kontrola podmínky pro všechny prvky seznamu pomocí all/any:
    ```python
    numbers = [1, 2, 3, 4]

    # existuje v listu číslo větší než 3? Výsledkem je True/False
    has_big_number = any(n > 3 for n in numbers)

    # jsou všechan čísla menší než 5? Výsledkem je True/False
    all_small = all(n < 5 for n in numbers)
    ```

13. Odstranění duplicitních položek v listu pomocí set (množiny):
    ```python
    data = [1, 2, 2, 3, 1, 4]

    unique_data = list(set(data))
    print(unique_data)
    ```

14. Slicing listů:
    r

15. Zjištění co je proměnná za datový typ:
    ```python
    x = 10

    if isinstance(x, int):
        print("x je celé číslo")

    y = "text"
    if isinstance(y, (str, list)):
        print("y je string nebo seznam")
    ```

## Úkoly k procvičení slicing listů
Mějme list:
```python
list_1 = list(range(100))
```

1. Prvních 10 prvků: Vytvořte seznam result_1, který obsahuje prvních 10 prvků ze seznamu list_1 (hodnoty 0 až 9).

2. Posledních 5 prvků: Vytvořte seznam result_2, který obsahuje posledních 5 prvků ze seznamu list_1 (hodnoty 95 až 99).

3. Sudá čísla: Vytvořte seznam result_3, který obsahuje všechna sudá čísla z celého seznamu my_list (0, 2, 4, ...).

4. Liché čísla: Vytvořte seznam result_4, který obsahuje všechna lichá čísla z celého seznamu my_list (1, 3, 5, ...).

5. Prvky od 20 do 30 (včetně): Vytvořte seznam result_5, který obsahuje prvky s hodnotami 20, 21, ..., 30 (včetně obou mezních hodnot).

6. Hodnota prvku na indexu 42: Vypište hodnotu prvku, který se nachází na indexu 42 v seznamu my_list.

7. Obrácený seznam: Vytvořte seznam result_7, který je kompletně obrácenou kopií seznamu my_list (tj. začíná 99 a končí 0).

8. Prvky od 90 do 80 (klesající): Vytvořte seznam result_8, který začíná číslem 90 a končí číslem 80 a je v klesajícím pořadí (90, 89, 88, ..., 80).

9. Každý 10. prvek od 5: Vytvořte seznam result_9, který začíná prvkem s hodnotou 5 a obsahuje každý desátý prvek poté (5, 15, 25, 35, ...).

10. Bez prvních 5 a posledních 5 prvků: Vytvořte seznam result_10, který obsahuje všechny prvky kromě prvních 5 a posledních 5 ze seznamu my_list.