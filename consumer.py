import click
import logging
from app.logger import LOG
from app.tweet_consumer import TweetConsumer
from app.config_reader import read_config


@click.command()
@click.option('--verbose', '-v', is_flag=True)
@click.option('--config', '-c', help="Json config file")
def main(verbose: bool = False, config: str = None) -> None:
    """
    An entry point for twitter consumer
    """
    loglevel = 'DEBUG' if verbose else 'INFO'
    LOG.setLevel(loglevel)
    config_data = None
    if config:
        config_data = read_config(config)

    consumer = TweetConsumer(config_data)
    consumer.execute()


if __name__ == '__main__':
    main()
