# routing_logic.py
# Core logic for the Eco-Routing Engine from the "Citizen Centered Climate Intelligence" paper.
# This script demonstrates the calculation of the Dynamic Holistic Cost (DHC) for a route.

def calculate_emission_factor_g_per_km(speed_kmh: float) -> float:
    """
    Calculates a heuristic vehicle emission factor based on average speed.
    This U-shaped curve models high emissions at low (congestion) and high (drag) speeds.
    """
    if speed_kmh < 1:
        speed_kmh = 1  # Avoid division by zero
    
    # Coefficients from the paper's heuristic model
    k1, k2, k3 = 80, 6500, 0.03
    
    congestion_term = k2 / speed_kmh
    drag_term = k3 * (speed_kmh ** 2)
    
    return k1 + congestion_term + drag_term

def analyze_route_holistic_cost(route_segments_data: pd.DataFrame, route_length_km: float, route_time_min: float) -> dict:
    """
    Analyzes a given route to calculate its Dynamic Holistic Cost (DHC).

    Args:
        route_segments_data: A DataFrame of road segments that make up the route. 
                             Must contain a 'static_eqs' column.
        route_length_km: The total length of the route in kilometers.
        route_time_min: The total travel time for the route in minutes.

    Returns:
        A dictionary containing the calculated costs and scores.
    """
    
    # 1. Define the weights for the DHC formula
    W_DIST = 0.3  # Weight for distance cost
    W_EMIS = 0.5  # Weight for emissions cost
    W_ECO = 0.2   # Weight for environmental reward
    
    # 2. Calculate dynamic components
    avg_speed_kmh = (route_length_km / (route_time_min / 60.0)) if route_time_min > 0 else 0
    emissions_g_per_km = calculate_emission_factor_g_per_km(avg_speed_kmh)
    total_emissions_kg = (emissions_g_per_km * route_length_km) / 1000.0
    
    # 3. Calculate cost components
    distance_cost = W_DIST * route_length_km
    emissions_cost = W_EMIS * total_emissions_kg
    
    # 4. Calculate environmental reward
    # In a real implementation, this sum would be weighted by the length of each segment on the route.
    # For this demonstration, we use the mean score of the segments.
    avg_eco_score = route_segments_data['static_eqs'].mean()
    environmental_reward = W_ECO * avg_eco_score * route_length_km # Scale reward by distance
    
    # 5. Calculate the final Dynamic Holistic Cost (DHC)
    # Lower is better.
    holistic_cost = distance_cost + emissions_cost - environmental_reward
    
    return {
        "holistic_cost": holistic_cost,
        "avg_eco_score": avg_eco_score,
        "total_emissions_kg": total_emissions_kg,
        "components": {
            "distance_cost": distance_cost,
            "emissions_cost": emissions_cost,
            "environmental_reward": environmental_reward,
        }
    }

# --- Example Usage ---
if __name__ == '__main__':
    print("\n--- Demonstrating Dynamic Holistic Cost Calculation ---")

    # Create dummy data for two different routes
    route_1_segments = pd.DataFrame({'static_eqs': [0.8, 0.9, 0.85]}) # A very green route
    route_2_segments = pd.DataFrame({'static_eqs': [0.3, 0.4, 0.35]}) # A less green route

    # Scenario 1: The greener route is slightly longer
    print("\nScenario 1: Green route vs. Shorter, less-green route")
    analysis_1 = analyze_route_holistic_cost(route_1_segments, route_length_km=5.5, route_time_min=12)
    analysis_2 = analyze_route_holistic_cost(route_2_segments, route_length_km=5.0, route_time_min=10)
    
    print(f"  Route 1 (Green): Holistic Cost = {analysis_1['holistic_cost']:.3f} (Eco Score: {analysis_1['avg_eco_score']:.3f})")
    print(f"  Route 2 (Short): Holistic Cost = {analysis_2['holistic_cost']:.3f} (Eco Score: {analysis_2['avg_eco_score']:.3f})")
    
    recommended_route = 1 if analysis_1['holistic_cost'] < analysis_2['holistic_cost'] else 2
    print(f"  > Recommendation: Route {recommended_route} is the optimal choice.")