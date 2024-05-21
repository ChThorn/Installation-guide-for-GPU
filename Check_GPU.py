import tensorflow as tf # type: ignore

print(tf.__version__)

len(tf.config.list_physical_devices('GPU'))>0
