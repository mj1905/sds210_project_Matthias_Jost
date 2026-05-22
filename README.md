# Spatial Analysis of the ZüriWieNeu-reports
ZüriWieNeu is an online platform where residents of the City of Zurich can report issues connected with the cities infrastructure they encounter during their everyday lifes. This project conducts a spatial analysis, looking at how these reports are distributed over the city. Five specific, unrelated questions were adressed:   

1. Q1: Is the report density (reports/area) higher in the city centre then in the outskirts of Zurich?
2. Q2: Are Zurichs Ice Hockey Fans responsible for graffitis?
3. Q3: How do the reports of the category VBZ/ÖV cluster over the city?
4. Q4: Which categories of problems are most commonly reported in Zurich? 
5. Q5: What is the most common report category per neighborhood?

# Data Sources:
The raw data was obtained from the following websites. For all datasets multiple file formats are supported. This project consitently used GeoPackages (.gpkg).  
  
Neighborhood data: Statistische Quartiere, Stadt Zürich (2026). Retrieved from: https://www.stadt-zuerich.ch/geodaten/download/Statistische_Quartiere?format=10005 (Downloaded 19.05.2026, Settings: Ausschnitt: Stadt Zürich, Format: Geopackage (.gpkg)).  
  
ZüriWieNeu-reports: Züri wie neu, Stadt Zürich (2026). Retrieved from: https://www.stadt-zuerich.ch/geodaten/download/Zueri_wie_neu?format=10008 (Downloaded 19.05.2026, Settings: Ausschnitt: Stadt Zürich, Format: Geopackage (.gpkg)).  
  
Public Transport Lines: Linien des öffentlichen Verkehrs (OGD) (kantonaler Datensatz), Stadt Zürich (2025). Retrieved from: https://www.stadt-zuerich.ch/geodaten/download/108?format=128 (Downloaded 20.05.2026, Settings: Ausschnitt: Stadt Zürich, Format: Geopackage (.gpkg)).  
  
To ensure the notebooks to find the raw data files, the downloaded zip files have to be extracted into the data/raw/ folder. Please ensure that the raw data files are inside the folder mentioned.
Further, the files eventually have to be renamed:
* Neighborhood data: Rename the quartiere dataset to *quartiere.gpkg*.
* ZüriWieNeu-reports: Rename the dataset to *reports_ZHwieneu.gpkg*.
* Public Transport Line data: Rename the dataset to *public_transport_lines.gpkg*.

# Setup Instructions: 
The environment file can be found in the working directory and is named *sds-env2.yml*. The full list of packes needed can be found within that file. It runs on Python 3.12.12. The following command should allow to immediately generate a copy of the conda environment used:  
 *conda env create --name sds-env2-copy --file sds-env2.yml*  

The environment unfortunatelly includes much more packages than actually needed for this project, as I installed the whole bundle of geospatial packages intorduced in the Conda setup page of the cours website. I unfortunately didn't see the notice to include as little as possible until the whole project was already written. At that point it seemed to be to dangerous to "clean up" the conda environment. 

Further, I used Anaconda Promt to manage the environment and Visual Study Code to code. 

# Working directory setup:
```
sds210_project_Matthias_Jost/    # This is the working directory!   
├── README.md                    # The file you are reading right now  
├── .gitignore                   # List of (large) files that shouldn't sync  
├── sds-env2.yml                 # The list of required Python packages  
├── data/                        # The raw and processed datasets  
│   ├── raw/  
│   └── processed/  
├── notebooks/                   # The Jupyter Notebooks  
├── scripts/                     # Your Jupyter Notebooks  
└── outputs/                     # Your final exported maps and charts  
```
Visualisation of the working directory derived from: https://hendrikwulf.github.io/sds210-jb/book/projects/repository/ 

# Execution Order:
First, the data folders have to be added manually to the working directory. Subsequently, the data mentioned above has to be downloaded to the correct folder and then subsequently renamed as explained under Data Sources. 
  
Please also ensure that the *functions_zh_wie_neu.py* script is in the correct folder (scripts/), else the code will fail in the first cell. 

Before you start, don't forget to set up the environment.

Then, execute the notebooks one for one. First, run the *raw_data_preprocessing.ipynb* notebook, followed by the four notebooks adressing the questions (Q4 and Q5 are answered together in the last notebook). It is recommended to run the four question notebooks in the following order: *Q1_area_dependency.ipynb*, *Q2_ice_hockey_and_graffiti.ipynb*, *Q3_public_transport_problems.ipynb* and *Q4_category_with_most_reports.ipynb*. Still, as the questions are independent of each other, the execution order of these four notebooks is not important.

Note that the file paths in the notebooks are relative but they depend on the fact, that the notebooks are exectuted in the notbooks/ folder.

# Small note regarding the Kernel
Occasionally, the Kernel fails to import all packages and dies. This somehow happened with all environments I used over the past few months. However, should this happen, I recommend restarting the Kernel. If that doesn't help, closing and reopening VS Code always worked. 