import tensorflow as tf

def shear_image(image, intensity):
    """
    Shears an image horizontally by a specified intensity.

    Args:
        image (tf.Tensor): A 3D tensor representing the image to shear.
        intensity (int): The intensity of the shear.

    Returns:
        tf.Tensor: The sheared image.
    """
    # Convert the image to a float32 tensor
    image = tf.cast(image, tf.float32)
    
    # Define the shear transformation matrix
    shear_matrix = tf.constant([[1.0, 0.0, 0.0],
                                [intensity / 100.0, 1.0, 0.0],
                                [0.0, 0.0, 1.0]], dtype=tf.float32)
    
    # Apply the affine transformation
    sheared_image = tf.raw_ops.ImageProjectiveTransformV2(
        images=tf.expand_dims(image, 0),
        transforms=tf.reshape(shear_matrix, [-1]),
        output_shape=tf.shape(image)[:2],
        interpolation='BILINEAR'
    )
    
    # Remove the batch dimension
    sheared_image = tf.squeeze(sheared_image, 0)
    
    return sheared_image
