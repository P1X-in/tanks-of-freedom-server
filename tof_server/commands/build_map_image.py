"""Build map image command blueprint."""
import click
from tof_server.commands.admin_group import admin_cli
from tof_server.models import map as map_model
from tof_server.utils import png_creator, png_creator_v2
from tof_server.utils import file_storage


@admin_cli.command('build-map-image')
@click.argument('code')
def execute(code):
    """Generate missing images."""
    map_data = map_model.find_map(code)

    if map_data is not None:
        print("V1 map identified")
        png_creator.create_map(code, map_data)
        return

    map_data = file_storage.get_map_v2(code)

    if map_data is not None:
        print("V2 map identified")
        print(map_data["metadata"])
        png_creator_v2.create_map(code, map_data)
        return
