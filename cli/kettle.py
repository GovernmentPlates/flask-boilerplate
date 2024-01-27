import click

from commands.maintenance import maintenance_mode
from commands.shell import shell
from commands.boil import boil


@click.group()
def kettle():
    pass


# Add commands below
kettle.add_command(maintenance_mode)
kettle.add_command(shell)
kettle.add_command(boil)


if __name__ == "__main__":
    kettle()
