import click
import logging
from app.logger import LOG
from app.tweet_consumer import TweetConsumer


@click.command()
@click.option('--verbose', '-v', is_flag=True)
def main(verbose: bool = False):
    """
    An entry point for twitter consumer
    """
    loglevel = 'DEBUG' if verbose else 'INFO'
    LOG.setLevel(loglevel)

    consumer = TweetConsumer()
    consumer.execute()


if __name__ == '__main__':
    main()
