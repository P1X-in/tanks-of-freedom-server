"""Build map images command blueprint."""
from flask import Blueprint
from tof_server.models import map as map_model

build_map_images_command = Blueprint('admin', __name__)


@build_map_images_command.cli.command('build-map-images')
def execute():
    """Generate missing images."""
    map_model.generate_missing_images()
