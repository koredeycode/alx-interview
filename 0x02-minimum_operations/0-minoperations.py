#!/usr/bin/python3
"""Module documentation"""


class opClass:
    """
    Opclass implementations
    """
    def __init__(self):
        self.count = 1
        self.ops = 0
        self.clipboard = 0

    def copy(self):
        """
        the copy function
        """
        self.clipboard = self.count
        self.ops += 1

    def paste(self):
        """
        the paste function
        """
        self.count += self.clipboard
        self.ops += 1

    def __str__(self):
        """
        string function
        """
        return "H" * self.count

    def clear(self):
        """
        restart the instance
        """
        self.__init__()

    def minOperations(self, n):
        """
        find the minimum operation
        """
        if not isinstance(n, int) or n < 1:
            return 0

        self.clear()

        while self.count < n:
            if self.clipboard == 0:
                self.copy()
                self.paste()
            elif n - self.count > 0 and (n - self.count) % self.count == 0:
                self.copy()
                self.paste()
            elif self.clipboard > 0:
                self.paste()
        return self.ops


def minOperations(n: int) -> int:
    """
    find the minimum operations
    """
    c = opClass()
    return c.minOperations(n)
