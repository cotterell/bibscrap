"""Tests for the bibscrap module."""

from bibscrap.cli.app import Application
from unittest.mock import Mock, patch

import logging
import unittest


log = logging.getLogger(__name__)


class BibscrapAppTest(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_init(self):
        self.assertIsInstance(self.app, Application)
