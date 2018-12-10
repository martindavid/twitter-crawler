import logging
import click
from app.config_reader import read_config


@click.command()
@click.argument('config')
@click.option('--api-type', '-t', help='choose between stream or search api')
@click.option('--verbose', '-v', is_flag=True)
def main(config: str = None, api_type: str = None, verbose: bool = False):
    """
    An entry point to twitter crawler application
    """
    loglevel = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    log = logging.getLogger(__name__)
    log.info(msg=f"Argument {config} {api_type}")

    if config:
        read_config(config)


if __name__ == '__main__':
    main()
