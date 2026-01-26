import tensorflow as tf
from tensorflow.keras import layers, models

# načtení dat
(train_data, train_targets), (test_data, test_targets) = tf.keras.datasets.boston_housing.load_data()

# normalizace dat
mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

model = models.Sequential([
    layers.Dense(2, activation='relu', input_shape=(train_data.shape[1],)),
    # Co zde  můžeš měnit pro lepší výsledky:
    # 1. Počet neuronů: Zkus změnit 2 na 32, 64, 128 či více. 
    #    Více neuronů = větší "kapacita mozku".
    # 2. Přidání vrstev: Můžeš pod tento řádek přidat další: layers.Dense(64, activation='relu'),
    #    Více vrstev = model dokáže pochopit složitější tvary.
    layers.Dense(1) 
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

print("\n--- ZAČÍNAM TRÉNOVAT ---")
# Co zde  můžeš měnit pro lepší výsledky:
    # 3. Více epoch: Více epoch znamená že model projde vícekrát data. To znamená 
    # že si data může model lépe "zapamatovat"
model.fit(train_data, train_targets, epochs=10, batch_size=16, verbose=0)

# uložení modelu
nazev_modelu = "house_model.keras"
model.save(nazev_modelu)
print(f"Model byl úspěšně uložen do souboru '{nazev_modelu}'")