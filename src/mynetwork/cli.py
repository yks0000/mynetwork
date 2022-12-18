#!/usr/bin/env python3
import click
from mynetwork.myip.myip import ip
from mynetwork.speed.speed import speed


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)


cli.add_command(ip, "ip")
cli.add_command(speed, "speed")


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
