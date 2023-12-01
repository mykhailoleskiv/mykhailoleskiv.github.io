import xml.etree.ElementTree as ET


if __name__ == "__main__":
    tree = ET.parse("source.xml")
    root = tree.getroot()
    # umap
    for point in root.find("trk").find("trkseg").iter("trkpt"):
        print([float(point.attrib["lat"]), float(point.attrib["lon"])], end=",\n")
    # osm and
    # for point in root.find("rte").iter("rtept"):
    #     print([float(point.attrib["lat"]), float(point.attrib["lon"])], end=",\n")
