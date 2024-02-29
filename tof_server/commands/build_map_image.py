"""Build map image command blueprint."""
import click
from flask import Blueprint
from tof_server.models import map_v2 as map_model

build_map_image_command = Blueprint('build-map-image', __name__, cli_group='admin')


@build_map_image_command.cli.command('build-map-image')
@click.argument('name')
def execute(name):
    """Generate missing images."""
    print(name)
    # map_model.generate_missing_images()
