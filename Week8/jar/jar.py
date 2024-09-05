class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
         if not isinstance(n, int) or n <= 0:
            raise ValueError("Invalid number of cookies to deposit.")
         if self.cookies + n > self._capacity:
            raise ValueError("Jar capacity exceeded.")
         self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Invalid number of cookies to withdraw.")
        if self.cookies < n:
            raise ValueError("Not enough cookies in the jar.")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
