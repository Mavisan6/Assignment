**Author**: [Mavi Santarelli](https://www.linkedin.com/in/mariavittoria-santarelli/)
**Contact**: m.santarelli@live.com

# Read Me

The aim of this study is to develop a Python tool to further analyse Habitat Connectivity maps that were previously created using Circuitscape. 
Specifically, the code extracts Zonal Statistics for Habitat Connectivity (a measure for biodiversity) and NDVI for agricultural land plots in Apulia.  

## Overview

The sections below provide a brief description of how to install and begin using the produced code as well as details on the source and content of test data provided in the repository.

## Setting up Your Environment


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
