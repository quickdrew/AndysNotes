## Introduction to 1D Convolutional Neural Networks (CNNs)

### What is a 1D CNN?
A **1D Convolutional Neural Network (CNN)** is a type of deep learning model designed to analyze **sequential or time-series data**. Unlike **2D CNNs**, which process images, **1D CNNs** extract patterns from **1D signals**, such as:

- Sensor readings  
- Audio waveforms  
- Stock market data  

### Why Use a 1D CNN?
✅ **Automatically detects patterns** in sequences  
✅ **Requires less computational power** than RNNs/LSTMs  
✅ **Works well for structured numerical sequences**  

---

## How Does a 1D CNN Work?
A **1D CNN** processes sequential data using **convolutional layers** that apply filters across the input data. This allows the model to **detect local patterns** and relationships.

### Key Components of a 1D CNN
1️⃣ **Convolutional Layers (`Conv1D`)**  
   - Extract patterns from input sequences  
   - Uses **filters (kernels)** to detect features  

2️⃣ **Pooling Layers (`MaxPooling1D`)**  
   - Downsamples the extracted features  
   - Reduces computation and prevents overfitting  

3️⃣ **Flatten Layer (`Flatten`)**  
   - Converts extracted features into a **1D vector** for classification  

4️⃣ **Fully Connected (`Dense`) Layers**  
   - Learns the relationships between extracted features  

5️⃣ **Output Layer**  
   - Produces the final prediction  

---

## Understanding the Windowing Concept
Since sequential data involves **time-dependent relationships**, a **single data point is not enough** to make predictions. Instead, we use a **window of past values** as input.

### What is a Window?
A **window** is a segment of the input sequence containing **multiple past values**. Instead of using one value, the model analyzes **a small section of the sequence** to detect patterns.

### When to Use a Window?
✅ **Use a window when:**

- Data has **sequential dependencies** (e.g., time-series, sensor data, speech signals).
- You need to detect **trends or short-term patterns** over multiple time steps.
- Predictions depend on **recent past values**, not just the current value.

❌ **Do not use a window when:**

- Each data point is **independent** (e.g., static images, tabular data without a time factor).
- There is **no meaningful temporal relationship** between values.
- The model is expected to classify **individual samples**, not patterns over time.

### Example: Windowed Input
If we use a **window size of 5**, our data might look like this:

| Time Step | Input Window | Target |
|-----------|-------------|--------|
| t=1       | [1, 2, 3, 4, 5] | 6 |
| t=2       | [2, 3, 4, 5, 6] | 7 |
| t=3       | [3, 4, 5, 6, 7] | 8 |

✅ **The model learns patterns across the window** instead of treating each value independently.

---

## 1D CNN non-Windowed Example
This example takes in `.csv` EMG sensor data like this:
```
	timestamp	label	emg_value
1	1739915829.7830825	NOISE	4
2	1739915829.7873728	NOISE	3
3	1739915829.7873728	NOISE	13
14885	1739915840.9299445	COLLECTING	2
14886	1739915840.930449	COLLECTING	3
14887	1739915840.930449	COLLECTING	0
```
then proceesses and trains a 1-D CNN to predict, based on EMG data, if a desired movement (collecting) is occuring or not (noise).

**Key points:**

- Increaseing the number of **epochs** increasing training passes and therefore accuracy but requires more training power/time

```python
############################################
# Preprocessing
#
# This model is a basic classification 1D CNN, it predicts based on the one specific memory input (EMG) at a time.
# It does not take in consideration patterns, it is a Memoryless model.
################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import tensorflow as tf  # Deep learning framework
from tensorflow import keras  # Keras API for model building
from tensorflow.keras import layers  # Layers for the neural network
import matplotlib.pyplot as plt  # For visualizing training progress


# Load the dataset
file_path = "emg_data.csv"  # Ensure this file is in your working directory
df = pd.read_csv(file_path)

# Convert categorical labels to numerical values
label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["label"])  # Example: NOISE -> 0, MOVEMENT -> 1 (sorts alphabetically)

# Normalize the EMG values from 0 to 1
scaler = MinMaxScaler()
df["emg_value"] = scaler.fit_transform(df[["emg_value"]])

# Prepare features (X) and labels (y) for training a 1D Convolutional Neural Network (CNN).
X = df["emg_value"].values.reshape(-1, 1, 1)  # df["emg_value"].values: Extracts the EMG signal values from the DataFrame.
                                              # Convolutional Neural Networks (CNNs) expect a 3D input shape for time-series data: (batch_size, time_steps, features)
                                              # -1 → Automatically infers the number of samples
                                              # 1 → Each sample has one time step (since this is a single EMG value per row).
                                              # 1 → There is only one feature per time step (the EMG value)
y = df["label"].values  # Labels (0 or 1) # Extracts the label column as a 1D NumPy array.
                                          # It contains binary classification labels (0 for NOISE, 1 for MOVEMENT).

# Split into train/test sets (80% train, 20% test)
# X, y → The input features (X) and labels (y).
# test_size=0.2 → Reserves 20% of the data for testing.
# random_state=42 → Ensures the same split every time (for reproducibility).
# stratify=y → Ensures that both the training and test sets maintain the same class distribution.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# This prints the number of samples in the training and test sets.
print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}, y_test shape: {y_test.shape}")

# Save the processed dataset (optional, this data is saved in memory within the notebook)
# pd.DataFrame({"emg_value": X_train.flatten(), "label": y_train}).to_csv("train_data.csv", index=False)
# pd.DataFrame({"emg_value": X_test.flatten(), "label": y_test}).to_csv("test_data.csv", index=False)


##########################################################################################
# Define a 1D Convolutional Neural Network (CNN) for binary classification
###########################################################
model = keras.Sequential([
    # First Convolutional Layer
    layers.Conv1D(filters=16, kernel_size=1, activation='relu', input_shape=(1, 1)),
    # Conv1D applies a filter over 1D input (EMG values). Here, we use:
    # - 16 filters (feature detectors)
    # - Kernel size = 1 (since each EMG value is a single point)
    # - ReLU activation function to introduce non-linearity
    # - Input shape = (1, 1), meaning each sample consists of 1 EMG value

    # First Max Pooling Layer
    layers.MaxPooling1D(pool_size=1),
    # MaxPooling downsamples the data, reducing overfitting and computation cost.

    # Second Convolutional Layer
    layers.Conv1D(filters=32, kernel_size=1, activation='relu'),
    # - 32 filters to extract more complex features
    # - Kernel size remains 1 since we are working with single values
    # - ReLU activation again

    # Second Max Pooling Layer
    layers.MaxPooling1D(pool_size=1),
    # Further downsampling the features extracted

    # Flatten Layer
    layers.Flatten(),
    # Converts the 1D feature maps into a single vector for classification.

    # Fully Connected (Dense) Layer
    layers.Dense(64, activation='relu'),
    # - 64 neurons for learning complex patterns in EMG values

    # Dropout Layer (Regularization)
    layers.Dropout(0.5),
    # - Randomly disables 50% of neurons during training to prevent overfitting.

    # Output Layer for Binary Classification
    layers.Dense(1, activation='sigmoid')
    # - 1 neuron output (since we have a binary classification)
    # - Sigmoid activation outputs a probability (0 to 1), which is interpreted as:
    #   - Close to 0 → Likely NOISE
    #   - Close to 1 → Likely MOVEMENT
])

# Compile the model
model.compile(optimizer='adam',  # Adam optimizer for adaptive learning rate
              loss='binary_crossentropy',  # Loss function for binary classification
              metrics=['accuracy'])  # Track accuracy during training

# Display model architecture summary
model.summary()

##########################################################################
####  Train the CNN
##################
# Train the CNN model using training data
history = model.fit(X_train,  # Training features (EMG values)
                    y_train,  # Corresponding labels (0 or 1)
                    epochs=10,  # Number of passes through the dataset
                    batch_size=32,  # Number of samples processed before model updates weights
                    validation_data=(X_test, y_test))  # Evaluate model on test data during training


# Evaluate the trained model on the test dataset
test_loss, test_acc = model.evaluate(X_test, y_test)


##########################################################################
#### Evaluate the Model Performance
#####################################
# Print test accuracy (percentage of correct classifications)
print(f"Test Accuracy: {test_acc:.4f}")


# Plot Training vs Validation Accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')  # X-axis: Epoch number
plt.ylabel('Accuracy')  # Y-axis: Accuracy percentage
plt.legend()  # Show legend
plt.title('CNN Training Accuracy Over Epochs')  # Title of the plot
plt.show()  # Display the plot

# Plot Training vs Validation Loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')  # X-axis: Epoch number
plt.ylabel('Loss')  # Y-axis: Loss value
plt.title('CNN Training Loss Over Epochs')  # Title of the plot
plt.show()  # Display the plot

```

---

## 1D CNN Windowed Example
This example processes the same data as the non-windowed example above, see the example for details.

**Key points:**

- Changing `time_steps = XX` changes how many previous EMG values to use.

```python
# To pick up on signal patterns of sampled data, this model
# processes a window (sequence) of EMG values instead of just one at a time.

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

#######################################################################
# Load and Preprocess the Data
####################################
# Load the dataset
file_path = "emg_data.csv"  # Ensure this file is in your working directory
df = pd.read_csv(file_path)

# Convert categorical labels to numerical values
label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["label"])  # NOISE → 0, MOVEMENT → 1

# Normalize the EMG values from 0 to 1
scaler = MinMaxScaler()
df["emg_value"] = scaler.fit_transform(df[["emg_value"]])

# Convert data to NumPy arrays
X = df["emg_value"].values
y = df["label"].values  # Labels (0 or 1)

#######################################################################
# Reshape Data to Include a Sequence of EMG Values
####################################

# Define how many previous EMG values to use in each input window
time_steps = 50  # Instead of using 1 EMG value, use a sequence of 10

# Create sequences of EMG values
X_seq = np.array([X[i:i+time_steps] for i in range(len(X) - time_steps)])
y_seq = y[time_steps:]  # Align labels with the sequences

# Reshape X_seq to fit CNN input requirements (samples, time_steps, features)
X_seq = X_seq.reshape(X_seq.shape[0], time_steps, 1)

# Split into training and testing sets again
X_train, X_test, y_train, y_test = train_test_split(X_seq, y_seq, test_size=0.2, random_state=42, stratify=y_seq)

# Print new shapes
print(f"X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")

#############################################################
# Develop CNN Architecture to Process Sequences
###############################
model = keras.Sequential([
    # First Convolutional Layer - Detects patterns in time series data
    layers.Conv1D(filters=32, kernel_size=3, activation='relu', input_shape=(time_steps, 1)),
    layers.MaxPooling1D(pool_size=2),

    # Second Convolutional Layer - Captures more complex patterns
    layers.Conv1D(filters=64, kernel_size=3, activation='relu'),
    layers.MaxPooling1D(pool_size=2),

    # Flatten the 1D feature maps into a vector for classification
    layers.Flatten(),

    # Fully Connected Layer for decision making
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),

    # Output Layer (Binary Classification)
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Print model summary
model.summary()

################################################################
# Train the CNN Model
#######################
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

################################################################
# Evaluate the Model
#######################
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")

################################################################
# Visualize Training Performance
#######################
# Plot Training vs Validation Accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.title('CNN Training Accuracy Over Epochs')
plt.show()

# Plot Training vs Validation Loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('CNN Training Loss Over Epochs')
plt.show()


```
---

## Final Thoughts
1D CNNs are **powerful tools for analyzing sequential data**. They efficiently capture **patterns over time** using convolutional layers, making them useful for **signal processing, forecasting, and classification tasks**.

Would you like to explore **CNN + LSTM models** for even better sequence learning? 🚀
