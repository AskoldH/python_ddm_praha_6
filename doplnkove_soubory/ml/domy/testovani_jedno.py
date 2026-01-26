import tensorflow as tf
import numpy as np

# načtení dat
model = tf.keras.models.load_model('house_model.keras')
(train_data, train_targets), (test_data, test_targets) = tf.keras.datasets.boston_housing.load_data()

# normalizace
mean = train_data.mean(axis=0)
std = train_data.std(axis=0)
test_data_norm = (test_data - mean) / std

# predikce
index = 10
dum_na_test = test_data_norm[index:index+1]
predikce = model.predict(dum_na_test)

print(f"\nAI předpověděla: ${predikce[0][0] * 1000:.0f}")
print(f"Skutečná cena je: ${test_targets[index] * 1000:.0f}")