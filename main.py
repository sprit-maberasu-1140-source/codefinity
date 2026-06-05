class MultiHeadAttention:
    def __init__(self, hidden_dim):
        self.hidden_dim = hidden_dim
    def __call__(self, x):
        # Dummy self-attention: just returns input for demonstration
        return x

class FeedForward:
    def __init__(self, hidden_dim):
        self.hidden_dim = hidden_dim
    def __call__(self, x):
        # Dummy feed-forward: just returns input for demonstration
        return x

class TransformerEncoderBlock:
    def __init__(self, hidden_dim):
        # Initializing the self-attention layer
        self.attention = MultiHeadAttention(hidden_dim)
        
        # Initializing the feed-forward network
        self.ffn = FeedForward(hidden_dim)

    def forward(self, x):
        # Applying self-attention
        attn_output = self.attention(x)
        
        # Processing through the feed-forward network
        output = self.ffn(attn_output)
        
        return output
