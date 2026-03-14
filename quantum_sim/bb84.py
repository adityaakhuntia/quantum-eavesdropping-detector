import random

def bb84_simulation(eavesdrop=False):

    n = 100

    a_bits = [random.randint(0,1) for _ in range(n)]
    a_bases = [random.randint(0,1) for _ in range(n)]

    b_bases = [random.randint(0,1) for _ in range(n)]

    b_bits = []

    for i in range(n):

        if a_bases[i] == b_bases[i]:
            bit = a_bits[i]
        else:
            bit = random.randint(0,1)

        if eavesdrop:
            if random.random() < 0.25:
                bit = 1-bit

        b_bits.append(bit)

    return a_bits, a_bases, b_bases, b_bits