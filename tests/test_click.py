import pathlib
from enum import Enum

import click

from mtoolbox.click import EnumChoice, ParsedDate, Path


class AF(Enum):
    IPv4 = 4
    IPv6 = 6


def test_enum_choice(runner):
    @click.command()
    @click.option("--af", type=EnumChoice(AF, int))
    def cmd(af):
        click.echo(af)

    result = runner.invoke(cmd, ["--af", "6"])
    assert result.exit_code == 0
    assert result.output == "AF.IPv6\n"

    result = runner.invoke(cmd, ["--help"])
    assert result.exit_code == 0
    assert "--af [4|6]" in result.output


def test_path(runner):
    @click.command()
    @click.option("--path", type=Path())
    def cmd(path):
        click.echo(path)
        click.echo(isinstance(path, pathlib.Path))

    result = runner.invoke(cmd, ["--path", "directory"])
    assert result.exit_code == 0
    assert result.output == "directory\nTrue\n"


def test_parsed_date(runner):
    @click.command()
    @click.option("--date", type=ParsedDate())
    def cmd(date):
        click.echo(date)

    result = runner.invoke(cmd, ["--date", "21 february 2019 at noon"])
    assert result.exit_code == 0
    assert result.output == "2019-02-21 12:00:00\n"

    settings = {"RETURN_AS_TIMEZONE_AWARE": True, "TIMEZONE": "UTC"}

    @click.command()
    @click.option(
        "--date", type=ParsedDate(settings=settings),
    )
    def cmd2(date):
        click.echo(date.tzinfo)

    result = runner.invoke(cmd2, ["--date", "21 february 2019 at noon"])
    assert result.exit_code == 0
    assert result.output == "UTC\n"
