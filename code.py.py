def main():
    config = read_config()

    use_current_prices = config.get("use_current_prices", False)

    if use_current_prices:
        current_prices = config.get("prices", {})

        # Assign current prices to material variables
        lumber_price_per_sqft = current_prices.get("lumber", 0.0)
        tile_price_per_sqft = current_prices.get("tile", 0.0)
        steel_price_per_sqft = current_prices.get("steel", 0.0)
        stone_price_per_sqft = current_prices.get("stone", 0.0)
    else:
        # Ask the user to input custom parameters
        lumber_price_per_sqft = float(input("Enter the average price of lumber per square foot for the homeowner: $"))
        tile_price_per_sqft = float(input("Enter the average price of tile per square foot for the homeowner: $"))
        steel_price_per_sqft = float(input("Enter the average price of steel per square foot for the homeowner: $"))
        stone_price_per_sqft = float(input("Enter the average price of stone per square foot for the homeowner: $"))

    # Rest of the code remains the same...
    # Calculate individual costs
    lumber_cost = calculate_cost("Lumber", lumber_price_per_sqft, lumber_square_feet)
    tile_cost = calculate_cost("Tile", tile_price_per_sqft, tile_square_feet)
    steel_cost = calculate_cost("Steel", steel_price_per_sqft, steel_square_feet)
    stone_cost = calculate_cost("Stone", stone_price_per_sqft, stone_square_feet)

    # Calculate total cost
    total_cost = lumber_cost + tile_cost + steel_cost + stone_cost

    # Display results
    print("\nCost breakdown:")
    print(f"Lumber: ${lumber_cost:.2f}")
    print(f"Tile: ${tile_cost:.2f}")
    print(f"Steel: ${steel_cost:.2f}")
    print(f"Stone: ${stone_cost:.2f}")

    print("\nTotal project cost: ${:.2f}".format(total_cost))
