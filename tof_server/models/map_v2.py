"""Module for operations on maps."""
from tof_server import config
from tof_server.utils import randcoder, file_storage
from tof_server.utils import png_creator_v2 as png_creator
from tof_server.repository import map_v2 as map_repository


def persist_map(map_data, author_id):
    """Method for persisting a map based on it's data content."""
    map_data['metadata'] = _fill_metadata(map_data['metadata'])

    new_map_code = _generate_code(map_data['metadata'])

    existing_id = map_repository.find_id_by_code(new_map_code)

    if existing_id is not None:
        return {
            'created': False,
            'code': new_map_code,
            'base_code': map_data['metadata']['base_code'],
            'iteration': map_data['metadata']['iteration']
        }

    map_repository.persist_new_map(
        new_map_code,
        map_data['metadata']['base_code'],
        map_data['metadata']['iteration'],
        author_id
    )
    file_storage.store_map_v2(new_map_code, map_data)
    png_creator.create_map(new_map_code, map_data)

    return {
        'created': True,
        'code': new_map_code,
        'base_code': map_data['metadata']['base_code'],
        'iteration': map_data['metadata']['iteration']
    }


def find_map(map_code):
    """Method for retrieving map data."""
    return file_storage.get_map_v2(map_code)


def find_map_metadata(map_code):
    """Method for retrieving map metadata."""
    return map_repository.find_metadata_by_code(map_code)


def find_maps_page(offset_id=-1):
    """Method for getting list of maps for page."""
    maps_metadata = map_repository.find_latest_maps_metadata(offset_id)

    return _decorate_map_with_data(maps_metadata)


def find_maps_top_downloads(top=50):
    """Method for getting list of top downloaded maps."""
    maps_metadata = map_repository.find_maps_metadata_by_top_downloads(top)

    return _decorate_map_with_data(maps_metadata, False)


def _decorate_map_with_data(maps_metadata, add_downloads=True):
    """Method for decorating list of maps with more data."""
    maps_ids = [map_metadata['id'] for map_metadata in maps_metadata]

    maps_downloads = []
    if add_downloads:
        maps_downloads = map_repository.find_download_by_ids(maps_ids)

    result = []
    for map_metadata in maps_metadata:
        map_data = file_storage.get_map_v2(map_metadata['code'])
        map_metadata['name'] = map_metadata['code']
        if 'metadata' in map_data:
            map_metadata['name'] = map_data['metadata']['name']

        if add_downloads:
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


def _generate_code(metadata):
    """Method for generating v2 map code."""
    return metadata['base_code'] + "-" + str(metadata['iteration'])


def _generate_unused_code():
    """Method for generating a new, unused code."""
    size_increase = 0
    while True:
        code = randcoder.get_random_code(config.MAP_CODE_LENGTH + size_increase)

        if not map_repository.is_base_code_used(code):
            return code
        else:
            if size_increase == config.MAP_CODE_LENGTH:
                return None
            size_increase = size_increase + 1


def find_maps_by_map_author(map_code):
    """Method for getting list of maps by author of map."""
    player_id = map_repository.find_player_by_code(map_code)
    if player_id is None:
        return []

    maps_metadata = map_repository.find_maps_metadata_by_player(player_id)

    return _decorate_map_with_data(maps_metadata)


def _fill_metadata(metadata):
    """Fill missing metadata."""
    if 'iteration' not in metadata:
        metadata['iteration'] = 0
    if 'base_code' not in metadata or metadata['base_code'] is None:
        base_code = _generate_unused_code()
        if base_code is None:
            return None
        metadata['base_code'] = base_code
    if 'name' not in metadata:
        metadata['name'] = metadata['base_code']

    return metadata


def ban_map_by_code(map_code):
    """Method for banning a map by it's code."""
    map_repository.ban_map_by_code(map_code)
