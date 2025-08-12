from fractions import Fraction
from math import gcd
from functools import reduce
import sys
import time
from argparse import ZERO_OR_MORE


MOD = 998244353     # Classic NTT-friendly prime: supports large 2^k roots (n | q-1).  See §3.4.
PRIM_ROOT = 3       # A primitive generator for the needed roots mod MOD (standard choice).

def ntt(a, invert):
    n = len(a)

    # --- Bit-reversal permutation (NO -> BO). §4.4 definition & examples.
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    # --- Iterative CT butterfly stages. §4.1: decimation and staged butterflies.
    length = 2
    while length <= n:
        # Twiddle factor for this stage: ω^{(q-1)/length}. Requires n | (q-1). §3.4 Thm. 3.1.
        wlen = pow(PRIM_ROOT, (MOD - 1) // length, MOD)
        if invert:
            # Use inverse twiddle for INTT. (Multiply by w^{-1} per butterfly.)
            wlen = pow(wlen, MOD - 2, MOD)
        for i in range(0, n, length):
            w = 1
            half = length // 2
            for j in range(i, i + half):
                u = a[j]
                v = (a[j + half] * w) % MOD
                a[j] = (u + v) % MOD
                a[j + half] = (u - v) % MOD
                w = (w * wlen) % MOD
        length <<= 1

    if invert:
        # Final scaling by n^{-1} to complete the INTT (see GS examples: divide by n).
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = (a[i] * inv_n) % MOD

def convolution(a, b):
    """
    Linear convolution via NTT:
      - Zero-pad to length >= len(a)+len(b)-1 so the cyclic convolution equals the
        linear one (standard FFT/NTT trick). §2.1 (linear conv), §3.2.3 (NTT conv).
      - Apply NTT(a), NTT(b), point-wise multiply, INTT => a * b. Prop. 3.1.
    """
    # Find closest power of 2 >= to the combined length of a and b
    n = 1
    need = len(a) + len(b) - 1
    while n < need:
        n <<= 1
    # print(f"closest power of 2: {n}")

    fa = a[:] + [0] * (n - len(a))
    fb = b[:] + [0] * (n - len(b))
    # print(f"zero-padded a: {fa}")
    # print(f"zero-padded b: {fb}")

    # print(f"fa before ntt: {fa}")
    ntt(fa, False)   # CT forward: NO->BO.
    # print(f"fa after ntt: {fa}")
    # print(f"fb before ntt: {fa}")
    ntt(fb, False)
    # print(f"fb after ntt: {fb}")
    for i in range(n):
        # Convolution theorem: element-wise multiply in transform domain. Prop. 3.1.
        fa[i] = (fa[i] * fb[i]) % MOD
    ntt(fa, True)    # Inverse transform back to time/coef domain (apply 1/n).

    res = fa[:need]
    return [int(x) for x in res]  # Exact for our sizes; we stay < MOD.

def deconvolve_series(S, C):
    """
    Solve the lower-triangular Toeplitz system for Q in:  C * Q = S,
    where C[0] > 0 and '*' is linear convolution (power-series multiplication).
    This is the forward-substitution formula:
        Q[k] = (S[k] - sum_{i=1..k} C[i]*Q[k-i]) / C[0]
    We keep exact rationals (Fraction) here.

    Note: This step is O(n^2). To make the WHOLE pipeline O(n log n), one would
    compute R = C^{-1} mod x^L by Newton iteration (each iteration uses NTT
    convolutions) and then set Q = S * R. The NTT paper provides the fast
    multiplication building block (CT/GS + convolution theorem); Newton itself
    is a standard power-series trick outside the paper’s scope. See §4 for the
    O(n log n) multiplications we’d reuse.
    """
    L = len(S)
    Q = [Fraction(0, 1) for _ in range(L)]
    c0 = C[0]
    for k in range(L):
        acc = 0
        jmax = min(k, len(C) - 1)
        for i in range(1, jmax + 1):
            acc += C[i] * Q[k - i]
        Q[k] = Fraction(S[k] - acc, c0)
    return Q

def minimal_integer_poly_from_rational(Q):
    """
    Convert rational-coefficient series Q to the *primitive* integer polynomial D:
      1) Multiply by the lcm of denominators,
      2) Divide all coefficients by gcd (content) to minimize.
    The Kattis statement guarantees existence and uniqueness of the answer; this
    produces the minimal-integer solution consistent with that guarantee.
    """
    den = 1
    for q in Q:
        den = (den * q.denominator) // gcd(den, q.denominator)

    D0 = [int(q * den) for q in Q]
    # Trim trailing zeros (defensive; not expected).
    while D0 and D0[-1] == 0:
        D0.pop()
    if not D0:
        return [0], 1

    g = 0
    for x in D0:
        g = gcd(g, abs(x))
    D = [x // g for x in D0]
    scale = den // g
    return D, scale

def solve_io(data: str) -> str:
    t0 = time.perf_counter()
    nA, nB, nC = map(int, data.splitlines()[0].split())
    A, B, C = [list(map(int, line.split())) for line in data.splitlines()[1:]]
    # t1 = time.perf_counter(); print(f"{(t1 - t0) * 1e6:.6f} us for parsing input part 1")
    # print("Parsed input:")
    # print(f"nA: {nA} nB: {nB} nC: {nC}")
    # print(f"A: {A}")
    # print(f"B: {B}")
    # print(f"C: {C}")

    t0 = time.perf_counter()
    amin, bmin, cmin = min(A), min(B), min(C)
    amax, bmax, cmax = max(A), max(B), max(C)

    # I am too stupid to understand this
    # TODO: Ask simon why its ok to convert to zero-indexed,
    # like there is no guarantee that each polynomial is shifted by the same amount
    A_hist = [0] * (amax - amin + 1)
    B_hist = [0] * (bmax - bmin + 1)
    C_hist = [0] * (cmax - cmin + 1)
    for v in A: A_hist[v - amin] += 1
    for v in B: B_hist[v - bmin] += 1
    for v in C: C_hist[v - cmin] += 1
    # t1 = time.perf_counter(); print(f"{(t1 - t0) * 1e6:.6f} us for processing A,B,C")
    # print(f"A: {A_hist}")
    # print(f"B: {B_hist}")
    # print(f"C: {C_hist}")


    # Fast linear convolution S = A * B via NTT (zero-padded, then NTT-ptwise-INTT).
    S = convolution(A_hist, B_hist)

    # Deconvolution C' * Q = S (rational series).
    Q = deconvolve_series(S, C_hist)

    # Minimal integer die from Q.
    D, _scale = minimal_integer_poly_from_rational(Q)

    # Convert back from shifted index k to actual face value (d_min + k).
    dmin = (amin + bmin) - cmin
    faces = []
    for idx, coeff in enumerate(D):
        if coeff > 0:
            faces.extend([dmin + idx] * coeff)
    faces.sort()

    # Output format per Kattis statement.
    out = []
    out.append(str(len(faces)))
    out.append(" ".join(map(str, faces)) if faces else "")
    return "\n".join(out)

if __name__ == "__main__":
    data = sys.stdin.read()
    print(solve_io(data))
