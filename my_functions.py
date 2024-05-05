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
