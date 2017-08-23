"""Module for operations on maps."""
import hashlib
import json
import collections
from tof_server import config
from tof_server.utils import randcoder, png_creator
from tof_server.repository import map as map_repository


def persist_map(map_data, author_id):
    """Method for persisting a map based on it's data content."""
    map_data = _rewrite_data_as_sorted(map_data)
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

    return _decorate_map_with_data(maps_metadata)


def _decorate_map_with_data(maps_metadata):
    """Method for decorating list of maps with more data."""
    maps_ids = [map_metadata['id'] for map_metadata in maps_metadata]

    maps_data = map_repository.find_data_by_ids(maps_ids)
    maps_downloads = map_repository.find_download_by_ids(maps_ids)

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

        if map_metadata['id'] in maps_downloads:
            map_metadata['downloads'] = maps_downloads[map_metadata['id']]
        else:
            map_metadata['downloads'] = 0
        result.append(map_metadata)

    return result


def mark_map_download(map_code):
    """Method for marking map download for stats."""
    map_id = map_repository.find_id_by_code(map_code)
    map_repository.mark_map_download(map_id)


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


def find_maps_by_map_author(map_code):
    """Method for getting list of maps by author of map."""
    player_id = map_repository.find_player_by_code(map_code)
    if player_id is None:
        return []

    maps_metadata = map_repository.find_maps_metadata_by_player(player_id)

    return _decorate_map_with_data(maps_metadata)


def _rewrite_data_as_sorted(data):
    """Method for re-writing data collection to ensure it is key-sorted."""
    sorted_data = collections.OrderedDict()

    for key, value in sorted(data.items()):
        if isinstance(value, dict):
            sorted_data[key] = _rewrite_data_as_sorted(value)
        else:
            sorted_data[key] = value

    return sorted_data
