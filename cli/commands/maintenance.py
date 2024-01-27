import click
import pathlib

from dotenv import set_key, get_key

from util import ClickUtils


@click.command("maintenance")
@click.option(
    "--status", "-s", is_flag=True,
    help="Returns the current maintenance mode status"
)
def maintenance_mode(status: bool) -> None:
    """Toggle maintenance mode for the site"""

    spinner = ClickUtils.Spinner(
        f"{'Checking' if status else 'Toggling'} maintenance mode..."
    )
    spinner.start()

    # Get the config file path
    config_file_path = (
        pathlib.Path(__file__).parent.parent.parent.absolute() / ".env"
    )

    try:
        # Get the current maintenance mode state
        maintenance_mode_state = get_key(config_file_path, "MAINTENANCE_MODE")
        assert maintenance_mode_state
    except AssertionError:
        spinner.stop()
        click.secho(
            "ERROR: Config file not found or is missing the "
            "`MAINTENANCE_MODE` key value.",
            fg="red",
        )
        exit(1)

    cfg = ClickUtils.Config()
    maintenance_mode_state = cfg.eval_bool_env_var(maintenance_mode_state)

    if status:
        spinner.stop()
        click.secho(
            "Maintenance mode is currently " +
            f"{'enabled' if maintenance_mode_state else 'disabled'}.",
            fg="yellow",
        )
        exit(0)

    # Toggle the maintenance mode state
    if not maintenance_mode_state:
        set_key(config_file_path, "MAINTENANCE_MODE", "True")
    else:
        set_key(config_file_path, "MAINTENANCE_MODE", "False")

    spinner.stop()
    click.secho(
        "Maintenance mode is now " +
        f"{'enabled' if not maintenance_mode_state else 'disabled'}.",
        fg="green",
    )
    click.secho(
        "Please restart the server for the changes to take "
        "effect.", fg="yellow"
    )
