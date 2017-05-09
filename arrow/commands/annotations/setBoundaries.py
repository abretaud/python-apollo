import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('setBoundaries')
@click.argument("uniquename")
@click.argument("start")
@click.argument("end")


@pass_context
@apollo_exception
@dict_output
def cli(ctx, uniquename, start, end):
    """Warning: Undocumented Method
    """
    return ctx.gi.annotations.setBoundaries(uniquename, start, end)