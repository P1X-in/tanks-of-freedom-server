"""Load commands blueprints."""
from tof_server import app
from tof_server.commands.build_map_images import build_map_images_command

app.register_blueprint(build_map_images_command)
