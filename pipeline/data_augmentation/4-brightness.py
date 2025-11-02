import tensorflow as tf

def change_brightness(image, max_delta):
    """
    Randomly changes the brightness of an image.

    Args:
        image (tf.Tensor): A 3D tensor representing the image to change.
        max_delta (float): The maximum amount the image should be brightened (or darkened).

    Returns:
        tf.Tensor: The altered image.
    """
    return tf.image.random_brightness(image, max_delta)
