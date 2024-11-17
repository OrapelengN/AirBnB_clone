#!/usr/bin/python3
"""Unittests for the HBNB console."""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up resources before each test."""
        self.console = HBNBCommand()

    def test_quit_command(self):
        """Test the 'quit' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("quit")
            self.assertEqual(output.getvalue().strip(), '')

    def test_help_command(self):
        """Test the 'help' command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
