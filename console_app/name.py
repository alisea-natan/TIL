import click
from config.config import name as nick


@click.command()
@click.option('--name', '-n', default=nick)
def print_hi(name):
    print(f'Hi, {name}')
