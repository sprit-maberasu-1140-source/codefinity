import numpy as np

def relu(x):
    return np.maximum(0, x)

def position_wise_ffn(x, W1, b1, W2, b2):
    # x: (batch_size, seq_len, d_model)
    # W1: (d_model, d_ff)
    # b1: (1, d_ff)
    # W2: (d_ff, d_model)
    # b2: (1, d_model)
    out1 = np.matmul(x, W1) + b1  # (batch_size, seq_len, d_ff)
    out1 = relu(out1)
    out2 = np.matmul(out1, W2) + b2  # (batch_size, seq_len, d_model)
    return out2
