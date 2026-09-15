import unittest

from prime import count_primes


def is_prime_naive(x: int) -> bool:
    if x < 2:
        return False
    return all(x % d != 0 for d in range(2, int(x**0.5) + 1))


class TestCountPrimes(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_primes(10), 4)
        self.assertEqual(count_primes(1), 0)

    def test_borders(self):
        self.assertEqual(count_primes(0), 0)
        self.assertEqual(count_primes(2), 0)
        self.assertEqual(count_primes(3), 1)
        self.assertEqual(count_primes(4), 2)

    def test_known_values(self):
        self.assertEqual(count_primes(100), 25)
        self.assertEqual(count_primes(1000), 168)
        self.assertEqual(count_primes(10**6), 78498)

    def test_against_naive(self):
        for n in range(200):
            expected = sum(1 for x in range(n) if is_prime_naive(x))
            self.assertEqual(count_primes(n), expected, n)


if __name__ == "__main__":
    unittest.main(verbosity=2)
