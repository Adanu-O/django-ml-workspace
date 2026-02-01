def inner_product(v1, v2):
    """
    Computes the inner (dot) product of two vectors.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same length")

    return sum(a * b for a, b in zip(v1, v2))
