import tensorflow as tf

model = tf.keras.models.load_model("model_fashion.keras")
_, (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()
test_images = test_images.astype("float32") / 255

loss, acc = model.evaluate(test_images, test_labels)
print(f"Přesnost: {acc*100:.2f} %")
