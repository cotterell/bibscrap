from bibscrap import BibscrapApp, BibscrapException
from gettext import gettext as _
from unittest.mock import Mock, create_autospec, patch

import argparse
import bibscrap
import io
import logging
import unittest
import pytest


log = logging.getLogger(__name__)


class BibscrapTest(unittest.TestCase):
    def test_bibscrap(self):
        self.assertTrue(True)


class BibscrapAppTest(unittest.TestCase):
    def setUp(self):
        self.app = BibscrapApp()

    def test_init(self):
        self.assertIsInstance(self.app, BibscrapApp)

    def test_init_arg_parser(self):
        arg_parser = self.app.arg_parser
        self.assertIsInstance(arg_parser, argparse.ArgumentParser)
        self.assertEqual(arg_parser.prog, _("bibscrap"))

    def test_init_command_subparsers(self):
        command_subparsers = self.app.command_subparsers
        self.assertIsInstance(command_subparsers, argparse._SubParsersAction)

    def test_init_app_commands_is_empty_dict(self):
        commands = self.app.commands
        self.assertIsInstance(commands, dict)
        self.assertEqual(commands, dict())

    @patch("sys.exit")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_arg_parser_version_stdout(self, mock_stdout, mock_exit):
        self.app.arg_parser.parse_args(["--version"])
        self.assertEqual(
            mock_stdout.getvalue(),
            f"{BibscrapApp.PROG} {BibscrapApp.VERSION}\n",
        )

    @patch("sys.exit")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_arg_parser_version_exit(self, mock_stdout, mock_exit):
        self.app.arg_parser.parse_args(["--version"])
        mock_exit.assert_called()

    @patch("bibscrap.builtin_extensions", ["math"])
    def test_load_builtin_extensions(self):
        with self.assertRaises(BibscrapException):
            self.app.load_builtin_extensions()
