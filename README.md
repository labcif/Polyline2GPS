# Polyline2GPS

Repository for script to decode Google Polylines to coordinates and store them in a file and generate a map with the coordinates

## Requirements
 - Python 3
 - Python libraries: polyline, folium, argparse, geopy. xlsxwriter, pyfiglet

## How it works

Polyline is a string of characters that encodes a series of coordinates. The polyline is encoded using the Google Maps API.
To decode the polyline, the script uses the polyline library. The script takes the polyline as input and returns a list of coordinates.
After that, the script creates a map with the coordinates using the folium library or creates a Google Earth file with the coordinates.

### Example of polyline

```text
'_p~iF~ps|U_ulLnnqC_mqNvxq`@'
```

## Parameters
    - f, --file: File with the polyline
    - t, --type: Type of output file. Options: html, kml
## Usage

```bash
python3 polyline2gps.py -f <file> -t <type>
```

## Output

The script will create a file called a xlsx file with the coordinates and a map with the coordinates. The xlsx file will contain the coordinates and additional information
such as the road, city, postcode and country using the geopy library. To improve speed and prevent blocking the script will save the coordinates in an SQLite database and 
only use the geopy library if the coordinates are not in the database. The map will be created using the folium library and will be saved as an html file.
Or the script will create a KML file with the coordinates to use in Google Earth.

## License

This code is under the GNU General Public License v3.0. See the LICENSE file for more information.
