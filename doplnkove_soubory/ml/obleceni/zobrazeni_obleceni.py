import tensorflow as tf
import matplotlib.pyplot as plt

class_names = [
    "Tričko", "Kalhoty", "Svetr", "Šaty", "Kabát",
    "Sandál", "Košile", "Teniska", "Kabelka", "Bota"
]

# načtení dat
(train_images, train_labels), _ = tf.keras.datasets.fashion_mnist.load_data()
train_images = train_images.astype("float32") / 255

index_to_show = 42
plt.imshow(train_images[index_to_show], cmap="gray")
plt.title(f"Předmět: {class_names[train_labels[index_to_show]]}")
plt.axis("off")
plt.savefig("vystup_obleceni.png")
