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


# Extracting centroid coordinates (lat, lon) of a shapefile

import pyproj

def shapefile_center_to_latlon(shapefile_path, utm_zone):
    """
    This function calculates the geographic center (centroid) of a shapefile and 
    converts its coordinates from UTM to latitude and longitude.

    Args:
        shapefile_path (str): Path to the shapefile.
        utm_zone (int): The UTM zone number of the shapefile.

    Returns:
        tuple: A tuple containing the latitude and longitude of the centroid.
    """
    
    # Load the shapefile into a GeoDataFrame
    gdf = gpd.read_file(shapefile_path)

    # Calculate the geometric center (centroid) of all features in the shapefile
    center = gdf.unary_union.centroid

    # Extract the UTM coordinates of the center point
    utm_x, utm_y = center.x, center.y

    # Create a transformer object for converting coordinates from UTM to WGS84
    utm_to_wgs84 = pyproj.Transformer.from_crs(f'EPSG:326{utm_zone}', 'EPSG:4326', always_xy=True)

    # Use the transformer to convert the UTM coordinates to latitude and longitude
    lon, lat = utm_to_wgs84.transform(utm_x, utm_y)

    return lat, lon



# Extracting raster bounds and converting them to latitude and longitude 

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


# Transforming rasters to be used in Cartopy

import numpy as np
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio.warp import transform_bounds

def transform_raster(raster_path, target_crs):
    '''
    This function takes a raster file path and a target Coordinate Reference System (CRS) as inputs.
    It opens the raster file, reads the data, and gets the bounds of the raster.
    Then, it calculates the transform and the new dimensions for the reprojected data.
    It creates a new array for the reprojected data and performs the reprojection.
    Finally, it calculates the new bounds of the reprojected data and returns the reprojected data,
    the new transform, and the new bounds.

    Parameters:
    raster_path (str): The path to the raster file.
    target_crs (dict): The target CRS in proj4 format.

    Returns:
    dst_img (numpy.ndarray): The reprojected raster data.
    transform (affine.Affine): The transform of the reprojected data.
    (new_left, new_bottom, new_right, new_top) (tuple): The bounds of the reprojected data.
    '''

    # Open the raster file
    with rio.open(raster_path) as src:
        # Read the raster data
        img = src.read(1)

        # Get the bounds of the raster
        left, bottom, right, top = src.bounds

        # Define the source CRS
        src_crs = src.crs

    # Calculate the transform and the new dimensions
    transform, width, height = calculate_default_transform(src_crs, target_crs, src.width, src.height, *src.bounds)

    # Create a new array for the reprojected data
    dst_img = np.empty((src.count, height, width))

    # Reproject the data
    reproject(
        img,
        dst_img,
        src_transform=src.transform,
        src_crs=src_crs,
        dst_transform=transform,
        dst_crs=target_crs,
        resampling=Resampling.cubic)

    # Calculate the new bounds
    new_left, new_bottom, new_right, new_top = transform_bounds(src_crs, target_crs, left, bottom, right, top)

    return dst_img, transform, (new_left, new_bottom, new_right, new_top)

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Adding a Scale bar to a Cartopy Plot
def scale_bar(ax, location=(0.92, 0.05)):
    
    """Add a scale bar adapted this question: https://stackoverflow.com/q/32333870 and 
    answered by SO user Siyh: https://stackoverflow.com/a/35705477"""
    
    x0, x1, y0, y1 = ax.get_extent() # get the current extent of the axis
    sbx = x0 + (x1 - x0) * location[0] # get the lower left x coordinate of the scale bar
    sby = y0 + (y1 - y0) * location[1] # get the lower left y coordinate of the scale bar

    linewidth = 6  # width of the scale bar, adjust as needed
    ax.plot([sbx, sbx - 5000], [sby, sby], color='k', linewidth=linewidth, transform=ax.projection) # plot a thick black line, 5 km long
    ax.plot([sbx, sbx - 2500], [sby, sby], color='k', linewidth=linewidth, transform=ax.projection) # plot a smaller black line from 0 to 2.5 km long
    ax.plot([sbx-2500, sbx - 5000], [sby, sby], color='w', linewidth=linewidth, transform=ax.projection) # plot a white line from 2.5 to 5 km

    ax.text(sbx, sby-500, '5 km', transform=ax.projection, fontsize=8) # add a label at 5 km
    ax.text(sbx-2500, sby-500, '2.5 km', transform=ax.projection, fontsize=8) # add a label at 2.5 km
    ax.text(sbx-5000, sby-500, '0 km', transform=ax.projection, fontsize=8) # add a label at 0 km

    return ax

#Adding a North Arrow to a Cartopy Plot

def add_north_arrow(ax, x=0.9, y=0.9):
    
    """Add a north arrow at position x, y (in axes-relative coordinates)"""
    
    ax.annotate('N', xy=(x, y-0.05), xycoords='axes fraction',
                ha='center', va='center', fontsize=20,
                bbox=dict(boxstyle="square", facecolor='none', edgecolor='none'))
    ax.arrow(x, y, 0, 0.05, transform=ax.transAxes, 
             head_width=0.01, head_length=0.02, fc='black', ec='black')




