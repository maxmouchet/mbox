import pathlib

import click
import dateparser as dp


class EnumChoice(click.ParamType):
    def __init__(self, enum, type_):
        self.enum = enum
        self.type_ = type_

    def convert(self, value, param, ctx):
        return self.enum(self.type_(value))

    @property
    def name(self):
        vals = [str(v.value) for v in self.enum.__members__.values()]
        return f"[{'|'.join(vals)}]"


class Path(click.Path):
    def convert(self, value, param, ctx):
        return pathlib.Path(super().convert(value, param, ctx))


class ParsedDate(click.ParamType):
    name = "DATE"

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def convert(self, value, param, ctx):
        return dp.parse(value, **self.kwargs)
