"""Module for storing and retrieving files."""
import os.path
import json
from tof_server import config


def store_map_v2(map_code, map_data):
    """Method for storing map data into json file."""
    if _map_exists(map_code):
        return

    file_path = _get_file_path(map_code)
    fp = open(file_path, "w")
    json.dump(map_data, fp, indent=4)
    fp.close()


def get_map_v2(map_code):
    """Method for reading map data from file."""
    if not _map_exists(map_code):
        return None

    map_data = None
    with open(_get_file_path(map_code), "r") as data:
        map_data = json.load(data)
    data.close()
    return map_data


def _map_exists(map_code):
    """Method for checking if particular map has generated image."""
    file_path = _get_file_path(map_code)
    return os.path.isfile(file_path)


def _get_file_path(map_code):
    """Method for generating map image path."""
    return config.MAPS_V2_FOLDER + map_code + ".tofmap.json"
