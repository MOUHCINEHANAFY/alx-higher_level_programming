#!/usr/bin/python3
"""numpy function"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplication with numpy.

    Args:
        m_a (ints/floats): First matrix.
        m_b (ints/floats): Fecond matrix.
    """

    return (np.matmul(m_a, m_b))
