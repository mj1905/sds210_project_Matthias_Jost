#This file hosts all functions used inside the 5 jupyter notebooks.

import geopandas as gpd #type: ignore 
import matplotlib.pyplot as plt #type: ignore  
from pathlib import Path

# Functions Block 1: Checking crs, geometry and datetime
def check_and_convert_crs(gdf, epsg=2056):
    '''
    This function is used to check whether the loaded data is in the correct crs (default epsg=2056).
    If the data is already in the right projection, the function does nothing.
    If no crs is assigned yet, the function throws an error.
    If a wrong crs is assigned, it is converted to epsg=2056.

    Parameters:
    gdf: geodataframe
            The geodataframe we want to check for correct crs.
    epsg: int,
            The crs we want our data to be in. Default is 2056 (CH1903+ / LV95). 
    
    Returns:
    gdf: geodataframe
            The same geodataframe we put into the function. Unchanged if the crs was correct, reprojected if the crs was not correct.
    '''
    #Block 1 Checks if the data has a crs
    if gdf.crs is None:
        print("No CRS defined! Please assigne the correct CRS before you continue the analysis.")
        raise ValueError("No CRS defined!")
    
    #Block 2: Checks for the correct crs
    if gdf.crs.to_epsg() != epsg:
        gdf=gdf.to_crs(epsg=epsg)
        return gdf
    
    return gdf

def check_active_geometry_name(gdf):
    '''
    This function has the purpose to print the name of the active geometry of a geodataframe
    or to give an error message if none is defined.

    Parameters:
    gdf: geodataframe
        The geodataframe you want to check.

    Retruns:
    no return values    
    '''
    #Block 1: Checks whether a geometry exists
    if gdf.geometry is None:
        raise ValueError("No geometry defined!")
    
    #Block 2: checks checks whether the geometry column is one of the gdf columns
    if gdf.geometry.name not in gdf.columns:
        raise ValueError("Geometry column wrongly assigned!")

    else:
        print(f"The active geometry column of this geodataframe is called '{gdf.geometry.name}'.")
    return


# Function Block 2: Importing data 
def import_preprocessed_data(file_name, epsg=2056): 
    '''
    This function is designed to import the desired preprocessed data file into the jupyter notebook.
    The function automaticall checks whether the correct crs is assigned and if a geometry column
    exists by calling the two functions defined above.

    Parameters:
    file_name: string
        The name of the file you want to load. Don't forget to include the file ending!
    epsg: integer
        Number of the CRS that is desired. If none is given, EPSG=2056 is taken (ideal for Zurich).

    Outputs:
    gdf: geodataframe
        The loaded and checked geodataframe.
    '''
    #define import path
    import_path=Path(f"../data/processed/{file_name}")

    # "File exists check"
    if not import_path.exists():
        raise FileNotFoundError(f"File {file_name }not found! Please check the file name and the import path.")
    
    # If exists, loads and checks the file
    else:
        gdf=gpd.read_file(import_path)
        gdf=check_and_convert_crs(gdf, epsg=epsg)
        check_active_geometry_name(gdf)

    return gdf

def import_raw_data(file_name, layer=None, epsg=2056):   
    '''
    This function is designed to import the desired raw data file into the jupyter notebook.
    The function is designed to automatically check the crs and geometry of the raw data. 
    To do so, the two functions check_and_convert_crs() and check_active_geometry_name() are called within this function.

    Parameters:
    file_name: string
        The name of the file you want to load. Don't forget to include the file ending!
    layer: string
        Per default no layer is expected. If a certain layer of the data should be loaded, the layer needs to be specified.
    epsg: integer
        Number of the crs used. This is per default set to epsg=2056, the swiss corrdinate system.

    Outputs:
    gdf: geodataframe
        This gives the loaded gdf, checked for crs and geometry. You just need to assign it to a name.
    '''
    #define import path
    import_path=Path(f"../data/raw/{file_name}")

    #checking wheter the file exists
    if not import_path.exists():
        raise FileNotFoundError(f"File {file_name }not found! Please check the file name and the import path.")
    
    #if file exists: load and check the file
    else:
        gdf=gpd.read_file(import_path, layer=layer)
        gdf=check_and_convert_crs(gdf, epsg=epsg)
        check_active_geometry_name(gdf)
    
    return gdf
    

# Function Block 3: Exporting images and data
def export_result_to_png(file_name):
    '''
    The function has the purpose to export a final map or plot as a .png to the output folder.

    Parameters:
    file_name: string
        The file name you want to give your plot. You do not have to include the ending!
    
    Return Values:
    confirmation message: string

    '''
    #define output path
    output_path=Path("../outputs")
    output_path.mkdir(parents=True, exist_ok=True) #creates a directory if none exists
    full_path= output_path/f"{file_name}.png"

    #save the figure
    plt.savefig(full_path, bbox_inches="tight", dpi=300)

    return f"File was saved to {full_path}."



def export_processed_data(gdf, file_name, file_format="GPKG"):
    '''
    This function is designed to export the processed data to the data/processed/ folder. 

    Parameters:
    gdf: geodataframe
        The name of the geodataframe you want to export.
    file_name: string
        Name of the file you want to export, including its file format.
    file_format: string
        The file format you want to export your data to. Default is a .gpkg. 

    Return values:
    confirmation message: string
        The confirmation that the exported file is created in the desired folder.
    '''
    #define the export path
    export_path=Path(f"../data/processed")
    export_path.mkdir(parents=True, exist_ok=True) #creates the folders if they are missing
    full_path=export_path/f"{file_name}"

    # Data export
    gdf.to_file(full_path, driver=file_format)

    return f"The file '{file_name}' was exported to {full_path}."


