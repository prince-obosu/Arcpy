#_UpdateCursor_Activity_Script.py
# Prince Obosu

# The purpose of this script is to practice using the Arcpy UpdateCursor to access
# and fetch records from an existing GIS dataset
# 5/3/2024

# This script Update Cursor to create a new text field that is then populated by the concatenation of the Month, Day, Year fields.

# Tool syntax for this script:
# Update Cursor
#arcpy.da.UpdateCursor(in_table,field_name, (where_clause), (spatial_reference), (explode_to_points), (sql_clause))

# Set up Try/Except block
# Set up Try/Except block
try:
    # Import arcpy and sys modules
    import arcpy
    import sys

    # Turn on overwrite output
    arcpy.overwriteOutput = True

    # Set workspace
    arcpy.env.workspace = r"C:\Users\princ\Desktop\python class\module_16\PythonScripting_Ex08_Data\Ex08"

    # Check if alaska shapefile exists - if not, end the script
    if arcpy.Exists("alaska.shp"):
        print("Data needed for script exists. Script will continue.")
    else:
        sys.exit("Alaska shapefile does not exist in your current workspace.")

    # Create a backup copy of the dataset
    if arcpy.Exists("alaska_original.shp"):
        print("Backup of data already exists.")
    else:
        arcpy.CopyFeatures_management("alaska.shp", "alaska_original.shp")
        print("Original data has been saved to a backup copy.")

    # Add a new field called "SEASONS" to alaska.shp
    arcpy.AddField_management("alaska.shp", "SEASONS", "TEXT")
    print("SEASONS field has been added to the dataset")

    # Update Cursor to update all rows to have SEASONS be a concatenation of the MONTH, DAY, YEAR fields
    with arcpy.da.UpdateCursor("alaska.shp", ["SEASONS", "MONTH_ADM", "DAY_ADM", "YEAR_ADM"]) as cursor:
        for row in cursor:
            row[0] = str(row[1]) + "-" + str(row[2]) + "-" + str(row[3])  # Concatenate MONTH, DAY, YEAR
            cursor.updateRow(row)

    print("Data has been updated and can be found here: ", arcpy.env.workspace)
    print("Please load the data into ArcPro to verify that the data has been updated")

    # Turn off overwrite output
    arcpy.overwriteOutput = False

except Exception as e:
    print("An error occurred in your script:")
    print(e)
