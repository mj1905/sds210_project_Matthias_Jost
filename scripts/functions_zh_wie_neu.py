#This file hosts all functions used inside the 5 jupyter notebook.
import geopandas as gpd #type: ignore 
import matplotlib.pyplot as plt #type: ignore 
import numpy as np #type: ignore 
import cmcrameri.cm as cmc #type: ignore 
from pathlib import Path

def import_preprocessed_data(file_name): #evtl put the other two functions inside this  
    '''
    This function is designed to load the desired processed file into the jupyter notebook.

    Parameters:
    file_name: string
        The name of the file you want to load. Don't forget to include the file ending!

    Outputs:
    gpd.read_file(import_path): function
        This gives the loaded gdf. You just need to assign it to a name.
    '''
    import_path=Path(f"../data/processed/{file_name}")

    if not import_path.exists():
        print(f"File {file_name }not found! Please check the file name and the import path.")
        return
    return gpd.read_file(import_path)

def import_raw_data(file_name): #evtl put the other two functions inside this  
    '''
    This function is designed to load the desired raw data file into the jupyter notebook.

    Parameters:
    file_name: string
        The name of the file you want to load. Don't forget to include the file ending!

    Outputs:
    gpd.read_file(import_path): function
        This gives the loaded gdf. You just need to assign it to a name.
    '''
    import_path=Path(f"../data/raw/{file_name}")

    if not import_path.exists():
        print("File not found! Please check the file name and the import path.")
    return gpd.read_file(import_path)

def export_result_to_png(file_name):
    '''
    The function has the purpose to export a final map or plot as a .png to the output folder.

    Parameters:
    file_name: string
        The file name you want to give your plot. You do not have to include the ending!
    
    Return Values:
    string: confirmation message 

    '''
    #define the output path
    output_path=Path("../outputs")
    output_path.mkdir(parents=True, exist_ok=True)
    full_path= output_path/f"{file_name}.png"

    #then save the figure
    plt.savefig(full_path, bbox_inches="tight", dpi=300)

    return f"File was saved to {full_path}."