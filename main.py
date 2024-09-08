import random
import logging

from index import generate_hash


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SEED = 1234
VEC_SIZE = 1536
NUM_VEC = 100

DEPTH = 5

def main():
    rand = random.Random(SEED)

    vectors = [[2 * rand.random() - 1 for _ in range(VEC_SIZE)] for _ in range(NUM_VEC)]

    for vector in vectors:
        logger.debug(f"vector: {vector}")

        hsh = generate_hash(logger, vector, DEPTH)

        logger.info(f"out vector hash: {hsh}\n")

if __name__ == "__main__":
    main()