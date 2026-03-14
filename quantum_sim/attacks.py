import numpy as np

def intercept_resend(alice_bits, alice_bases):
    eve_bases = np.random.randint(0, 2, len(alice_bits))
    eve_bits = []

    for i in range(len(alice_bits)):
        if eve_bases[i] == alice_bases[i]:
            eve_bits.append(alice_bits[i])
        else:
            eve_bits.append(np.random.randint(0, 2))

    return np.array(eve_bits), eve_bases
