def calculate_cost(material, price_per_sqft, square_feet):
    total_cost = price_per_sqft * square_feet
    return total_cost

def main():
    print("Welcome to the Home Project Cost Calculator!")
    print("Please provide the following information.")

    # Lumber
    lumber_price_per_sqft = float(input("Enter the average price of lumber per square foot for the homeowner: $"))
    lumber_square_feet = float(input("How many square feet of lumber do you need? "))

    # Tile
    tile_price_per_sqft = float(input("Enter the average price of tile per square foot for the homeowner: $"))
    tile_square_feet = float(input("How many square feet of tile do you need? "))

    # Steel
    steel_price_per_sqft = float(input("Enter the average price of steel per square foot for the homeowner: $"))
    steel_square_feet = float(input("How many square feet of steel do you need? "))

    # Stone
    stone_price_per_sqft = float(input("Enter the average price of stone per square foot for the homeowner: $"))
    stone_square_feet = float(input("How many square feet of stone do you need? "))

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

if __name__ == "__main__":
    main()
