import unittest

from app import dispatch, paths


class RouteTests(unittest.TestCase):
    def test_unknown_path_returns_none(self):
        self.assertIsNone(dispatch("/definitely-not-routed"))

    def test_paths_is_sorted(self):
        self.assertEqual(paths(), sorted(paths()))


if __name__ == "__main__":
    unittest.main()
