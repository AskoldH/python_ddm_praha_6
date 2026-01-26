import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# načtení modelu
model = load_model('muj_model_mnist.keras')

# načtení a normalizace dat
_, (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
test_images = test_images.astype("float32") / 255

# testování jednoho čísla
index = 80
predikce = model.predict(test_images[index:index+1])
tip_ai = np.argmax(predikce)
skutecnost = test_labels[index]

print(f"\nAI si myslí, že na obrázku je: {tip_ai}")
print(f"Ve skutečnosti tam je: {skutecnost}")