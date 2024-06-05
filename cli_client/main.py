import click
from srt_core.config import Config

@click.command()
@click.option('--config-file', default='config.yaml', help='Path to the config file')
def cli(config_file):
    config = Config(config_file)
    click.echo(f"Server Name: {config.server_name}")
    click.echo(f"Default LLM Name: {config.default_llm_name}")

if __name__ == '__main__':
    cli()
