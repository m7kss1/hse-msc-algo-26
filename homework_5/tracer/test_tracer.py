import io
import unittest
from contextlib import redirect_stdout

from tracer import tracer


class TestTracer(unittest.TestCase):
    def test_recursion_and_arguments(self):
        @tracer
        def f(n, *, x=1):
            return x if n == 0 else f(n - 1, x=x) + 1
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(f(1, x=3), 4)
        self.assertEqual(out.getvalue().splitlines(), [
            '-> f(1, x=3)', '  -> f(0, x=3)',
            '  <- f = 3', '<- f = 4',
        ])
        self.assertEqual(f.__name__, 'f')

    def test_exception_restores_depth(self):
        @tracer
        def fail():
            raise ValueError('ошибка')
        @tracer
        def ok():
            return None
        out = io.StringIO()
        with redirect_stdout(out):
            with self.assertRaises(ValueError):
                fail()
            ok()
        self.assertEqual(out.getvalue().splitlines()[-2:],
                         ['-> ok()', '<- ok = None'])
        self.assertIn('!! fail: ValueError: ошибка', out.getvalue())


if __name__ == '__main__':
    unittest.main(verbosity=2)
