import pyproj

def convert_coordinate(northing,easting):
    transformer = pyproj.Transformer.from_crs(state_plane_crs, lat_lon_crs)         # Create a pyproj transformer object to convert from state plane to latitude and longitude
    lat, lon = transformer.transform(easting, northing)                             # Convert the state plane coordinates to latitude and longitude
    # print("Latitude: ",lat)
    # print("Longitude: ",lon)
    print(lat,",",lon)                                                              # Display converted coordinates
    
# Define the state plane coordinate system
state_plane_crs = pyproj.CRS.from_epsg(2277)    # EPSG code as per state plane coordinate system

# Define the latitude and longitude coordinate system
lat_lon_crs = pyproj.CRS.from_epsg(4326)        # EPSG code for WGS84 datum

# Define the state plane coordinates (in feet)
#x = 3221051.75                                  # EASTING
#y = 10387051.75                                 # NORTHING

coordinateFile = 'C:\\Users\\projectasst\\Desktop\\PepperCreekWWCoordinates.txt'

with open(coordinateFile) as coord:
    for line in coord:
        x,y = line.split()
        convert_coordinate(x,y)                     # Call Function to Convert Coordinates

print("\n")


    

    

