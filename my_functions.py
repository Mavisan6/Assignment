# clipping rasters to AOI

from rasterio.mask import mask
import geopandas as gpd
import rasterio as rio

def clip_raster_to_aoi(raster_path, AOI_path, output_path):
    """
    This function clips a raster file to a specified Area of Interest (AOI).

    Parameters:
    raster_path (str): The path to the input raster file.
    AOI_path (str): The path to the shapefile defining the AOI.
    output_path (str): The path where the output clipped raster file will be saved.

    Returns:
    None
    """
    # Load the search area polygon
    AOI = gpd.read_file(AOI_path)

    with rio.open(raster_path) as src:
        # Clip the raster data to the search area
        clipped_data, clipped_transform = mask(src, shapes=AOI.geometry.values, crop=True)

        # Update the metadata of the source file
        out_meta = src.meta.copy()
        out_meta.update({"driver": "GTiff",
                         "height": clipped_data.shape[1],
                         "width": clipped_data.shape[2],
                         "transform": clipped_transform})

        # Write the clipped data to the output file
        with rio.open(output_path, 'w', **out_meta) as dst:
            dst.write(clipped_data)

    print(f"Clipped raster saved to {output_path}")

# Extracting raster bounds and converting them to latitude and longitude 

import pyproj

def get_tiff_bounds_to_latlon(tiff_path):
    """
    Extracts bounding box from a TIFF file and converts it to latitude and longitude. 

    Args:
        tiff_path (str): Path to the TIFF file.

    Returns:
        Tuple: A tuple containing (lon_min, lat_min, lon_max, lat_max).
    """
    
    # Open the tIFF file
    with rio.open(tiff_path) as dataset:
        # Get the bounding box in map coordinates
        bounding_box = dataset.bounds

        # Define the source (TIFF) and target (WGS 84) coordinate systems
        src_crs = pyproj.CRS(dataset.crs)
        target_crs = pyproj.CRS("EPSG:4326") #WGS 84

        # Create a transformer
        transformer = pyproj.Transformer.from_crs(src_crs, target_crs, always_xy=True)

        # Transform the bounding box coordinates
        minx, miny, maxx, maxy = bounding_box
        lon_min, lat_min = transformer.transform(minx, miny)
        lon_max, lat_max = transformer.transform(maxx, maxy)

        return lon_min, lat_min, lon_max, lat_max



