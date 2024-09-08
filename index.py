from typing import List
import base64
import logging


def generate_hash(logger: logging.Logger, vector: List[str], depth: int) -> str:
    dim = len(vector)
    to_interleave = []

    for i in range(dim):
        l = -1
        h = 1

        out = ""
        scalar = vector[i]

        for _ in range(depth):
            mid = (l + h) / 2

            if scalar > mid:
                out += "1"
                l = mid
            else:
                out += "0"
                h = mid

        to_interleave.append(out)

    logger.debug(f"to_interleave: {to_interleave}")

    b_str = ""
    for i in range(depth):
        for j in range(dim):
            b_str += to_interleave[j][i]

    logger.debug(f"b_str: {b_str}")

    b_int = int(b_str, 2)
    num_bytes = (len(b_str) + 7) // 8

    byte_array = b_int.to_bytes(num_bytes, byteorder="big")

    encoded = base64.b32encode(byte_array).decode("utf-8")

    logger.debug(f"encoded: {encoded}")

    return encoded