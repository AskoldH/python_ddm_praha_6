import tensorflow as tf

# načtení dat
model = tf.keras.models.load_model('house_model.keras')
(train_data, train_targets), (test_data, test_targets) = tf.keras.datasets.boston_housing.load_data()

# normalizace
mean = train_data.mean(axis=0)
std = train_data.std(axis=0)
test_data_norm = (test_data - mean) / std

mse, mae = model.evaluate(test_data_norm, test_targets, verbose=0)

print(f"\nPrůměrná chyba je: ${mae * 1000:.2f}")
print("Neboli AI je průměrně liší o tolik.")