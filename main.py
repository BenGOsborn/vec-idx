import random
import logging

from index import generate_hash


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

SEED = 1234

VEC_SIZE = 10
DEPTH = 5

def main():
    rand = random.Random(SEED)

    vector = [2 * rand.random() - 1 for _ in range(VEC_SIZE)]

    logger.info(f"vector: {vector}")

    hsh = generate_hash(logger, vector, DEPTH)

if __name__ == "__main__":
    main()