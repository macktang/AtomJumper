import unittest



class TestPlayer(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_velocity_increase(self):
        """Does velocity increase work?"""
        b = vec(0,0)
        physics.updateVelocity(b,1,1)
        self.assertTrue(b.x == 1)
        self.assertTrue(b.y == 1)

if __name__ == '__main__':
    unittest.main()