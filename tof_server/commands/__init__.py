"""Load commands blueprints."""
from tof_server import app
from tof_server.commands.build_map_images import build_map_images_command
from tof_server.commands.build_map_image import build_map_image_command
from tof_server.commands.ban_map_v2 import ban_map_v2_command

app.register_blueprint(build_map_images_command)
app.register_blueprint(build_map_image_command)
app.register_blueprint(ban_map_v2_command)
