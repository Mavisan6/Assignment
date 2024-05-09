**Author**: [Mavi Santarelli](https://www.linkedin.com/in/mariavittoria-santarelli/)
**Contact**: m.santarelli@live.com

# Read Me

The aim of this study is to develop a Python tool to further analyse Habitat Connectivity maps that were previously created using Circuitscape as part of my [BSc dissertation project](https://www.linkedin.com/posts/mariavittoria-santarelli_sustainableagriculture-agroecological-community-activity-6954342396763504641-3Ndx?utm_source=share&utm_medium=member_desktop). 

## Overview

Specifically, the code is divided in 4 parts as described below:
1. [Part 1](ScriptP1.ipynb) extracts and prepares data to be used in the analysis using libraries like `geopandas` and `deep_translator` to perform tasks such as opening, modifying, translating, clipping and joining shapefiles.
2. [Part 2](ScriptP2.ipynb) downloads satellite images relative to the area of interest (AOI) and calculates *Normalised Difference Vegetation Index (NDVI)* values using libraries such as `EarthAccess`, `shapely` and `rasterio`.
3. [Part 3](ScriptP3.ipynb) extracts Zonal Statistics and performs comparative analysis of NDVI and Habitat Connectivity data using libraries like `rasterstats`, `rasterio` and `matplotlib`.
4. [Part 4](ScriptP4.ipynb) explores ways to deploy tools and libraries such as `seaborn`,`folium` and `cartopy` to display the results obtained.  

The sections below provide a brief description of the project's dependencies, how to install and begin using the produced code as well as details on the source and content of test data provided in the repository.

### Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [License](#license)
- [Acknowledgements](#acknowledgments)

## Dependencies
Each library required for this project is listed with a brief description and a link to its documentation for more detailed information on usage and features.

1. **Python**: the programming language used for this project ([Python Documentation](https://www.python.org/doc/)).
2. **Geopandas**: a library that makes working with geospatial data in Python easier. ([Geopandas Documentation](https://geopandas.org/en/stable/docs.html)).
3. **Cartopy**: a Python package designed for geospatial data processing to create maps and perform other geospatial analyses. It provides an interface built on top of Matplotlib for creating publication-quality maps ([Cartopy Documentation](https://scitools.org.uk/cartopy/docs/latest/).
4. **JupyterLab**: an interactive notebook authoring application and editing environment. This is necessary for the correct visualisation of the script files as they contain markdown cells for code and workflow explanation ([JupyterLab Documentation](https://jupyterlab.readthedocs.io/en/stable/index.html)).
5. **ipywidgets**: interactive HTML widgets for Jupyter notebooks ([ipywidgets Documentation](https://ipywidgets.readthedocs.io/en/latest/)).
6.  **Rasterio**: a library for reading and writing geospatial raster data ([Rasterio Documentation](https://rasterio.readthedocs.io/en/stable/quickstart.html)).
7.  **pyepsg**: a library providing simple access to the EPSG database ([pyepsg Documentation](https://pyepsg.readthedocs.io/en/latest/)).
8.  **Folium**: a library to create interactive leaflet maps using Python data manipulation tools([Folium Documentation](https://python-visualization.github.io/folium/latest/)).
9.  **Matplotlib**: a plotting library for creating static, interactive, and animated visualizations in Python ([Matplotlib Documentation](https://matplotlib.org/stable/index.html)).
10.  **NumPy**: a fundamental package for scientific computing with Python ([NumPy Documentation](https://numpy.org/doc/stable/index.html?ref=mostlypython.com)).
11.  **Deep Translator**: a flexible tool to translate between different languages using multiple translators ([Deep Translator Documentation](https://deep-translator.readthedocs.io/en/latest/README.html))
12.  **Shapely**: a library for manipulation and analysis of planar geometric objects ([Shapely Documentation](https://shapely.readthedocs.io/en/stable/manual.html)).
13.  **Rasterstats**: a Python module for summarizing geospatial raster datasets based on vector geometries ([Rasterstats Documentation](https://pythonhosted.org/rasterstats/)).
14.  **Seaborn**: a statistical data visualization library based on Matplotlib ([Seaborn Documentation](https://seaborn.pydata.org/)).
15.  **Earthaccess**: a library to search, download, or stream NASA Earth science data ([Earthaccess Documentation](https://earthaccess.readthedocs.io/en/latest/tutorials/getting-started/)).
16.  **pyproj**: python interface to PROJ, a cartographic projections and coordinate transformations library ([pyproj Documentation](https://pyproj4.github.io/pyproj/stable/).

To streamline the setup process, all dependencies are included in the [environment.yml](environment.yml) file. This allows for quick and consistent environment setup to run the code. Please follow the instructions provided below to create and activate your environment using this file.

## Installation

### Setting up Your Environment

## Usage

## Data

Data on Agricultural Management Type and Protected Areas was sourced and extracted from the land cover map of Apulia, available from the regional 
spatial database [(Banche Dati - S.I.T. - SIT Puglia (regione.puglia.it)).](https://pugliacon.regione.puglia.it/web/sit-puglia-paesaggio/file-vettoriali). The folder Data_files contains test data that was used to run the code as described below.

#### AgriculturalPlots.shp

The shapefile AgriculturalPlots contains information on the location, number and management type for all agricultural plots under the Area of Interest (AOI). The file has already been clipped to the AOI to reduce computational time and facilitate the handling of the Geodataframe. However, the code will still show other data preparation tools, such as deleting columns and translating the content of the shapefile. 

#### Area_of_Interest.shp

A specific AOI was chosen for the presented case study to reduce processing time, however, the code could be run to assess trends in the whole region. The shapefile Area_of_Interest contains information on the boundaries of the AOI.

#### PAs.shp

The shapefile PAs contains information on the location and extent of Protected Areas around the whole region of Apulia. The code will show how to clip the shapefile to the AOI. 

#### Final.asc

This is the Habitat Connectivity map produced as a result of a study conducted for my [BSc Dissertation](https://www.linkedin.com/posts/mariavittoria-santarelli_sustainableagriculture-agroecological-community-activity-6954342396763504641-3Ndx?utm_source=share&utm_medium=member_desktop). The code will  use this data to extract habitat connectivity values and perform zonal statistics.





## License

This project is licensed under the [MIT License](https://github.com/Mavisan6/Assignment/blob/main/LICENSE) - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
- [Automating GIS and remote sensing workflows with open python libraries](https://towardsdatascience.com/automating-gis-and-remote-sensing-workflows-with-open-python-libraries-e71dd6b049ee) by [Guilherme M. Iablonovski](https://guilhermeiablonovski.medium.com/)
- Production of Habitat Connectivity data was made possible thanks to the collaboration with the ornithologist [Gianpasquale Chiatante](https://www.researchgate.net/profile/Gianpasquale-Chiatante) during my [BSc Dissertation](https://www.linkedin.com/posts/mariavittoria-santarelli_sustainableagriculture-agroecological-community-activity-6954342396763504641-3Ndx?utm_source=share&utm_medium=member_desktop).
- [README Guide](https://coding-boot-camp.github.io/full-stack/github/professional-readme-guide/) by The Coding Bootcamp


