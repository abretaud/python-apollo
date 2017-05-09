import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('add_to_group')
@click.argument("group", type=str)
@click.argument("user", type=str)


@pass_context
@apollo_exception
@dict_output
def cli(ctx, group, user):
    """Add a user to a group
    """
    return ctx.gi.users.add_to_group(group, user)