# Decode_Polyline

Repository for script to decode Google Polylines to coordinates and store them in a file and generate a map with the coordinates

## Requirements
 - Python 3
 - Python libraries: polyline, folium, argparse

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
python3 decode_polyline.py -f <file> -t <type>
```

## Output

The script will create a file called coordinates.txt with the coordinates and a map called map.html or a Google Earth file called map.kml.

## License

This code is under the GNU General Public License v3.0. See the LICENSE file for more information.
