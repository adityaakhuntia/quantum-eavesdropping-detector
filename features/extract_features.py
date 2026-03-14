import numpy as np

def extract_qber(alice_bits, bob_bits, alice_bases, bob_bases):
    matched = alice_bases == bob_bases
    errors = np.sum(alice_bits[matched] != bob_bits[matched])
    total = np.sum(matched)

    if total == 0:
        return 0

    return errors / total
