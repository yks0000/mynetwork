import requests
import click
from rich.console import Console

console = Console(log_path=False, log_time=False)


def public_ip() -> requests.Response:
    return requests.get('https://wgetip.com')


@click.command()
def ip():
    response = public_ip()
    console.log(f'Public IP: {response.text}')
