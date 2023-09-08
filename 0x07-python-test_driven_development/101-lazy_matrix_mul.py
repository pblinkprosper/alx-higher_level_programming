#!/usr/bin/python3
"""Multiplies 2 matrices by using the module NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):

    """Function multiplies two matrices with numpy"""

    return (np.matmul(m_a, m_b))
