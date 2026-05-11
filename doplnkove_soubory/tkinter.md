# Úvod do tvorby GUI aplikací pomocí knihovny Tkinter

Tkinter je standardní knihovna Pythonu pro tvorbu grafického uživatelského rozhraní (GUI). Umožňuje nám vytvářet
klasická okna, která znáte z Windows, Linux nebo macOS. Tkinter vytváří samostatné aplikace s tlačítky, textovými poli a
menu.

## 1. Příprava prostředí

Tkinter je součástí základní instalace Pythonu, takže většinou nemusíte nic instalovat pomocí `pip`. Stačí knihovnu
správně importovat.

```python
import tkinter as tk
from tkinter import messagebox

print("Tkinter is ready to use!")

```

## 2. První okno (Hello World)

Každá aplikace začíná vytvořením hlavního okna (často nazývaného `root`). Aby okno nezmizelo hned po spuštění, musí
běžet tzv. `mainloop` – nekonečná smyčka, která čeká na interakci uživatele (kliknutí, psaní).

```python
import tkinter as tk

root = tk.Tk()
root.title("Hello World App")
root.geometry("400x300")

# Add a text label (Label)

label = tk.Label(root, text="Ahoj světe!", font=("Arial", 14))
label.pack(pady=20)  # Place it in the window with some padding

# Start the application loop

root.mainloop()
```

## 3. Přehled základních prvků (Widgetů)

| Prvek (Widget)                          | Co to dělá                                                   |
|:----------------------------------------|:-------------------------------------------------------------|
| `tk.Tk()`                               | Vytvoří hlavní okno aplikace.                                |
| `tk.Label(text="...")`                  | Zobrazí statický text nebo obrázek.                          |
| `tk.Button(text="...", command=funkce)` | Tlačítko, které po kliknutí spustí zadanou funkci.           |
| `tk.Entry()`                            | Jednořádkové pole pro vstup textu od uživatele.              |
| `tk.Text()`                             | Víceřádkové pole pro delší texty.                            |
| `element.pack()`                        | Správce rozložení (skládá prvky pod sebe nebo vedle sebe).   |
| `element.grid(row=0, col=0)`            | Správce rozložení (umísťuje prvky do tabulky/mřížky).        |
| `element.config(text="...")`            | Umožňuje měnit vlastnosti prvku za běhu (např. změnit text). |
| `element.get()`                         | Získá text, který uživatel napsal do pole `Entry`.           |
| `root.destroy()`                        | Ukončí aplikaci a zavře okno.                                |

## 4. Simulace interakce: Pozdravník

V této ukázce vytvoříme aplikaci, která si vezme jméno od uživatele a po kliknutí na tlačítko ho osobně pozdraví.

```python
import tkinter as tk


def say_hello():
    name = name_entry.get()
    if name:
        output_label.config(text=f"Ahoj, {name}!", fg="green")
    else:
        output_label.config(text="Nezadal jsi jméno!", fg="red")


root = tk.Tk()
root.title("Pozdravník")
root.geometry("300x200")

tk.Label(root, text="Napiš své jméno:").pack(pady=5)

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

greet_button = tk.Button(root, text="Pozdrav mě!", command=say_hello)
greet_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
output_label.pack(pady=10)

root.mainloop()

```

## Úkoly

1. **Počítač kliknutí:** Vytvořte okno s tlačítkem a nápisem. Nápis bude ukazovat číslo 0 a po každém kliknutí na
   tlačítko se číslo o jedna zvýší.
2. **Změna barev:** Vytvořte tři tlačítka (Červená, Zelená, Modrá). Po kliknutí na tlačítko se změní barva pozadí
   hlavního okna na danou barvu (bude se hodit `root.config(bg="color_name")`).
3. **Generátor hesel:** Vytvořte aplikaci s tlačítkem, která po kliknutí vygeneruje náhodné heslo (kombinace písmen a
   čísel) a zobrazí ho v Labelu, uživatel bude moct zadat délku hesla a zda má obsahovat čísla, písmena a speciální
   znaky nebo něco z toho chce vynechat.
4. **GUI sledovač známek:** viz úkoly 9 jen vizuálním uživatelksým rozhraním.
5. **Jednoduchá kalkulačka:** Vytvořte dvě pole `Entry` pro čísla a čtyři tlačítka pro základní operace (+, -, *, /).
   Výsledek zobrazte v Labelu. Nezapomeňte ošetřit dělení nulou, tohle je klasický GUI úkol, každý programátor si jednou
   musí naprogramovat kalkulačku.
6. **Věštkyně:** Vytvořte aplikaci, kam uživatel napíše otázku. Po kliknutí na tlačítko
   aplikace náhodně vybere jednu z odpovědí (např. "Ano", "Ne", "Možná", "Zkus to znovu" či další podle tvého uvážení) a
   zároveň dramaticky změň vizuální podobu aplikace, tedy pro např. "Ano" změň vizuál do zelena, pro "Ne" .
