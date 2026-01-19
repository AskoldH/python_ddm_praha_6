import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# načtení modelu
model = load_model('muj_model_mnist.keras')

# načtení a normalizace dat
_, (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
test_images = test_images.astype("float32") / 255

# testování modelu
print("\n--- TESTOVÁNÍ ---")
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"\nPřesnost testování: {test_acc*100:.2f} %")