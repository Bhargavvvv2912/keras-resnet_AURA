import sys
import os

def validate_resnet():
    print("--- 🏗️ Keras-ResNet Package Integrity Check ---")
    try:
        # Without our shim, this WILL fail in 2026 (Keras 3.0)
        from keras.engine.topology import Layer
        print("SUCCESS: Legacy Keras internal topology found.")
        
        import keras_resnet
        print(f"SUCCESS: Package 'keras_resnet' initialized.")
        return True
    except Exception as e:
        print(f"CRITICAL FAILURE: {type(e).__name__} - {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if validate_resnet() else 1)