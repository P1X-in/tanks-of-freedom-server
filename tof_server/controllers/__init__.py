"""Load controllers blueprints."""
from tof_server import app
from tof_server.controllers.main import controller_main
from tof_server.controllers.map import controller_map
from tof_server.controllers.match import controller_match
from tof_server.controllers.player import controller_player
from tof_server.controllers.browser import controller_browser

app.register_blueprint(controller_main)
app.register_blueprint(controller_player)
app.register_blueprint(controller_map)
app.register_blueprint(controller_match)
app.register_blueprint(controller_browser)
