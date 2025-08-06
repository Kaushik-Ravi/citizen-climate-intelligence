# photogrammetry_model.py
# Core photogrammetric logic for the "Citizen Centered Climate Intelligence" paper.
# This script demonstrates the underlying mathematical model for dendrometry using a standard smartphone camera.

import math

def calculate_camera_constant(sensor_width_mm: float, focal_length_mm: float) -> float:
    """
    Calculates the camera's intrinsic constant (C), a unitless ratio.
    """
    if focal_length_mm <= 0:
        raise ValueError("Focal length must be a positive number.")
    return sensor_width_mm / focal_length_mm

def calculate_scale_factor(camera_constant: float, distance_to_object_m: float, image_width_px: int) -> float:
    """
    Calculates the scale factor (e.g., meters per pixel), which is the critical
    value for converting pixel measurements to real-world units.
    """
    if image_width_px <= 0:
        raise ValueError("Image width in pixels must be a positive number.")
    
    # Real-world width of the scene captured by the camera at a given distance
    scene_width_m = camera_constant * distance_to_object_m
    
    # Scale factor in meters per pixel
    return scene_width_m / image_width_px

def measure_dimension_from_pixels(scale_factor_m_per_px: float, dimension_in_pixels: int) -> float:
    """
    Converts a measurement in pixels to a real-world measurement in meters.
    """
    return scale_factor_m_per_px * dimension_in_pixels

# --- Example Usage ---
if __name__ == '__main__':
    # This example demonstrates a full workflow as described in the paper.
    
    # 1. Known camera parameters (from EXIF data or user calibration)
    PHONE_SENSOR_WIDTH_MM = 6.17
    PHONE_FOCAL_LENGTH_MM = 4.25
    
    # 2. Measurement scenario
    distance_m = 12.5  # Citizen stands 12.5 meters away from a tree
    photo_width_px = 4032  # The photo has a resolution width of 4032 pixels
    
    # 3. Measurements taken from the photo (in pixels)
    tree_height_in_pixels = 1850
    canopy_width_in_pixels = 1400
    dbh_in_pixels = 85

    print("--- Demonstrating Tree Measurement Calculations ---")
    
    # Step 1: Calculate the camera's intrinsic constant.
    cam_const = calculate_camera_constant(PHONE_SENSOR_WIDTH_MM, PHONE_FOCAL_LENGTH_MM)
    print(f"1. Camera Constant (C) calculated as: {cam_const:.4f}")
    
    # Step 2: Calculate the scale factor for this specific photo.
    scale_factor = calculate_scale_factor(cam_const, distance_m, photo_width_px)
    print(f"2. Scale Factor for this photo is: {scale_factor:.6f} meters/pixel")
    
    # Step 3: Convert pixel measurements to real-world dimensions.
    real_height = measure_dimension_from_pixels(scale_factor, tree_height_in_pixels)
    real_canopy = measure_dimension_from_pixels(scale_factor, canopy_width_in_pixels)
    real_dbh_m = measure_dimension_from_pixels(scale_factor, dbh_in_pixels)
    
    print("\n--- Final Calculated Metrics ---")
    print(f"Tree Height: {real_height:.2f} meters")
    print(f"Canopy Diameter: {real_canopy:.2f} meters")
    print(f"Diameter at Breast Height (DBH): {real_dbh_m * 100:.2f} cm")