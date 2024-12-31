import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, Concatenate

def build_and_train_model(X_train_spatial, X_train_omics, y_train, X_test_spatial, X_test_omics, y_test, output_filepath):
    input_shape = X_train_spatial.shape[1:]
    input_layer = Input(shape=input_shape)
    
    # Convolutional layers
    conv1 = Conv2D(32, kernel_size=(3, 3), activation='relu')(input_layer)
    conv2 = Conv2D(64, kernel_size=(3, 3), activation='relu')(conv1)
    flatten = Flatten()(conv2)
    
    # Additional omics input
    other_omics_input = Input(shape=(X_train_omics.shape[1],))
    combined = Concatenate()([flatten, other_omics_input])
    
    # Fully connected layers
    fc1 = Dense(128, activation='relu')(combined)
    output = Dense(1, activation='sigmoid')(fc1)
    
    model = tf.keras.models.Model(inputs=[input_layer, other_omics_input], outputs=output)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    # Train the model
    model.fit([X_train_spatial, X_train_omics], y_train, epochs=50, batch_size=32, validation_data=([X_test_spatial, X_test_omics], y_test))
    
    # Save the model
    model.save(output_filepath)

if __name__ == "__main__":
    import numpy as np
    
    # Dummy data for illustration; replace with actual data loading code
    X_train_spatial = np.random.rand(100, 64, 64, 1)
    X_train_omics = np.random.rand(100, 50)
    y_train = np.random.randint(2, size=100)
    X_test_spatial = np.random.rand(20, 64, 64, 1)
    X_test_omics = np.random.rand(20, 50)
    y_test = np.random.randint(2, size=20)
    
    build_and_train_model(X_train_spatial, X_train_omics, y_train, X_test_spatial, X_test_omics, y_test, "results/model/optimized_model.h5")
