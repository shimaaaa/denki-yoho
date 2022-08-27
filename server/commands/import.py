import click
from commands.importer import import_tokyo_forecast


@click.group()
def cli():
    pass


@cli.command()
def all():
    import_tokyo_forecast()


@cli.command()
def tokyo():
    import_tokyo_forecast()


if __name__ == "__main__":
    cli()
