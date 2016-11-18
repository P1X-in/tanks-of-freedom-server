"""Module for operations on maps."""
import hashlib
import json
from tof_server import config
from tof_server.utils import randcoder, png_creator
from tof_server.repository import map as map_repository


def persist_map(map_data, author_id):
    """Method for persisting a map based on it's data content."""
    map_hash = hashlib.md5(json.dumps(map_data).encode()).hexdigest()
    map_code = _get_code_for_map(map_hash)
    if map_code is not None:
        return map_code

    new_map_code = _generate_unused_code()
    if new_map_code is None:
        return None

    map_repository.persist_new_map(map_data, new_map_code, map_hash, author_id)
    png_creator.create_map(new_map_code, map_data)

    return new_map_code


def find_map(map_code):
    """Method for retrieving map data."""
    map_data = map_repository.find_data_by_code(map_code)
    if map_data is None:
        return None

    return json.loads(map_data)


def find_map_metadata(map_code):
    """Method for retrieving map metadata."""
    return map_repository.find_metadata_by_code(map_code)


def find_maps_page(offset_id=-1):
    """Method for getting list of maps for page."""
    maps_metadata = map_repository.find_latest_maps_metadata(offset_id)

    maps_ids = [map_metadata['id'] for map_metadata in maps_metadata]

    maps_data = map_repository.find_data_by_ids(maps_ids)

    result = []
    for map_metadata in maps_metadata:
        if map_metadata['id'] in maps_data:
            map_raw_data = maps_data[map_metadata['id']]
            try:
                map_data = json.loads(map_raw_data)
                map_metadata['name'] = map_data['name']
                map_metadata['error'] = False
            except ValueError:
                map_metadata['name'] = "ERR"
                map_metadata['error'] = True
        else:
            map_metadata['name'] = ""
        result.append(map_metadata)

    return result


def _get_code_for_map(map_hash):
    """Method for determining code for a map."""
    existing_map_code = map_repository.find_code_by_hash(map_hash)

    if existing_map_code is not None:
        return existing_map_code

    return None


def _generate_unused_code():
    """Method for generating a new, unused code."""
    size_increase = 0
    while True:
        code = randcoder.get_random_code(config.MAP_CODE_LENGTH + size_increase)
        code_map_id = map_repository.find_id_by_code(code)

        if code_map_id is None:
            return code
        else:
            if size_increase == config.MAP_CODE_LENGTH:
                return None
            size_increase = size_increase + 1


def generate_missing_images():
    """Method for generating missing map images."""
    map_codes = map_repository.get_all_codes()

    for code in map_codes:
        if not png_creator.map_image_exists(code[0]):
            map_data = find_map(code[0])
            png_creator.create_map(code[0], map_data)
