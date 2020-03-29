import tensorflow as tf

# Check ROCm stack and GPU
rocm = tf.test.is_built_with_rocm()
print(rocm)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
# Terminal command to watch AMD GPU: watch -n 1 rocm-smi
