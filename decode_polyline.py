#!/usr/bin/python
import sys
import polyline
import folium
import argparse


# Author: Fabian Nunes
# Script to decode an encoded polyline value to a set of coordinates for Google Maps
# Requires the polyline module (Install with pip install polyline)
# Example: python decode_polyline.py file.txt -html|-url|-kml

class Bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


parser = argparse.ArgumentParser(description='Decode an encoded polyline value to a set of coordinates and generate a map')
parser.add_argument('-f', '--file', help='File with the encoded polyline', required=True)
parser.add_argument('-t', '--type', help='Type of output', required=True, choices=["html", "kml"])
args = parser.parse_args()

FILE = args.file
TYPE = args.type

try:
    f = open(FILE, 'r')
except IOError:
    print(Bcolors.FAIL + "File not found" + Bcolors.ENDC)
    sys.exit(1)

print(Bcolors.OKBLUE + "[Info ] Reading file: " + FILE)
f = open(FILE, "r")
lines = f.readlines()
f.close()

print(Bcolors.OKBLUE + "[Info ] Decoding polyline")
for line in lines:
    line = line.strip()
    print(Bcolors.OKBLUE + "[Info ] Decoding polyline: " + line)
    print(line)
    coordinates = polyline.decode(line)

    print(coordinates)
    # Create a file with the coordinates
    f = open("coordinates.txt", "w")
    for coordinate in coordinates:
        coordinate = str(coordinate)
        # remove the parenthesis
        coordinate = coordinate.replace("(", "")
        coordinate = coordinate.replace(")", "")
        f.write(coordinate + "\n")
    f.close()
    print(Bcolors.OKGREEN + "[Done ] Decoded polyline: " + line)

    if TYPE == "-html":
        # Generate HTML file with the map and the route using Folium
        place_lat = []
        place_lon = []
        print(Bcolors.OKBLUE + "[Info ] Generating HTML file with the map and the route")
        m = folium.Map(location=[coordinates[0][0], coordinates[0][1]], zoom_start=10, max_zoom=19)

        for coordinate in coordinates:
            # if points are to close, skip
            if len(place_lat) > 0 and abs(place_lat[-1] - coordinate[0]) < 0.0001 and abs(
                    place_lon[-1] - coordinate[1]) < 0.0001:
                continue
            else:
                place_lat.append(coordinate[0])
                place_lon.append(coordinate[1])

        points = []
        for i in range(len(place_lat)):
            points.append([place_lat[i], place_lon[i]])

        # Add points to map
        for index, lat in enumerate(place_lat):
            # Start point
            if index == 0:
                folium.Marker([lat, place_lon[index]],
                              popup=('Start Location\n'.format(index)),
                              icon=folium.Icon(color='blue', icon='flag', prefix='fa')).add_to(m)
            # last point
            elif index == len(place_lat) - 1:
                folium.Marker([lat, place_lon[index]],
                              popup=(('End Location\n').format(index)),
                              icon=folium.Icon(color='red', icon='flag', prefix='fa')).add_to(m)
            # middle points

        # Create polyline
        folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(m)
        # Save the map to an HTML file
        title = 'Garmin_Polyline_Map'
        m.save(title + '.html')
    elif TYPE == "-kml":
        # Generate KML file with the coordinates
        print(Bcolors.OKBLUE + "[Info ] Generating KML file with the coordinates")
        kml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <kml xmlns="http://www.opengis.net/kml/2.2">
        <Document>
        <name>Coordinates</name>
        <description>Coordinates</description>
        <Style id="yellowLineGreenPoly">
            <LineStyle>
                <color>7f00ffff</color>
                <width>4</width>
            </LineStyle>
            <PolyStyle>
                <color>7f00ff00</color>
            </PolyStyle>
        </Style>
        <Placemark>
            <name>Absolute Extruded</name>
            <description>Transparent green wall with yellow outlines</description>
            <styleUrl>#yellowLineGreenPoly</styleUrl>
            <LineString>
                <extrude>1</extrude>
                <tessellate>1</tessellate>
                <altitudeMode>clampedToGround</altitudeMode>
                <coordinates>
                """
        for coordinate in coordinates:
            kml += str(coordinate[1]) + "," + str(coordinate[0]) + ",0 \n"
        kml = kml[:-1]
        kml += """
                </coordinates>
            </LineString>
        </Placemark>
        </Document>
        </kml>
        """
        # remove the first space
        kml = kml[1:]
        # remove last line
        kml = kml[:-1]
        #remove extra indentation
        kml = kml.replace("    ", "")
        f = open("map.kml", "w")
        f.write(kml)
        f.close()
        print(Bcolors.OKGREEN + "[Done ] Generated KML file with the coordinates" + Bcolors.ENDC)

