import tensorflow as tf
import matplotlib.pyplot as plt

# načtení dat, celkem 70 000 obrázků
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# normalizace (převod na čísla 0 až 1)
train_images = train_images.astype("float32") / 255

# zobrazení obrázku z train images
image_to_show = train_images[78] 
plt.imshow(image_to_show, cmap='gray') # jak se má zobrazit
plt.title(f"Číslo na obrázku: {train_labels[0]}") # nastavení nadpisu
plt.colorbar() # ukázání stupnice
nazev_vystupniho_souboru = "vystup.png"
plt.savefig(nazev_vystupniho_souboru) # uložení do souboru

print(f"\n\nObrázek byl uložen do souboru '{nazev_vystupniho_souboru}'.")