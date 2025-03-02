"""Ban map v2 command blueprint."""
import click
from tof_server.commands.admin_group import admin_cli
from tof_server.models import map_v2 as map_model
from tof_server.utils import file_storage


@admin_cli.command('ban-map-v2')
@click.argument('code')
def execute(code):
    """Ban v2 map by code."""
    map_data = file_storage.get_map_v2(code)

    if map_data is not None:
        print("V2 map identified")
        print(map_data["metadata"])
        map_model.ban_map_by_code(code)
        return
