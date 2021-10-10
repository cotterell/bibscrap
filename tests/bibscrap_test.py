from unittest.mock import patch

import bibscrap
import unittest
import pytest


class BibscrapTest(unittest.TestCase):
    def test_bibscrap(self):
        self.assertTrue(True)


class BibscrapAppTest(unittest.TestCase):
    @patch("bibscrap.builtin_extensions", ["math"])
    def test_load_builtin_extensions(self):
        with self.assertRaises(bibscrap.BibscrapException):
            app = bibscrap.BibscrapApp()
            app.load_builtin_extensions()
