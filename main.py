import click
from edamapi.edamapi import reformat


@click.group(
    help="""
    \b
    A python tool to reformat ontologies in a more reproducible way.

    \b
    Usage examples :
        python main.py reformat -i edam.ttl -o edam.jsonld -f jsonld
        python main.py compare -l v1.ttl -r v2.ttl
    """
)
@click.version_option(version="1.0.0")
def cli():
    pass


cli.add_command(reformat)

if __name__ == "__main__":
    cli()
