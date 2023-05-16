#!/usr/bin/python3
"""
Module documentation for the utf-8
validation task
"""
#from typing import List


#def validUTF8(data: List[int]) -> bool:
def validUTF8(data) -> bool:
    """
    determines if a given data set represents a valid utf-8 encoding
    """
    num_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
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
            if (byte >> 6) != 0b10:
                return False

        num_bytes -= 1

    return num_bytes == 0
