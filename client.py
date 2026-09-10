import math

class DCT2Engine:
    """
    Discrete Cosine Transform Type-II (DCT-II) and Inverse DCT Engine.
    Implements orthogonal energy compaction transforms.
    """
    def dct2(self, x):
        n = len(x)
        res = []
        for k in range(n):
            s = 0.0
            scale = math.sqrt(1.0 / n) if k == 0 else math.sqrt(2.0 / n)
            for i in range(n):
                s += x[i] * math.cos(math.pi * (i + 0.5) * k / n)
            res.append(scale * s)
        return res

    def idct2(self, x):
        n = len(x)
        res = []
        for i in range(n):
            s = 0.0
            for k in range(n):
                scale = math.sqrt(1.0 / n) if k == 0 else math.sqrt(2.0 / n)
                s += scale * x[k] * math.cos(math.pi * (i + 0.5) * k / n)
            res.append(s)
        return res
