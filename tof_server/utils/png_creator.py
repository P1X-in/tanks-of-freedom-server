"""Module for creating png map images."""
import png
import os.path
from tof_server import config


MAP_SIZE = 40

COLOUR_WATER = [21, 194, 165]
COLOUR_PLAIN = [163, 206, 39]
COLOUR_DIRT = [247, 226, 107]
COLOUR_FOREST = [68, 137, 26]
COLOUR_CITY = [204, 204, 204]
COLOUR_MOUNTAIN = [157, 157, 157]
COLOUR_ROAD = [101, 109, 113]
COLOUR_ROAD_COUNTRY = [164, 100, 34]
COLOUR_RIVER = [49, 162, 242]
COLOUR_FENCE = [27, 38, 50]
COLOUR_BUILDING = [190, 38, 51]
COLOUR_OTHER = [255, 255, 255]

TERRAIN_PLAIN = 0
TERRAIN_FOREST = 1
TERRAIN_MOUNTAINS = 2
TERRAIN_RIVER = 3
TERRAIN_CITY = 4
TERRAIN_CITY_DESTROYED = 33
TERRAIN_ROAD = 5
TERRAIN_DIRT_ROAD = 6
TERRAIN_DIRT = 7
TERRAIN_BRIDGE = 8
TERRAIN_FENCE = 9
TERRAIN_STATUE = 10

TERRAIN_HQ_BLUE = 11
TERRAIN_HQ_RED = 12

TERRAIN_BARRACKS_FREE = 13
TERRAIN_FACTORY_FREE = 14
TERRAIN_AIRPORT_FREE = 15
TERRAIN_TOWER_FREE = 16

TERRAIN_SPAWN = 17

TERRAIN_BARRACKS_RED = 19
TERRAIN_FACTORY_RED = 20
TERRAIN_AIRPORT_RED = 21
TERRAIN_TOWER_RED = 22

TERRAIN_BARRACKS_BLUE = 23
TERRAIN_FACTORY_BLUE = 24
TERRAIN_AIRPORT_BLUE = 25
TERRAIN_TOWER_BLUE = 26


def create_map(map_code, map_data):
    """Method for creating map image."""
    if map_image_exists(map_code):
        return

    file_path = get_file_path(map_code)

    image_matrix = generate_base_image_matrix()
    image_matrix = fill_matrix_with_data(image_matrix, map_data)

    image = png.from_array(image_matrix, "RGB")
    image.save(file_path)


def map_image_exists(map_code):
    """Method for checking if particular map has generated image."""
    file_path = get_file_path(map_code)
    return os.path.isfile(file_path)


def get_file_path(map_code):
    """Method for generating map image path."""
    return config.MAP_IMAGES_FOLDER + map_code + ".png"


def generate_base_image_matrix():
    """Method for generating base image matrix."""
    image_matrix = []

    for y in range(MAP_SIZE):
        row = []
        for x in range(MAP_SIZE):
            row.append(COLOUR_WATER)
        image_matrix.append(row)

    return image_matrix


def fill_matrix_with_data(image_matrix, map_data):
    """Method for filling image matrix with actual map data."""
    terrain_mapping = {
        TERRAIN_PLAIN: COLOUR_PLAIN,
        TERRAIN_FOREST: COLOUR_FOREST,
        TERRAIN_MOUNTAINS: COLOUR_MOUNTAIN,
        TERRAIN_RIVER: COLOUR_RIVER,
        TERRAIN_CITY: COLOUR_CITY,
        TERRAIN_CITY_DESTROYED: COLOUR_CITY,
        TERRAIN_ROAD: COLOUR_ROAD,
        TERRAIN_DIRT_ROAD: COLOUR_ROAD_COUNTRY,
        TERRAIN_DIRT: COLOUR_DIRT,
        TERRAIN_BRIDGE: COLOUR_ROAD,
        TERRAIN_FENCE: COLOUR_FENCE,
        TERRAIN_STATUE: COLOUR_CITY,
        TERRAIN_HQ_BLUE: COLOUR_BUILDING,
        TERRAIN_HQ_RED: COLOUR_BUILDING,
        TERRAIN_BARRACKS_FREE: COLOUR_BUILDING,
        TERRAIN_FACTORY_FREE: COLOUR_BUILDING,
        TERRAIN_AIRPORT_FREE: COLOUR_BUILDING,
        TERRAIN_TOWER_FREE: COLOUR_BUILDING,
        TERRAIN_SPAWN: COLOUR_ROAD,
        TERRAIN_BARRACKS_RED: COLOUR_BUILDING,
        TERRAIN_FACTORY_RED: COLOUR_BUILDING,
        TERRAIN_AIRPORT_RED: COLOUR_BUILDING,
        TERRAIN_TOWER_RED: COLOUR_BUILDING,
        TERRAIN_BARRACKS_BLUE: COLOUR_BUILDING,
        TERRAIN_FACTORY_BLUE: COLOUR_BUILDING,
        TERRAIN_AIRPORT_BLUE: COLOUR_BUILDING,
        TERRAIN_TOWER_BLUE: COLOUR_BUILDING,
    }

    for tile in map_data['tiles']:
        x = tile['x']
        y = tile['y']
        terrain = tile['terrain']
        if x >= 0 and x < MAP_SIZE and y >= 0 and y < MAP_SIZE:
            if terrain in terrain_mapping:
                colour = terrain_mapping[terrain]
            else:
                colour = COLOUR_OTHER
            image_matrix[y][x] = colour
    return image_matrix
