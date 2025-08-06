# analytics_engine.py
# Core logic for the Analytics Engine from the "Citizen Centered Climate Intelligence" paper.
# This script demonstrates how environmental scores are calculated for urban road segments.

import pandas as pd
import geopandas as gpd
import numpy as np

def calculate_environmental_scores(roads_gdf: gpd.GeoDataFrame, trees_gdf: gpd.GeoDataFrame, buffer_size_meters: int = 10):
    """
    Calculates environmental scores for road segments based on nearby trees.

    Args:
        roads_gdf: A GeoDataFrame of road linestrings with a unique 'segment_id' column.
        trees_gdf: A GeoDataFrame of tree points with 'canopy_dia_m', 'CO2_sequestered_kg', 
                   and 'botanical_name' columns.
        buffer_size_meters: The distance around roads to consider trees.

    Returns:
        A GeoDataFrame of roads with calculated raw and normalized environmental scores.
    """
    print(f"Performing vectorized analysis with a {buffer_size_meters}-meter buffer...")

    # Ensure both GeoDataFrames use the same projected CRS for accurate buffer operations
    if roads_gdf.crs != trees_gdf.crs:
        print("Warning: CRS mismatch. Re-projecting trees to match roads CRS.")
        trees_gdf = trees_gdf.to_crs(roads_gdf.crs)

    # 1. Create a buffer around each road segment
    road_buffers = roads_gdf[['segment_id', 'geometry']].copy()
    road_buffers['geometry'] = road_buffers.geometry.buffer(buffer_size_meters)
    road_buffers['buffer_area_sq_m'] = road_buffers.geometry.area
    
    # 2. Pre-calculate tree properties
    trees_gdf['canopy_area_sq_m'] = np.pi * (trees_gdf['canopy_dia_m'] / 2)**2

    # 3. Perform a high-performance spatial join to find trees within each road's buffer
    joined_gdf = gpd.sjoin(trees_gdf, road_buffers, how='inner', predicate='within')
    
    # 4. Aggregate tree data for each unique road segment
    agg_funcs = {
        'canopy_area_sq_m': pd.NamedAgg(column='canopy_area_sq_m', aggfunc='sum'),
        's_co2_total': pd.NamedAgg(column='CO2_sequestered_kg', aggfunc='sum'),
        's_bio_count': pd.NamedAgg(column='botanical_name', aggfunc='nunique')
    }
    eco_scores = joined_gdf.groupby('segment_id').agg(**agg_funcs)
    
    # 5. Merge aggregated scores back to the original road data
    roads_with_scores = roads_gdf.merge(eco_scores, on='segment_id', how='left').fillna(0)
    
    # 6. Calculate raw scores
    roads_with_scores['s_canopy'] = roads_with_scores['canopy_area_sq_m'] / road_buffers['buffer_area_sq_m']
    roads_with_scores['s_co2'] = roads_with_scores['s_co2_total'] / roads_with_scores.geometry.length
    roads_with_scores['s_bio'] = np.log1p(roads_with_scores['s_bio_count']) # Use log1p for stability
    
    # 7. Normalize scores using Quantile Transformation (robust to outliers)
    for col in ['s_canopy', 's_co2', 's_bio']:
        roads_with_scores[f'{col}_norm'] = roads_with_scores[col].rank(pct=True)

    # 8. Calculate final composite scores
    # Static Environmental Quality (SEQ) Score for vehicular routing
    roads_with_scores['static_eqs'] = (0.5 * roads_with_scores['s_canopy_norm']) + \
                                      (0.3 * roads_with_scores['s_co2_norm']) + \
                                      (0.2 * roads_with_scores['s_bio_norm'])

    # Serenity Score for pedestrian/recreational routing
    roads_with_scores['serenity_score'] = (0.7 * roads_with_scores['s_canopy_norm']) + \
                                          (0.3 * roads_with_scores['s_bio_norm'])
                                          
    return roads_with_scores

# --- Example Usage ---
# In a real scenario, roads_gdf and trees_gdf would be loaded from a database or file.
# Here we create dummy data to demonstrate the function's use.
if __name__ == '__main__':
    from shapely.geometry import LineString, Point

    print("\n--- Demonstrating Environmental Score Calculations ---")
    
    # Create a dummy GeoDataFrame for roads
    roads_data = {'segment_id': [1, 2], 'geometry': [LineString([(0, 0), (100, 0)]), LineString([(0, 50), (100, 50)])]}
    roads_gdf = gpd.GeoDataFrame(roads_data, crs="EPSG:32643")
    
    # Create a dummy GeoDataFrame for trees
    trees_data = {
        'canopy_dia_m': [10, 8, 12, 5],
        'CO2_sequestered_kg': [50, 30, 70, 15],
        'botanical_name': ['Ficus religiosa', 'Azadirachta indica', 'Ficus religiosa', 'Peltophorum pterocarpum'],
        'geometry': [Point(25, 2), Point(75, -1), Point(25, 48), Point(75, 51)]
    }
    trees_gdf = gpd.GeoDataFrame(trees_data, crs="EPSG:32643")

    # Run the main calculation function
    final_roads = calculate_environmental_scores(roads_gdf, trees_gdf)
    
    print("\n--- Final Results ---")
    print("Columns of interest:")
    print(final_roads[['segment_id', 'static_eqs', 'serenity_score', 's_canopy_norm', 's_co2_norm', 's_bio_norm']].round(4))