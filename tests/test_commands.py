"""
Module containing tests for the commands and functionality of the 'app' module.
"""

import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand


def test_greet_command(capfd):
    """
    Test the GreetCommand class.
    """
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"


def test_goodbye_command(capfd):
    """
    Test the GoodbyeCommand class.
    """
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"


def test_app_greet_command(capfd, monkeypatch):
    """
    Test the greet command in the App class.
    """
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()  # Assuming App.start() is now a static method based on previous discussions

    assert str(e.value) == "Exiting...", "The app did not exit as expected"
