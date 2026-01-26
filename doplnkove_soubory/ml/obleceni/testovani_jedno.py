import tensorflow as tf
import numpy as np

class_names = [
    "Tričko", "Kalhoty", "Svetr", "Šaty", "Kabát",
    "Sandál", "Košile", "Teniska", "Kabelka", "Bota"
]

model = tf.keras.models.load_model("model_fashion.keras")
_, (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
test_images = test_images.astype("float32") / 255

# testování jednoho oblečení
index = 7
predikce = model.predict(test_images[index:index+1])
tip_ai = np.argmax(predikce)

print(f"\nAI si myslí, že na obrázku je: {class_names[tip_ai]}")
print(f"Ve skutečnosti tam je: {class_names[test_labels[index]]}")
