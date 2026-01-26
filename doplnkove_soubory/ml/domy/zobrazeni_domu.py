import tensorflow as tf
import matplotlib.pyplot as plt

# načtení dat
(train_data, train_targets), (test_data, test_targets) = tf.keras.datasets.boston_housing.load_data()

rooms = train_data[:, 5] 
prices = train_targets

plt.scatter(rooms, prices, alpha=0.7)
plt.xlabel("Průměrný počet pokojů")
plt.ylabel("Cena (v tisícovkách dolarů)")
plt.title("Vztah počet pokojů-cena")
plt.grid(True)

output_file = "house_data.png"
plt.savefig(output_file)
print(f"Graf uložen do '{output_file}'")