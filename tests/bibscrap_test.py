"""Tests for the bibscrap module."""

from bibscrap.app import BibscrapApp
from bibscrap.errors import BibscrapError, BibscrapExtensionTypeError
from gettext import gettext as _
from semver import VersionInfo
from unittest.mock import Mock, patch

import argparse
import bibscrap
import bibscrap.app
import io
import logging
import pytest
import unittest


log = logging.getLogger(__name__)


class BibscrapModuleTest(unittest.TestCase):
    def test_version_is_semver(self):
        try:
            version = VersionInfo.parse(bibscrap.__version__)
        except ValueError as invalid_version_error:
            self.fail(f"bibscrap.__version__: {invalid_version_error!s}")


class BibscrapAppTest(unittest.TestCase):
    def setUp(self):
        self.app = BibscrapApp()

    def test_init(self):
        self.assertIsInstance(self.app, BibscrapApp)

    def test_init_arg_parser(self):
        arg_parser = self.app.arg_parser
        self.assertIsInstance(arg_parser, argparse.ArgumentParser)
        self.assertEqual(arg_parser.prog, _("bibscrap"))

    def test_init_command_parsers(self):
        command_parsers = self.app.command_parsers
        self.assertIsInstance(command_parsers, argparse._SubParsersAction)

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

    @patch("bibscrap.app.builtin_extensions", ["math"])
    def test_load_builtin_extensions(self):
        with self.assertRaises(BibscrapExtensionTypeError):
            self.app.load_builtin_extensions()

    def test_command_invalid_args(self):
        invalid_args = [
            None,
            argparse.Namespace(),
        ]
        for args in invalid_args:
            with self.subTest(args=args), self.assertRaises(BibscrapError):
                self.app.command(args)

    def test_command_valid_args(self):
        mock_command_func = Mock()
        with patch.dict(self.app.commands, {"mock": mock_command_func}, clear=True):
            args = argparse.Namespace(command="mock")
            self.app.command(args)
        mock_command_func.assert_called()
