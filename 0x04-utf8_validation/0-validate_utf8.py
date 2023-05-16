#!/usr/bin/python3
"""
module documentation for the utf-8 validation task
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    determines if a given data set represents a valid utf-8 encoding
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # Check the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes for the next character
            if (byte >> 7) == 0b0:
                num_bytes = 1
            elif (byte >> 5) == 0b110:
                num_bytes = 2
            elif (byte >> 4) == 0b1110:
                num_bytes = 3
            elif (byte >> 3) == 0b11110:
                num_bytes = 4
            else:
                return False
        else:
            # Check if the byte starts with the continuation pattern "10"
            if (byte >> 6) != 0b10:
                return False

        num_bytes -= 1

    # If there are remaining bytes, it means the data is incomplete
    return num_bytes == 0
