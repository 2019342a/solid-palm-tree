"""
Module where the geojson methods reside.
"""

import geojson

import parse

def create_map(data_file):
    """
    creates the map in GeoJSON and writes it to a file.
    """

    geo_map = {"type": "FeatureCollection"}

    item_list = []

    for index, line in enumerate(data_file):

        if line['X'] == "0" or line['Y'] == "0":
            continue

        data = {}

        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        item_list.append(data)

    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))

def main():
    data = parse.parse(parse.SF_FILE, ",")

    return create_map(data)

if __name__ == "__main__":
    main()
