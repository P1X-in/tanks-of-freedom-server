"""Load commands blueprints."""
from tof_server import app
from tof_server.commands.admin_group import admin_cli

app.cli.add_command(admin_cli)
