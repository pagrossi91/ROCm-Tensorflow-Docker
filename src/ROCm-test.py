from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model
import tensorflow as tf

import numpy as np
import os
import pickle
import sklearn

# Check ROCm stack and GPU
rocm = tf.test.is_built_with_rocm()
print(rocm)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# Terminal command to watch AMD GPU: watch -n 1 rocm-smi