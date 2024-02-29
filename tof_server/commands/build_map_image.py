"""Build map image command blueprint."""
from flask import Blueprint
from tof_server.models import map_v2 as map_model

build_map_image_command = Blueprint('admin', __name__)


@build_map_image_command.cli.command('build-map-image')
def execute():
    """Generate missing images."""
    print("here")
    # map_model.generate_missing_images()
