import random
import time
from secret import FLAG

seed = str(round(time.time()))
random.seed(seed)

key = []
for i in range(len(FLAG)):
	key.append(random.randrange(256))

ct = [m ^ k for m, k in zip(FLAG + seed.encode(), key + [ord("a")] * len(seed))]

with open("ciphertext.txt", "w") as f:
    f.write(bytes(ct).hex())
