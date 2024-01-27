import click
import sys
from flask.cli import with_appcontext
from flask.globals import current_app as app

from util import ClickUtils


@click.command("shell")
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable verbose context output"
)
@click.option(
    "--no-banner",
    "-nb",
    is_flag=True,
    help="Disable the banner message"
)
@with_appcontext
def shell(verbose: bool, no_banner: bool) -> None:
    """Starts an interactive shell with the app context"""

    spinner = ClickUtils.Spinner("Starting interactive shell...")
    spinner.start()

    try:
        from IPython.terminal.ipapp import TerminalIPythonApp
        from IPython import __version__ as ipython_version
    except ImportError:
        spinner.stop()
        click.secho(
            "ERROR: IPython is not installed. Please install it with",
            " `pip install ipython`.",
            fg="red",
        )
        exit(1)

    ctx = app.make_shell_context()

    # Banner message
    cf = ClickUtils.Colors()
    banner = cf.cformat(
        f"{cf.YELLOW}** [Boilerplate Interactive Shell Started] **\n"
        f"{cf.MAGENTA}Boilerplate is ready for your commands! "
        f"Use `exit`/`quit` or use Ctrl + D to quit.\n"
        f"Autocompletion is enabled, press Tab to use it.\n"
    )

    if verbose:
        # Verbose context and shell information output
        banner += cf.cformat(f"\n{cf.CYAN}** [Context Variables] **")
        for key, value in ctx.items():
            banner += cf.cformat(f"\n{cf.YELLOW}* {key} -> {cf.GREEN}{value}")
        banner += (
            f"\n\n{cf.CYAN}** [Shell Information] **"
            f"\n{cf.YELLOW}* Python Version -> {cf.GREEN}v{sys.version}"
            f"\n{cf.YELLOW}* IPython Version -> {cf.GREEN}v{ipython_version}\n"
        )

    ipython_app = TerminalIPythonApp.instance(
        user_ns=ctx,
        display_banner=False
    )
    ipython_app.initialize(argv=[])
    click.clear()

    if not no_banner:
        ipython_app.shell.show_banner(banner)

    spinner.stop()
    ipython_app.start()
