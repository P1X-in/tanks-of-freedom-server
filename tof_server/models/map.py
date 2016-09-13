"""Module for operations on maps."""
import hashlib
import json
from tof_server import config
from tof_server.utils import randcoder
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

    return new_map_code


def find_map(map_code):
    """Method for retrieving map data."""
    map_data = map_repository.find_data_by_code(map_code)
    if map_data is None:
        return None

    return json.loads(map_data)


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
