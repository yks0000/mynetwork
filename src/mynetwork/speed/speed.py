import click
import speedtest
from hurry.filesize import size, si
from rich.console import Console

console = Console(log_path=False, log_time=False)
speed_test = speedtest.Speedtest()


@click.group()
@click.pass_context
def speed(ctx):
    """Speed Group"""
    pass


@speed.command()
def download():
    with console.status(f"[bold green]Running download speed test..."):
        console.log(f'Download Speed: {size(speed_test.download(), si)}')


@speed.command()
def upload():
    with console.status(f"[bold green]Running upload speed test..."):
        console.log(f'Upload Speed: {size(speed_test.upload(), si)}')


speed.add_command(download, name="download")
speed.add_command(upload, name="upload")