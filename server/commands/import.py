import click
from commands.importer import TokyoDemandForecastImporter


@click.group()
def cli():
    pass


@cli.command()
def all():
    TokyoDemandForecastImporter.run()


@cli.command()
def tokyo():
    TokyoDemandForecastImporter.run()


if __name__ == "__main__":
    cli()
