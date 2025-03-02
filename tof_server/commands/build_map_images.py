"""Build map images command blueprint."""
from tof_server.commands.admin_group import admin_cli
from tof_server.models import map as map_model


@admin_cli.command('build-map-images')
def execute():
    """Generate missing images."""
    map_model.generate_missing_images()
