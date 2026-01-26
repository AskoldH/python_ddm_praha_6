import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# načtení a normalizace
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
train_images = train_images.astype("float32") / 255
test_images = test_images.astype("float32") / 255

# definice modelu, vytvoření vektoru, vytvoření neuronové sítě 
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)), 
    # Co zde  můžeš měnit pro lepší výsledky:
    # 1. Počet neuronů: Zkus změnit 2 na 32, 64, 128 či více. 
    #    Více neuronů = větší "kapacita mozku".
    # 2. Přidání vrstev: Můžeš pod tento řádek přidat další: layers.Dense(64, activation='relu'),
    #    Více vrstev = model dokáže pochopit složitější tvary.
    layers.Dense(2, activation='relu'),
    layers.Dense(10, activation='softmax') # 10 výstupů (čísla 0-9)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
    
print("\n--- ZAČÍNÁM TRÉNOVAT ---")
# Co zde  můžeš měnit pro lepší výsledky:
    # 3. Více epoch: Více epoch znamená že model projde vícekrát data. To znamená 
    # že si data může model lépe "zapamatovat"
model.fit(train_images, train_labels, epochs=10)

# uložení modelu
nazev_modelu = "muj_model_mnist.keras"
model.save(nazev_modelu)
print(f"Model byl úspěšně uložen do souboru '{nazev_modelu}'")