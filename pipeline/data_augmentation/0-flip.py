import tensorflow as tf

def flip_image(image):
    """
    Flips an image horizontally.

    Args:
        image (tf.Tensor): A 3D tensor representing the image to flip.

    Returns:
        tf.Tensor: The horizontally flipped image.
    """
    return tf.reverse(image, axis=[1])
