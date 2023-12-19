# Import the necessary libraries
import ee
import geemap

print("starting")
# Initialize the Earth Engine module
ee.Initialize()
print("initialized")
# Define the area of interest
point = ee.Geometry.Point([85.3475465, 23.3499754])
print("point defined")
# Define the image collection
collection = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR")
print("collection defined")
# Filter the collection
image = (
    collection.filterBounds(point)
    .filterDate("2021-10-01", "2021-10-31")
    .sort("CLOUD_COVER")
    .first()
)
print("image defined")
# Define the visualization parameters
vis_params = {"min": 0, "max": 3000, "bands": ["B4", "B3", "B2"]}
print("vis_params defined")
# Create a map
Map = geemap.Map(center=[23.3499754, 85.3475465], zoom=10)
print("map defined")
# Add the image to the map
Map.addLayer(image, vis_params, "Landsat-8")
print("image added")
# Display the map
Map
print("map displayed")
# Define the file name and path
out_dir = "output/"
out_file = out_dir + "output.png"
print("out_dir and out_file defined")
# Export the image as a PNG
geemap.ee_export_image(
    image, filename=out_file, scale=30, region=point, file_per_band=False
)
print("image exported")
