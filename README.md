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
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Data Provided](#data-provided)
- [License](#license)
- [Acknowledgements](#acknowledgments)

## Dependencies
Each library required for this project is listed with a brief description and a link to its documentation for more detailed information on usage and features.

1. **Python**: the programming language used for this project ([Python Documentation](https://www.python.org/doc/)).
2. **Geopandas**: a library that makes working with geospatial data in Python easier ([Geopandas Documentation](https://geopandas.org/en/stable/docs.html)).
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

## Installation and Setup

### 1. Forking the Repository

To get started with the project, you should first create your own copy of the repository by forking it. To do so, visit the [original repository](https://github.com/Mavisan6/Assignment/tree/main) on GitHub and click the 'Fork' button in the upper right corner. This will create a copy of the repository in your GitHub account (you will need to create an account first if you don't have one already).

### 2. Cloning the Forked Repository

After forking the repository on GitHub, you'll want to work with it on your local machine. To do this, you need to clone it using Git, which is a version control system that lets you manage and keep track of your source code history.

Here are the steps to clone the forked repository:

1. **Install Git**:
   - If you don't have Git installed on your computer, download and install it from [Git's official website](https://git-scm.com/).

2. **Open Terminal or Command Prompt**:
   - On macOS or Linux, open the Terminal.
   - On Windows, open Command Prompt or Git Bash (if you installed Git for Windows).

3. **Navigate to the Directory**:
   - Use the `cd` command to navigate to the directory where you want to clone the repository.

4. **Clone the Repository**:
   - Run the following command:
     ```bash
     git clone https://github.com/your-username/repository-name.git
     ```
   - Replace `your-username` with your actual GitHub username.
   - Replace `repository-name` with the actual name of the repository you forked.

5. **Navigate to the Repository Folder**:
   - After cloning, a new folder with the repository's name will be created. Navigate into it with:
     ```bash
     cd repository-name
     ```

6. **Verify the Remote Repository**:
   - Ensure that the remote URL has been set correctly by running:
     ```bash
     git remote -v
     ```
   - You should see the URL of your fork listed as `origin`.

By following these steps, you'll have a local copy of the forked repository, and you can start working on it right away!

### 3. Setting up your Environment

After cloning the repository, the next step is to set up the environment which includes all the necessary dependencies to run the project.

### Install Anaconda or Miniconda
   
Anaconda and Miniconda are both free distributions of Python that include a package manager called `conda`. They help to manage libraries, dependencies, and environments. Visit the [Anaconda website](https://www.anaconda.com/download) or the [Miniconda website](https://docs.anaconda.com/free/miniconda/index.html) to download the installer for your operating system and follow the installation instructions provided on the website.

### Create the Conda Environment

The `environment.yml` file contains all the necessary package information needed to create an environment that mirrors the project's setup. To install it follow the below instructions.

1. **Navigate to the Project Directory**:
   - Open your terminal or command prompt.
   - Use the `cd` command to navigate to the root directory of the cloned repository.

2. **Create the Environment**:
   - Run the following command to create a new conda environment based on the `environment.yml` file:
     ```bash
     conda env create -f environment.yml
     ```
   - This command reads the `environment.yml` file in your project directory and sets up an environment with all the dependencies listed in the file.

3. **Activate the Environment**:
   - Once the environment is created, you need to activate it to use it:
     ```bash
     conda activate your-environment-name
     ```
   - Replace `your-environment-name` with the name of the environment that you have given in the `environment.yml` file.

### Verify the Environment

After setting up the environment, it's good practice to verify that everything is installed correctly.

1. **Check Installed Packages**:
   - With the environment activated, list all the installed packages using:
     ```bash
     conda list
     ```
   - This will show you all the packages installed in the active conda environment.

2. **Test Running the Project**:
   - Try running the project or a test script to ensure that the environment is set up properly and all dependencies are working as expected.

By following these steps, you should have a fully functional development environment for the project. If you encounter any issues, check the `environment.yml` file for errors or missing details, and ensure that all steps were followed correctly.

### 4. Configuring .netrc for Earthaccess

The `.netrc` file stores login and initialization information used by the auto-login process. It allows you to access NASA Earthdata without having to enter your credentials every time.

1. **Create a NASA Earthdata Account**:
   - If you don't already have an account, register at [NASA Earthdata Login](https://earthaccess.readthedocs.io/en/latest/tutorials/getting-started/). You'll need this account to access data using Earthaccess.

2. **Locate Your Home Directory**:
   - The `.netrc` file should be placed in your home directory. On Unix-like systems, this is typically `/home/your-username/`. On Windows, it might be `C:\Users\your-username\`.

3. **Create the .netrc File**:
   - Open a text editor and create a new file named `.netrc`.
   - Add the following lines, replacing `your-username` and `your-password` with your NASA Earthdata credentials:
     
     ```
     machine urs.earthdata.nasa.gov
     login your-username
     password your-password
     ```
   - Save the file to your home directory.

4. **Set File Permissions** (Unix-like systems):
   - For security reasons, the `.netrc` file should only be readable by you. Change the file permissions by running:
     
     ```bash
     chmod 600 ~/.netrc
     ```
   - This command makes the `.netrc` file readable and writable only by the file's owner.

5. **Verify the Configuration**:
   - You can verify that Earthaccess is using the `.netrc` file correctly by attempting to access NASA Earthdata through the library. If you're not prompted for credentials, the setup is successful.

By following these steps, you'll be able to use Earthaccess without manually entering your credentials each time. Make sure to keep your `.netrc` file secure, as it contains sensitive information.


## Usage

This project consists of a series of Jupyter notebooks that should ideally be run in a specific order to ensure all operations perform correctly, as some notebooks depend on the output from previous ones.

### 1. Running the Notebooks

To run the notebooks, you'll need to use Jupyter Lab or Jupyter Notebook. If you've followed the installation instructions, you should have Jupyter Lab installed in your environment.

1. **Start Jupyter Lab**:
   - Activate your conda environment:
     ```bash
     conda activate your-environment-name
     ```
   - Start Jupyter Lab by running:
     ```bash
     jupyter lab
     ```
   - This will open Jupyter Lab in your web browser.

2. **Open and Run the Notebooks**:
   - In Jupyter Lab, navigate to the folder containing the notebooks.
   - The notebooks are named in the order they should be run (e.g., `ScriptP1.ipynb`, `ScriptP2.ipynb`, etc.).
   - Open each notebook and run the cells in order by pressing `Shift + Enter` or by using the 'Run' menu at the top.

### 2. Notebook Dependencies

- **Part 1**: This is the starting point of the project and does not depend on any other notebooks.
- **Part 2**: Downloads satellite images and can be run independently of the others.
- **Part 3**: Depends on the outputs of both Part 1 and Part 2. Ensure these have been run successfully before starting Part 3.
- **Part 4**: For those who wish to skip directly to the analysis, the final output files are provided in the `Data_files` folder. However, running Parts 1 through 3 is recommended for a complete understanding of the process.

### 3. Tips for Running the Notebooks

- Save your work often by clicking the 'Save' icon or using the `Ctrl + S` (or `Cmd + S` on Mac) shortcut.
- If a notebook fails to run, check that you have executed all previous notebooks in the sequence.
- You can clear all outputs and rerun a notebook to ensure a fresh start by going to the 'Kernel' menu and selecting 'Restart Kernel and Clear All Outputs'.

By following these instructions, you should be able to run and interact with the Jupyter notebooks in this project successfully.

## Data Provided

This project includes a variety of data files essential for conducting the analysis. Below is a detailed description of each file and its purpose within the project:

### Python Functions File

- **my_functions.py**: A Python file containing custom functions used across multiple notebooks. Importing this file in your notebooks will allow you to access and reuse these functions, ensuring consistency and reducing code duplication.

### Shapefiles

Shapefiles are used to represent geospatial vector data. Each `.shp` file comes with several supplementary files like `.sbx`, `.dbf`, `.shx`, and `.cpg` that store indexing, attribute data, shape index, and character encoding information respectively. These files are necessary for the shapefile to be read and processed correctly.

- **AgriculturalPlots.shp**: Contains data on the location, number, and management type of agricultural plots within the Area of Interest (AOI). The file is pre-clipped to the AOI to minimize computational load.
- **Area_of_Interest.shp**: Defines the boundaries of the chosen AOI for the case study. This file can be used to limit the analysis to a specific region.
- **PAs.shp**: Provides the location and extent of Protected Areas in the Apulia region. The code demonstrates how to clip this data to the AOI.

### Raster Files

Raster files store pixel-based data and are accompanied by files like `.tfw` and `.tif.aux.xml` which contain georeferencing information and metadata. These files ensure that the raster data aligns correctly with the map coordinates.

- **habcon.tiff**: A Habitat Connectivity map used to extract connectivity values and perform zonal statistics. This map was previously created using Circuitscape as part of my [BSc dissertation project](https://www.linkedin.com/posts/mariavittoria-santarelli_sustainableagriculture-agroecological-community-activity-6954342396763504641-3Ndx?utm_source=share&utm_medium=member_desktop).

### Additional Contextual Data

Additional shapefiles are provided for context and visualization purposes, not directly used in the analysis:

- **nesting.shp**: Shows nesting sites of a specific bird species, provided by the ornithologist [Gianpasquale Chiatante](https://www.researchgate.net/profile/Gianpasquale-Chiatante). 
- **urban.shp**: Represents urban areas within the study region.

By utilizing these data files as instructed in the Jupyter notebooks, you can replicate the analysis and explore the geospatial trends within the Area of Interest.

Shapefile data on Agricultural Management Type, Protected Areas and Urban Areas was sourced and extracted from the land cover map of Apulia, available from the regional 
spatial database [(Banche Dati - S.I.T. - SIT Puglia (regione.puglia.it))](https://pugliacon.regione.puglia.it/web/sit-puglia-paesaggio/file-vettoriali).


## License

This project is licensed under the [MIT License](https://github.com/Mavisan6/Assignment/blob/main/LICENSE) - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
- [Automating GIS and remote sensing workflows with open python libraries](https://towardsdatascience.com/automating-gis-and-remote-sensing-workflows-with-open-python-libraries-e71dd6b049ee) by [Guilherme M. Iablonovski](https://guilhermeiablonovski.medium.com/)
- Production of Habitat Connectivity data was made possible thanks to the collaboration with the ornithologist [Gianpasquale Chiatante](https://www.researchgate.net/profile/Gianpasquale-Chiatante) during my [BSc Dissertation](https://www.linkedin.com/posts/mariavittoria-santarelli_sustainableagriculture-agroecological-community-activity-6954342396763504641-3Ndx?utm_source=share&utm_medium=member_desktop).
- [README Guide](https://coding-boot-camp.github.io/full-stack/github/professional-readme-guide/) by The Coding Bootcamp


