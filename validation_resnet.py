import sys
import os

# --- THE PEACE TREATY ---
try:
    import tensorflow.keras as tf_keras
    sys.modules['keras'] = tf_keras
except ImportError:
    pass

def validate_resnet():
    print("--- 🏗️ Keras-ResNet Package Integrity Check ---")
    try:
        # This path was standard in 2018 but GONE in Keras 3.0
        # Failure: ModuleNotFoundError: No module named 'keras.engine'
        from keras.engine.topology import Layer
        print("SUCCESS: Legacy Keras internal topology found.")
        
        # Verify the 'keras_resnet' package itself is correctly installed
        import keras_resnet
        print(f"SUCCESS: Package 'keras_resnet' version {keras_resnet.__version__} initialized.")
        
        return True
    except Exception as e:
        print(f"CRITICAL FAILURE: {type(e).__name__} - {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if validate_resnet() else 1)