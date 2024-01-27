import click
import time
import threading
import itertools


class ClickUtils:
    """Utility functions for the click-based CLI"""

    class Spinner:
        def __init__(self, message: str, color: str = "yellow") -> None:
            """A spinner that can be used to indicate that a process is running

            :param message: Message to display next to the spinner
            :param color: Color of the spinner and message (uses colors from
            :func:`click.style`) - Optional (will default to `yellow`)
            """
            self.frames = itertools.cycle([
                "⢿", "⣻", "⣽", "⣾",
                "⣷", "⣯", "⣟", "⡿"
            ])
            self.thread = None
            self.active = False
            self.message = message
            self.color = color

        def start(self) -> None:
            """Starts the spinner animation"""
            if self.thread:
                raise RuntimeError("Spinner is already running")

            self.active = True
            self.thread = threading.Thread(target=self._spin)
            self.thread.start()

        def stop(self) -> None:
            """Stops the spinner animation"""
            if not self.thread:
                raise RuntimeError("Spinner is not running")

            self.active = False
            self.thread.join()

        def _clear(self) -> None:
            """Clears the spinner animation line from the cli"""
            message_length = len(self.message) + 2
            click.secho("\r" + " " * message_length + "\r", nl=False)

        def _spin(self) -> None:
            """Displays the spinner animation with the message"""
            while self.active:
                frame = next(self.frames)
                message = f"\r{frame} {self.message}"
                click.secho(message, fg=self.color, nl=False)
                time.sleep(0.1)
                self._clear()

    class Colors:
        """
        ASNI color codes and formatting
        (where :func:`click.style` cannot be used)
        """

        # Color codes pallet
        RED = "\033[0;31m"
        GREEN = "\033[0;32m"
        YELLOW = "\033[1;33m"
        CYAN = "\033[0;36m"
        MAGENTA = "\033[0;35m"

        # Formatting codes pallet
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        RESET = "\033[0m"  # Reset all colors and formatting

        def cformat(self, text: str) -> str:
            """Formats text with the given styles

            :param text: The text to format
            :param styles: The pallet style(s) to apply to the text
            :return: The formatted text
            """
            return f"{text}{self.RESET}"

    class Config:
        """Config utility methods for the CLI"""

        def eval_bool_env_var(self, env_var: str) -> bool:
            """Evaluates a boolean environment variable

            :param env_var: The environment variable to evaluate
            :return: The evaluated boolean value
            """
            # XXX: python-dotenv doesn't support boolean values nicely,
            # so we have to do it manually
            return True if env_var.lower() in ("true", "t", "1") else False
