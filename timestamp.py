### A script to extract markers from a final cut pro project

import xml.etree.ElementTree as ET
import datetime

# Parse the Final Cut Pro XML file
tree = ET.parse('./info.fcpxml')
root = tree.getroot()
ns = {'fcpxml': 'http://www.apple.com/fcpxml-1.0/'}
markerParents = root.findall('.//marker/..', ns)

def parseFCPTimeSeconds (timeString):
    vals = [float(n) for n in timeString.replace('s','').split('/')]
    if 1 == len(vals):
        val = vals[0]
    else:
        val = vals[0]/vals[1]
    return val


for parents in markerParents:
    offset = parseFCPTimeSeconds(parents.get('offset'))
    start = parseFCPTimeSeconds(parents.get('start'))


    markers = parents.findall(".//marker")
    for marker in markers:
        s = parseFCPTimeSeconds(marker.get('start'))
        s = round(s - start + offset)

        timeStr = str(datetime.timedelta(seconds=s))

        print(timeStr + " " + marker.get("value"))
