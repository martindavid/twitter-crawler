from typing import List, Dict
import logging
import click
from app.config_reader import read_config
from app.crawler import Crawler
from app.logger import LOG


@click.command()
@click.option('--keywords', '-k', help="List of keyword for crawling in a array of string format")
@click.option('--access-token', help="twitter access token use for crawling")
@click.option('--access-token-secret', help="twitter access secret token use for crawling")
@click.option('--config', '-c', help="json config file containing list of keyword and twitter tokens")
@click.option('--api-type', '-t', help='choose between stream or search api')
@click.option('--verbose', '-v', is_flag=True)
def main(keywords: List[str], access_token: str, access_token_secret: str, 
         config: str = None, api_type: str = None, verbose: bool = False):
    """
    An entry point to twitter crawler application
    """
    loglevel = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
    LOG.info(msg=f"Argument {config} {api_type}")
    crawler_config = None
    if config:
        crawler_config = read_config(config)

    if keywords and access_token and access_token_secret:
        crawler_config = construct_config(keywords, access_token, access_token_secret)

    if crawler_config:
        LOG.debug(crawler_config)
        LOG.debug(f"Api Type - {api_type}")
        crawler = Crawler.create_crawler_instance(api_type, crawler_config)
        crawler.execute()

    click.echo("Option is required")


def construct_config(keywords: List[str], access_token: str, access_token_secret: str) -> Dict:
    tokens = [{ "access_token": access_token, "access_token_secret": access_token_secret }]
    return {
        "keywords": keywords,
        "tokens": tokens
    }

if __name__ == '__main__':
    main()
