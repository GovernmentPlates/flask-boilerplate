import click
import time


@click.command("boil")
@click.option(
    "temperature",
    "-t",
    type=click.IntRange(min=23, max=200, clamp=True),
    default=100,
    help="The temperature to heat the water to",
)
def boil(temperature: int) -> None:
    """Heats water to a specified temperature (an example command)"""

    boil_time = (1 * 4.186 * (temperature - 23)) / 1
    click.secho(f"Boiling water to {temperature}°C...", fg="yellow")

    with click.progressbar(range(int(boil_time)), label="Progress:") as bar:
        for i in bar:
            time.sleep(1)

    click.secho(f"Water has now been heated to {temperature}°C", fg="green")
