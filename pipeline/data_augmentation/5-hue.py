import tensorflow as tf

def change_hue(image, delta):
    """
    Changes the hue of an image.

    Args:
        image (tf.Tensor): A 3D tensor representing the image to change.
        delta (float): The amount the hue should change. Must be in the range [-1.0, 1.0].

    Returns:
        tf.Tensor: The altered image.
    """
    return tf.image.adjust_hue(image, delta)
