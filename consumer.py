import logging
import click
from app.tweet_consumer import TweetConsumer


@click.command()
@click.option('--verbose', '-v', is_flag=True)
def main(verbose: bool = False):
    """
    An entry point for twitter consumer
    """
    loglevel = logging.DEBUG if verbose else logging.INFO
    print(loglevel)?!?jedi=0, ?!?    (*_***kwargs*_*) ?!?jedi?!?
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    consumer = TweetConsumer()
    consumer.execute()


if __name__ == '__main__':
    main()
