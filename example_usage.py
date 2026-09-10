from client import DCT2Engine

def main():
    print("=== Testing DCT-II JPEG Compression Engine ===")
    dct = DCT2Engine()
    vals = [10.0, 20.0, 30.0, 40.0]
    coeffs = dct.dct2(vals)
    print("DCT coefficients:", [round(c, 3) for c in coeffs])
    inv = dct.idct2(coeffs)
    print("IDCT reconstructed:", [round(v, 3) for v in inv])

    for orig, v in zip(vals, inv):
        assert abs(orig - v) < 1e-6
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
