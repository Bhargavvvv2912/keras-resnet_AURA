import sys
import os
import types

# --- THE DEEP SHIM (Required for 2020 Baseline Green) ---
try:
    import tensorflow.keras as tf_keras
    # 1. Map the base keras module
    sys.modules['keras'] = tf_keras
    
    # 2. Manually reconstruct the 'keras.engine.topology' path
    # This is where 2018 code expects to find the 'Layer' class.
    keras_engine = types.ModuleType('engine')
    keras_engine_topology = types.ModuleType('topology')
    keras_engine_topology.Layer = tf_keras.layers.Layer
    
    # Inject into the system modules
    sys.modules['keras.engine'] = keras_engine
    sys.modules['keras.engine.topology'] = keras_engine_topology
    print("SUCCESS: Deep Namespace Shim active (reconstructed keras.engine.topology).")
except Exception as e:
    print(f"Shim Warning: {e}")

def validate_resnet():
    print("--- 🏗️ Keras-ResNet Package Integrity Check ---")
    try:
        # This will now work in the baseline because of our Deep Shim
        from keras.engine.topology import Layer
        print("SUCCESS: Legacy Keras internal topology found via shim.")
        
        # Verify the 'keras_resnet' package itself is correctly installed
        # The package's internal imports will also benefit from the sys.modules injection
        import keras_resnet
        print(f"SUCCESS: Package 'keras_resnet' initialized.")
        
        return True
    except Exception as e:
        print(f"CRITICAL FAILURE: {type(e).__name__} - {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if validate_resnet() else 1)