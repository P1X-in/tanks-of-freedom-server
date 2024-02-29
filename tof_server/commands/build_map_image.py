"""Build map image command blueprint."""
import click
from flask import Blueprint
from tof_server.models import map_v2 as map_model
from tof_server.utils import png_creator_v2 as png_creator
from tof_server.utils import file_storage

build_map_image_command = Blueprint('build-map-image', __name__, cli_group='admin')


@build_map_image_command.cli.command('build-map-image')
@click.argument('code')
def execute(code):
    """Generate missing images."""
    map_data = file_storage.get_map_v2(code)
    print(map_data["metadata"])
    # png_creator.create_map(code, map_data)

    # map_model.generate_missing_images()
