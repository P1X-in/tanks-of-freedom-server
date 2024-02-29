"""Module for creating png map images."""
import png
import os.path
from tof_server import config


MAP_SIZE = 40

TILE_BUILDING = [115, 41, 48]
TILE_CITY = [47, 72, 78]
TILE_CONCRETE = [157, 157, 157]
TILE_DIRT_ROAD = [73, 60, 34]
TILE_FOREST = [68, 137, 26]
TILE_GRASS = [163, 206, 39]
TILE_MOUNTAIN = [204, 204, 204]
TILE_RIVER = [0, 87, 132]
TILE_ROAD = [101, 109, 113]
TILE_WATER = [49, 162, 242]
TILE_SNOW = [255, 255, 255]
TILE_SAND = [247, 226, 107]
TILE_AUTUMN = [235, 137, 49]
TILE_DUNES = [250, 180, 11]
TILE_CACTI = [17, 94, 51]

grass_tiles = ["ground_grass"]
snow_tiles = ["ground_snow"]
sand_tiles = ["ground_sand", "frame_wheat"]
concrete_tiles = ["ground_concrete"]
river_tiles = [
    "ground_river1",
    "ground_river2",
    "ground_snow_river1",
    "ground_snow_river2",
    "ground_sand_river1",
    "ground_sand_river2",
    "ground_swamp",
    "ground_swamp2",
    "ground_swamp3",
]
road_tiles = [
    "ground_road1",
    "ground_road2",
    "ground_road3",
    "ground_road4",
    "city_bridge",
    "ground_snow_road1",
    "ground_snow_road2",
    "ground_snow_road3",
    "ground_snow_road4",
    "ground_sand_road1",
    "ground_sand_road2",
    "ground_sand_road3",
    "ground_sand_road4",
    "bridge_plate",
    "bridge_legs",
    "bridge2_plate",
    "bridge2_legs",
    "ground_road_transition",
    "ground_road_transition2",
    "ground_road_transition3",
    "ground_road_transition4",
    "ground_snow_road_transition",
    "ground_snow_road_transition2",
    "ground_snow_road_transition3",
    "ground_snow_road_transition4",
    "ground_sand_road_transition",
    "ground_sand_road_transition2",
    "ground_sand_road_transition3",
    "ground_sand_road_transition4",
]
dirt_road_tiles = [
    "ground_dirt_road1",
    "ground_dirt_road2",
    "ground_dirt_road3",
    "ground_dirt_road4",
    "city_bridge_wood",
    "bridge_stone",
    "ground_mud",
    "bridge2_stone",
    "deco_rail_straight",
    "deco_rail_straight2",
    "deco_rail_turn",
    "deco_rail_t",
    "deco_rail_cross",
    "deco_rail_end",
]
city_tiles = [
    "city_building_big1",
    "city_building_big2",
    "city_building_big3",
    "city_building_big4",
    "city_building_big5",
    "city_building_medium1",
    "city_building_small1",
    "city_building_small2",
    "city_building_small3",
    "city_building_small4",
    "city_building_small5",
    "city_building_small6",
    "city_building_small10",
    "city_building_small11",
    "city_shop1",
    "city_shop2",
    "city_shop3",
    "city_farm1",
    "city_farm2",
    "deco_fountain",
    "deco_statue",
    "deco_statue_rat",
    "deco_statue_capsule",
    "damaged_statue",
    "damaged_statue_rat",
    "damaged_statue_capsule",
    "damaged_fountain",
    "damaged_building_small1",
    "damaged_building_small2",
    "damaged_building_small3",
    "damaged_building_small4",
    "damaged_building_small5",
    "damaged_building_small6",
    "damaged_building_small10",
    "damaged_building_small11",
    "damaged_building_medium1",
    "damaged_building_big1",
    "damaged_building_big2",
    "damaged_building_big3",
    "damaged_building_big4",
    "damaged_building_big5",
    "damaged_shop1",
    "damaged_shop2",
    "damaged_shop3",
    "damaged_farm1",
    "damaged_farm2",
    "destroyed_building_small1",
    "destroyed_building_small2",
    "destroyed_building_small3",
    "destroyed_building_small4",
    "destroyed_building_small5",
    "destroyed_building_small6",
    "destroyed_building_small10",
    "destroyed_building_small11",
    "destroyed_building_medium1",
    "destroyed_building_big1",
    "destroyed_building_big2",
    "destroyed_building_big3",
    "destroyed_building_big4",
    "destroyed_building_big5",
    "destroyed_shop1",
    "destroyed_shop2",
    "destroyed_shop3",
    "destroyed_farm1",
    "destroyed_farm2",
    "destroyed_statue",
    "destroyed_statue_rat",
    "destroyed_statue_capsule",
    "destroyed_fountain",
    "castle_wall_straight",
    "castle_wall_straight2",
    "castle_wall_corner",
    "castle_wall_cross",
    "castle_wall_t",
    "castle_wall_t2",
    "castle_wall_gate",
    "castle_wall_gate_closed",
    "brick_wall_straight",
    "brick_wall_straight2",
    "brick_wall_corner",
    "brick_wall_cross",
    "brick_wall_t",
    "brick_wall_t2",
    "brick_wall_gate",
    "brick_wall_gate_closed",
    "fence_wall_straight",
    "fence_wall_straight2",
    "fence_wall_corner",
    "fence_wall_cross",
    "fence_wall_t",
    "fence_wall_t2",
    "fence_wall_gate",
    "fence_wall_gate_closed",
    "futuristic_wall_straight",
    "futuristic_wall_straight2",
    "futuristic_wall_corner",
    "futuristic_wall_cross",
    "futuristic_wall_t",
    "futuristic_wall_t2",
    "futuristic_wall_gate",
    "futuristic_wall_gate_closed",
]
mountain_tiles = [
    "nature_big_rocks1",
    "nature_big_rocks2",
    "nature_big_rocks3",
    "nature_big_rocks4",
]
forest_tiles = [
    "nature_trees1",
    "nature_trees2",
    "nature_trees3",
    "nature_trees4",
    "nature_trees5",
    "nature_trees6",
    "nature_trees10",
    "nature_trees11",
    "nature_trees12",
    "nature_trees13",
    "nature_trees16",
    "nature_trees17",
    "nature_trees18",
]

forest_autumn_tiles = [
    "nature_trees7",
    "nature_trees8",
    "nature_trees9",
    "nature_trees14",
    "nature_trees15",
]

cacti_tiles = [
    "nature_sand_cacti1",
    "nature_sand_cacti2",
    "nature_sand_cacti3",
    "nature_sand_palms1",
    "nature_sand_palms2",
    "nature_sand_palms3",
    "nature_sand_palms4",
]

dune_tiles = [
    "nature_sand_dunes1",
    "nature_sand_dunes2",
    "nature_sand_dunes3",
    "nature_sand_dunes4",
]


def create_map(map_code, map_data):
    """Method for creating map image."""
    if _map_image_exists(map_code):
        return

    file_path = _get_file_path(map_code)

    image_matrix = _generate_base_image_matrix()
    image_matrix = _fill_matrix_with_data(image_matrix, map_data)

    image_matrix = _flatten_matrix(image_matrix)

    image = png.from_array(image_matrix, 'RGB')
    image.save(file_path)


def _map_image_exists(map_code):
    """Method for checking if particular map has generated image."""
    file_path = _get_file_path(map_code)
    return os.path.isfile(file_path)


def _get_file_path(map_code):
    """Method for generating map image path."""
    return config.MAP_V2_IMAGES_FOLDER + map_code + '.png'


def _generate_base_image_matrix():
    """Method for generating base image matrix."""
    image_matrix = []

    for y in range(MAP_SIZE):
        row = []
        for x in range(MAP_SIZE):
            row.append(TILE_WATER)
        image_matrix.append(row)

    return image_matrix


def _fill_matrix_with_data(image_matrix, map_data):
    """Method for filling image matrix with actual map data."""
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            tile_key = str(x) + '_' + str(y)
            if tile_key in map_data['tiles']:
                tile_data = map_data['tiles'][tile_key]

                image_matrix[y][x] = _get_cell_from_tile(tile_data)
    return image_matrix


def _flatten_matrix(image_matrix):
    """Method for flattening the generated matrix."""
    flat_data = []

    for row in image_matrix:
        new_row = []
        for pixel in row:
            new_row.append(pixel[0])
            new_row.append(pixel[1])
            new_row.append(pixel[2])
        flat_data.append(new_row)

    return flat_data


def _get_cell_from_tile(tile_data):
    """Method for picking colour for matrix cell."""
    if tile_data["building"]["tile"] is not None:
        return TILE_BUILDING

    if tile_data["terrain"]["tile"] in city_tiles:
        return TILE_CITY

    if tile_data["terrain"]["tile"] in mountain_tiles:
        return TILE_MOUNTAIN

    if tile_data["terrain"]["tile"] in forest_tiles:
        return TILE_FOREST

    if tile_data["terrain"]["tile"] in forest_autumn_tiles:
        return TILE_AUTUMN

    if tile_data["terrain"]["tile"] in dune_tiles:
        return TILE_DUNES

    if tile_data["terrain"]["tile"] in cacti_tiles:
        return TILE_CACTI

    if tile_data["ground"]["tile"] in dirt_road_tiles or tile_data["terrain"]["tile"] in dirt_road_tiles:
        return TILE_DIRT_ROAD

    if tile_data["ground"]["tile"] in road_tiles or tile_data["terrain"]["tile"] in road_tiles:
        return TILE_ROAD

    if tile_data["ground"]["tile"] in river_tiles:
        return TILE_RIVER

    if tile_data["ground"]["tile"] in concrete_tiles:
        return TILE_CONCRETE

    if tile_data["ground"]["tile"] in grass_tiles:
        return TILE_GRASS

    if tile_data["ground"]["tile"] in snow_tiles:
        return TILE_SNOW

    if tile_data["ground"]["tile"] in sand_tiles:
        return TILE_SAND

    # Fallback for undefined tiles
    return TILE_WATER
