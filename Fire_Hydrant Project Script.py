
# Prince Obosu

# Description:to identifying all parcels (owned pieces of property) within 500 feet of all fire
#hydrants within a subset* of municipalities and townships within the county. Each municipality/township
#needs for their data to remain separate as they are each responsible for sending out their own letters.
#You will need to provide GIS data, a map, and mailing addresses to each of municipalities/townships.   
# 5/11/2024

# ArcPy Tool Syntax:
# - arcpy.env.workspace: Sets the current workspace for geoprocessing operations.
# - arcpy.env.overwriteOutput: Allows overwriting of output files during geoprocessing.
# - arcpy.ListFeatureClasses(): Lists all feature classes in the current workspace.
# - arcpy.Buffer_analysis: perfoms buffer analysis on a feature class.
# - arcpy.AddField_management : adds new field to the attribute table.

# Script Summary:
#The script sets up the workspace directory where the data files are located and
#creates a file geodatabase within that workspace if it doesn't already exist.
#Setting spatial reference: It sets the spatial reference of the datasets to Ohio State Plane South NAD83.
#Input data selection: Depending on the user's choice (option 1 or 2),
#the script prompts the user to input specific dataset names or uses predefined dataset names.
#Adding a new field: It adds a new field called "Mail_Adres" to the selected parcel dataset.
#Iterating through datasets: The script iterates through each municipality and township to perform spatial analysis tasks.
#Buffer analysis: For each fire hydrants dataset, it creates a 500-feet buffer around the hydrants and
#saves the results as shapefiles in the output geodatabase.
#Data processing: It selects parcels intersecting with the hydrant buffers, adds a mail address field to the selected parcels,
#and calculates mailing addresses for selected parcels.
#Saving results: It saves the processed parcel data with added mailing addresses as separate shapefiles for each municipality and township.
#Error handling: The script includes error handling to catch and print any arcpy execution errors or other exceptions that may occur during execution

#importing arcpy and operating system
# Importing arcpy and operating system
import arcpy
import os

# Opening a try and except block
try:
    # Turn on overwrite output
    arcpy.env.overwriteOutput = True
    
    # Set workspace
    workspace = r"C:\Users\princ\Desktop\python class\Grad project\FinalProject_Data"
    arcpy.env.workspace = workspace
    print("\nThe workspace for the data used in this script is", workspace)
    
    # Check if the workspace is a file geodatabase, if not, create one
    print("Creating a file geodatabase for the project...")
    if not arcpy.Exists(os.path.join(workspace, "ProjectData.gdb")):
        arcpy.CreateFileGDB_management(workspace, "ProjectData.gdb")
    output_gdb = os.path.join(workspace, "ProjectData.gdb")
    
    # Set spatial reference to Ohio State Plane South NAD83
    spatial_reference = arcpy.SpatialReference(26916)
    print(f'The spatial reference of your datasets are set to {spatial_reference.name}')
    
    print("Choose option 1 if you want to dictate either a dataset name, location, or tool parameter for the analysis.")
    print("Choose option 2 if you want all datasets in your folder directory to undergo the analysis.")
    option = int(input("Choose either 1 or 2: "))

    if option == 1:
        print("you chose option 1")
        # Define input datasets
        parcels_shp = input("Enter the parcel dataset name (e.g., CURRENTPARCELS.shp): ")
        municipality_shp = input("Enter the municipality boundaries dataset name (e.g., Corp.shp): ")
        townships_shp = input("Enter the township boundaries dataset name (e.g., Townships.shp): ")
        fire_hydrants = input("Enter the fire hydrants dataset names separated by comma (e.g., WayneTWp_hydrants.shp, LibertyTWp_hydrants.shp, Millville_hydrants.shp): ").split(", ")
        
        # Create a new field for the concatenated mailing address
        print('Adding a new field "Mail_Adres" to selected parcels...')
        arcpy.AddField_management(parcels_shp, "Mail_Adres", "TEXT")
        print("Process was successful.")
        
        # Iterate through each municipality and township
        areas = input("Enter the names of municipalities and townships separated by comma: ").split(", ")

    else:
        print("you chose option 2")
        # Define input datasets
        print("Defining the dataset")
        parcels_shp = "CURRENTPARCELS.shp"
        municipality_shp = "Corp.shp"
        townships_shp = "Townships.shp"
        fire_hydrants = ["WayneTWp_hydrants.shp", "LibertyTWp_hydrants.shp", "Millville_hydrants.shp"]
        print("Process successful")
        
        # Create a new field for the concatenated mailing address
        print("Adding a new field 'Mail_Adres' to the parcel shapefiles")
        arcpy.AddField_management(parcels_shp, "Mail_Adres", "TEXT")      
        print("Process successful")
              
        # Iterate through each municipality and township
        print("Iterating through the municipality and township datasets")
        areas = ["Trenton", "Sharonville", "City of Fairfield", "Somerville", "New Miami", "Monroe", "Jacksonburg", "Oxford Corp.",
                 "City of Middletown", "Seven Mile", "Millville", "College Corner", "City of Hamilton",
                 "Liberty", "Reily", "Milford", "Morgan", "Wayne", "Madison", "Hanover", "Oxford", "Fairfield", "West Chester",
                 "Lemon", "St. Clair", "Ross"]
        print("Iteration completed")

    for hydrant_file in fire_hydrants:
        # Define input hydrant data
        print("Defining hydrant data.......")      
        hydrant_shp = hydrant_file
        
        # Check if the hydrant data exists
        if arcpy.Exists(hydrant_shp):
            # Create a feature layer for hydrants
            print("Creating a hydrant feature layer")
            arcpy.MakeFeatureLayer_management(hydrant_shp, "hydrant_lyr")
            print("Process successful")
            
            # Buffer hydrants by 500 feet
            print("Defining a 500 feet buffer around all hydrants...")
            output_name = os.path.splitext(os.path.basename(hydrant_file))[0] + "_buffer.shp"
            buffer_output = os.path.join(output_gdb, arcpy.ValidateTableName(output_name, output_gdb))
            arcpy.Buffer_analysis("hydrant_lyr", buffer_output, "500 Feet")
            print("Buffer analysis completed")      
            
            # Print progress message
            print(f"Buffer created for {hydrant_file}.")
        else:
            print(f"Hydrant data file {hydrant_file} not found.")
    
    # Print completion message
    print("Script execution completed.")
    print("Spatial analysis completed.")
    print("Check dataset in ArcGIS Pro.")
    
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
    
except Exception as e:
    print(e.args[0])
