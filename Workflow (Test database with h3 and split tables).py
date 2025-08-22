import arcpy

# Allow overwriting of outputs
arcpy.env.overwriteOutput = True

# Set workspace
gdb_path = r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb"
arcpy.env.workspace = gdb_path

#PROJECT AND CLIP RASTERS
#Project 2018 LULC raster, in this case, UTM 38S was used
arcpy.management.ProjectRaster(
    in_raster=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\LULC_2018",
    out_raster=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\LULC_2018_Projected",
    out_coor_system='PROJCS["WGS_1984_UTM_Zone_38S",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",45.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    resampling_type="NEAREST",
    cell_size="19,3159960118452 19,3159960118452",
    geographic_transform=None,
    Registration_Point=None,
    in_coor_system='PROJCS["WGS_1984_UTM_Zone_38S",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",45.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    vertical="NO_VERTICAL"
)

#Clip to AOI using "Extract by Mask"
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["WGS_1984_UTM_Zone_38S",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",45.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]', snapRaster="LULC_2018_Projected", cellSize="LULC_2018_Projected", mask="SustainableAreaforUse_10kmBuffer", scratchWorkspace=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb"):
    out_raster = arcpy.sa.ExtractByMask(
        in_raster="LULC_2018_Projected",
        in_mask_data="SustainableAreaforUse_10kmBuffer",
        extraction_area="INSIDE",
        analysis_extent='680285.8747 7225126.7571 733771.2361 7306607.6404 PROJCS["WGS_1984_UTM_Zone_38S".GEOGCS["GCS_WGS_1984".DATUM["D_WGS_1984".SPHEROID["WGS_1984".6378137.0.298.257223563]].PRIMEM["Greenwich".0.0].UNIT["Degree".0.0174532925199433]].PROJECTION["Transverse_Mercator"].PARAMETER["False_Easting".500000.0].PARAMETER["False_Northing".10000000.0].PARAMETER["Central_Meridian".45.0].PARAMETER["Scale_Factor".0.9996].PARAMETER["Latitude_Of_Origin".0.0].UNIT["Meter".1.0]]'
    )
    out_raster.save(r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\LULC_2018_Clipped")

#Project 2024 LULC raster
arcpy.management.ProjectRaster(
    in_raster=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\LULC_2024",
    out_raster=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\LULC_2024_Projected",
    out_coor_system='PROJCS["WGS_1984_UTM_Zone_38S",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",45.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    resampling_type="NEAREST",
    cell_size="19,3160341194304 19,3160341194304",
    geographic_transform=None,
    Registration_Point=None,
    in_coor_system='PROJCS["WGS_1984_UTM_Zone_38S",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",45.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]',
    vertical="NO_VERTICAL"
)

#Clip to AOI using "Extract by Mask", this raster must be aligned to the clipped 2018 raster
with arcpy.EnvManager(scratchWorkspace=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb"):
    out_raster = arcpy.sa.ExtractByMask(
        in_raster="LULC_2024_Projected",
        in_mask_data="SustainableAreaforUse_10kmBuffer",
        extraction_area="INSIDE",
        analysis_extent='680285.8747 7225126.7571 733771.2361 7306607.6404 PROJCS["WGS_1984_UTM_Zone_38S".GEOGCS["GCS_WGS_1984".DATUM["D_WGS_1984".SPHEROID["WGS_1984".6378137.0.298.257223563]].PRIMEM["Greenwich".0.0].UNIT["Degree".0.0174532925199433]].PROJECTION["Transverse_Mercator"].PARAMETER["False_Easting".500000.0].PARAMETER["False_Northing".10000000.0].PARAMETER["Central_Meridian".45.0].PARAMETER["Scale_Factor".0.9996].PARAMETER["Latitude_Of_Origin".0.0].UNIT["Meter".1.0]]'
    )
    out_raster.save(r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\LULC_2024_Clipped")


# GRID SUMMARY FEATURE LAYER
#Use generate tessellation tool to generate h3 hexagona (resolution 9: 0,1 Km2) specify size, shape etc

arcpy.management.GenerateTessellation(
    Output_Feature_Class=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_res9",
    Extent='680285.8747 7225126.7571 733771.2361 7306607.6404 PROJCS["WGS_1984_UTM_Zone_38S".GEOGCS["GCS_WGS_1984".DATUM["D_WGS_1984".SPHEROID["WGS_1984".6378137.0.298.257223563]].PRIMEM["Greenwich".0.0].UNIT["Degree".0.0174532925199433]].PROJECTION["Transverse_Mercator"].PARAMETER["False_Easting".500000.0].PARAMETER["False_Northing".10000000.0].PARAMETER["Central_Meridian".45.0].PARAMETER["Scale_Factor".0.9996].PARAMETER["Latitude_Of_Origin".0.0].UNIT["Meter".1.0]]',
    Shape_Type="H3_HEXAGON",
    Size="28606880.1316 Unknown",
    Spatial_Reference='PROJCS["WGS_1984_UTM_Zone_38S",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",10000000.0],PARAMETER["Central_Meridian",45.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]];-5120900 1900 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision',
    H3_Resolution=9
)

#Clip grid to AOI
arcpy.analysis.Clip(
    in_features="h3_res9",
    clip_features="SustainableAreaforUse_10kmBuffer",
    out_feature_class=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_res9_clipped",
    cluster_tolerance=None
)




#ADD MANAGEMENT ZONES
#Management zone boundaries must be in the gdb e.g core zone, sustainable use zone

#Core Zone

# Make a temporary feature layer from the clipped grid
arcpy.management.MakeFeatureLayer(
    "h3_res9_clipped",
    "grid_layer"
)

#Spatial join to find hexagons that fall within the core zone boundary 
arcpy.analysis.SpatialJoin(
    target_features="grid_layer",
    join_features="Core_zone",
    out_feature_class=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_res9_clipped_SpatialJoin",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping='GRID_ID "GRID_ID" true true false 12 Text 0 0,First,#,h3_res9_clipped,GRID_ID,0,11;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,Grid_Summary_model_Clip,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,Grid_Summary_model_Clip,Shape_Area,-1,-1',
    match_option="LARGEST_OVERLAP",
    search_radius=None,
    distance_field_name="",
    match_fields=None
)


# Make a temporary layer from the spatial join output
arcpy.management.MakeFeatureLayer(
    r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_res9_clipped_SpatialJoin",
    "core_zone_layer"
)

#Add field for the core zone
arcpy.management.AddField(
    in_table="core_zone_layer",
    field_name="core_zone",
    field_type="TEXT",
    field_precision=None,
    field_scale=None,
    field_length=255,
    field_alias="Core Zone",
    field_is_nullable="NULLABLE",
    field_is_required="NON_REQUIRED",
    field_domain=""
)


# Set all empty strings in the newly created field to NULL 
arcpy.management.CalculateField(
    in_table="core_zone_layer",
    field="core_zone",
    expression="None",
    expression_type="PYTHON3"
)

#Select hexagons that fall within the core zone based on join values (join = 1)
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="core_zone_layer",
    selection_type="NEW_SELECTION",
    where_clause="Join_Count = 1",
    invert_where_clause=None
)

#Populate hexagons that fall within core zone (join count = 1) with "True"
arcpy.management.CalculateField(
    in_table="core_zone_layer",
    field="core_zone",
    expression='"True"',
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)


#Select hexagons that fall outside the core zone based on join values (join = 0)
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="core_zone_layer",
    selection_type="NEW_SELECTION",
    where_clause="Join_Count = 0 AND core_zone IS NULL",
    invert_where_clause=None
)

#Populate hexagons that fall outside core zone (join count = 0) with "False"
arcpy.management.CalculateField(
    in_table="core_zone_layer",
    field="core_zone",
    expression='"False"',
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

#Clear selection (Very NB!)
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="core_zone_layer",
    selection_type="CLEAR_SELECTION"
)

# SUSTAINABLE USE ZONE

arcpy.analysis.SpatialJoin(
    target_features="core_zone_layer",
    join_features="Sustainable_Area_for_Use_1",
    out_feature_class=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_res9_clipped_SpatialJoin1",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping='TARGET_FID "TARGET_FID" true true false 4 Long 0 0,First,#,h3_res9_clipped_SpatialJoin,TARGET_FID,-1,-1;GRID_ID "GRID_ID" true true false 12 Text 0 0,First,#,Grid_Summary_mod_SpatialJoin,GRID_ID,0,11;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,Grid_Summary_mod_SpatialJoin,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,Grid_Summary_mod_SpatialJoin,Shape_Area,-1,-1;core_zone "Core Zone" true true false 255 Text 0 0,First,#,Grid_Summary_mod_SpatialJoin,core_zone,0,254;sustainable_use_zone "Sustainable Use Zone" true true false 255 Text 0 0,First,#,Grid_Summary_mod_SpatialJoin,sustainable_use_zone,0,254',
    match_option="LARGEST_OVERLAP",
    search_radius=None,
    distance_field_name="",
    match_fields=None
)


# Make a temporary layer from this output
arcpy.management.MakeFeatureLayer(
    r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_res9_clipped_SpatialJoin1",
    "sustainable_layer"
)

#Add field for sustainable use zone
arcpy.management.AddField(
    in_table="sustainable_layer",
    field_name="sustainable_use_zone",
    field_type="TEXT",
    field_precision=None,
    field_scale=None,
    field_length=255,
    field_alias="Sustainable Use Zone",
    field_is_nullable="NULLABLE",
    field_is_required="NON_REQUIRED",
    field_domain=""
)

# Set all empty strings to NULL
arcpy.management.CalculateField(
    in_table="sustainable_layer",
    field="sustainable_use_zone",
    expression="None",
    expression_type="PYTHON3"
)

#Select hexagons that fall within the sustainable use zone based on join count (Join count = 1)
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="sustainable_layer",
    selection_type="NEW_SELECTION",
    where_clause="Join_Count = 1",
    invert_where_clause=None
)

#Populate hexagons that fall within the sustainable use zone
arcpy.management.CalculateField(
    in_table="sustainable_layer",
    field="sustainable_use_zone",
    expression='"True"',
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

#Select hexagons that fall outside the sustainable use zone based on join count (Join count = 0)
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="sustainable_layer",
    selection_type="NEW_SELECTION",
    where_clause="Join_Count = 0 AND sustainable_use_zone IS NULL",
    invert_where_clause=None
)

#Populate hexagons that fall outside the sustainable use zone
arcpy.management.CalculateField(
    in_table="sustainable_layer",
    field="sustainable_use_zone",
    expression='"False"',
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

#Clear selection
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="sustainable_layer",
    selection_type="CLEAR_SELECTION"
)

## ADD MANAGEMENT ZONE FIELD

#Add field
arcpy.management.AddField(
    in_table="sustainable_layer",
    field_name="management_zone",
    field_type="TEXT",
    field_precision=None,
    field_scale=None,
    field_length=255,
    field_alias="Management Zone",
    field_is_nullable="NULLABLE",
    field_is_required="NON_REQUIRED",
    field_domain=""
)

# Set all empty strings to NULL
arcpy.management.CalculateField(
    in_table="sustainable_layer",
    field="management_zone",
    expression="None",
    expression_type="PYTHON3"
)

#Select hexagons where sustainable use zone field = true
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="sustainable_layer",
    selection_type="NEW_SELECTION",
    where_clause="sustainable_use_zone = 'True'",
    invert_where_clause=None
)

#Populate management zone field with "Sustainable Use Zone"
arcpy.management.CalculateField(
    in_table="sustainable_layer",
    field="management_zone",
    expression='"Sustainable Use Zone"',
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Select Core Zone next (overwrites Sustainable Use Zone if needed)
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="sustainable_layer",
    selection_type="NEW_SELECTION",
    where_clause="core_zone = 'True'",
    invert_where_clause=None
)


#Populate management zone field with "Core Zone"
arcpy.management.CalculateField(
    in_table="sustainable_layer",
    field="management_zone",
    expression='"Core Zone"',
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

#Select hexagons where management zone is null
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="sustainable_layer",
    selection_type="NEW_SELECTION",
    where_clause="management_zone IS NULL",
    invert_where_clause=None
)

#Populate hexagons with "None"
arcpy.management.CalculateField(
    in_table="sustainable_layer",
    field="management_zone",
    expression='"None"',
    expression_type="PYTHON3",
    code_block="",
    field_type="TEXT",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# Clear selection
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="sustainable_layer",
    selection_type="CLEAR_SELECTION"
)

##Creating a total area column for each grid, this is used in a percentage claculation for area later

#List rasters in GDB to refresh
rasters = arcpy.ListRasters()
print("Rasters in GDB:", rasters)



# Save the feature layer as a new permanent feature class
sustainable_fc = r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_managementzones"
arcpy.management.CopyFeatures("sustainable_layer", sustainable_fc)



arcpy.sa.ZonalStatisticsAsTable(
    in_zone_data=sustainable_fc,
    zone_field="GRID_ID",
    in_value_raster="LULC_2018_Clipped",
    out_table=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\LC_2018_GridArea",
    ignore_nodata="DATA",
    statistics_type="ALL",
    process_as_multidimensional="CURRENT_SLICE",
    percentile_values=[90],
    percentile_interpolation_type="AUTO_DETECT",
    circular_calculation="ARITHMETIC",
    circular_wrap_value=360,
    out_join_layer=None
)

arcpy.management.JoinField(
    in_data=sustainable_fc,
    in_field="GRID_ID",
    join_table="LC_2018_GridArea",
    join_field="GRID_ID",
    fields="AREA",
    fm_option="NOT_USE_FM",
    field_mapping=None,
    index_join_fields="NO_INDEXES"
)

##Rename joined "AREA" field
arcpy.management.AlterField(
    in_table=sustainable_fc,
    field="AREA",
    new_field_name="lc_gridarea_2018_m2",
    new_field_alias="LC Grid Area 2018 (m2)",
    field_type="",
    field_length=8,
    field_is_nullable="NULLABLE",
    clear_field_alias="DO_NOT_CLEAR"
)



arcpy.sa.ZonalStatisticsAsTable(
    in_zone_data=sustainable_fc,
    zone_field="GRID_ID",
    in_value_raster="LULC_2024_Clipped_CopyRaster",
    out_table=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\LC_2024_GridArea",
    ignore_nodata="DATA",
    statistics_type="ALL",
    process_as_multidimensional="CURRENT_SLICE",
    percentile_values=[90],
    percentile_interpolation_type="AUTO_DETECT",
    circular_calculation="ARITHMETIC",
    circular_wrap_value=360,
    out_join_layer=None
)



arcpy.management.JoinField(
    in_data=sustainable_fc,
    in_field="GRID_ID",
    join_table="LC_2024_GridArea",
    join_field="GRID_ID",
    fields="AREA",
    fm_option="NOT_USE_FM",
    field_mapping=None,
    index_join_fields="NO_INDEXES"
)


arcpy.management.AlterField(
    in_table=sustainable_fc,
    field="AREA",
    new_field_name="lc_grid_area_2024_m2",
    new_field_alias="LC Grid Area 2024 (m2)",
    field_type="",
    field_length=8,
    field_is_nullable="NULLABLE",
    clear_field_alias="DO_NOT_CLEAR"
)


#These two fields: (LC Grid Area 2018 (m2) and LC Grid Area 2024 (m2) should have the same area in both columns given they were projected, clipped and aligned correctly)


# remove unnessary fields
arcpy.management.DeleteField(
    in_table="h3_managementzones",
    drop_field="Join_Count;TARGET_FID;TARGET_FID_1",
    method="DELETE_FIELDS"
)


# Separate tables for lc 2018 and 2024
arcpy.management.CopyFeatures(
    in_features="h3_managementzones",
    out_feature_class=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_lc_2018",
    config_keyword="",
    spatial_grid_1=None,
    spatial_grid_2=None,
    spatial_grid_3=None
)


arcpy.management.CopyFeatures(
    in_features="h3_managementzones",
    out_feature_class=r"C:\Users\JanineStruwig\Documents\ArcGIS\Projects\FZS\Test.gdb\h3_lc_2024",
    config_keyword="",
    spatial_grid_1=None,
    spatial_grid_2=None,
    spatial_grid_3=None
)

## Three scripts for area extraction (create individual class rasters, zonal statisistics on each, )
##Grid Summary AOI and the land cover classes will be different and need to be specified for each land cover class




