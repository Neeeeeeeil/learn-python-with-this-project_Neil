# List of material costs per square meter for flooring
floor_cost = {
    "Marble": 100,
    "Timber": 20,
    "Porcelain": 50
}

# List of material costs per square meter for walls
wall_cost = {
    "Paint": 10,
    "Wood Panels": 30,
    "Wallpaper": 45
}

# Material names for easier reference
A = "Marble"
B = "Timber"
C = "Porcelain"
wall_A = "Paint"
wall_B = "Wood Panels"
wall_C = "Wallpaper"

# This will calculate the cost for both floor and walls
def estimate_floor_cost(Material, Area):
    AreaCost = floor_cost[Material] * Area
    return AreaCost

def estimate_wall_cost(Material, Area):
    AreaCost = wall_cost[Material] * Area
    return AreaCost

# Main loop where everything happens
while True:
    try:
        # Input room dimensions to get the area for the floor
        length = input("What is the length of the room? ")
        width = input("What is the width of the room? ")
        height = input("What is the height of the room? ")

        # Calculate area for the floor
        floor_area = int(length) * int(width)

        # Calculate perimeter for the walls (sum of all four sides)
        perimeter = 2 * (int(length) + int(width))

        # Calculate area for the walls (height * perimeter)
        wall_area = int(height) * perimeter

    except ValueError:
        # Handle invalid input for dimensions
        print("Invalid input, please use integers for dimensions.")
        continue  # Restart the loop if there's an error in the input

    # Material selection for the floor
    floor_material = input("What material would you like to use for your flooring? \nA: Marble \nB: Timber \nC: Porcelain\nAnswer A/B/C: ").strip().upper()

    if floor_material == "A":
        floor_material = A
    elif floor_material == "B":
        floor_material = B
    elif floor_material == "C":
        floor_material = C
    else:
        print("Invalid input, please select 'A', 'B' or 'C' for the floor material.")
        continue  # Restart if the input is invalid for the floor material

    # Material selection for the walls
    wall_material = input("What material would you like to use for your walls? \nA: Paint \nB: Wood Panels \nC: Wallpaper\nAnswer A/B/C: ").strip().upper()

    if wall_material == "A":
        wall_material = wall_A
    elif wall_material == "B":
        wall_material = wall_B
    elif wall_material == "C":
        wall_material = wall_C
    else:
        print("Invalid input, please select 'A', 'B' or 'C' for the wall material.")
        continue  # Restart if the input is invalid for the wall material

    # Calculate the costs for both the floor and walls
    floor_cost_total = estimate_floor_cost(floor_material, floor_area)
    wall_cost_total = estimate_wall_cost(wall_material, wall_area)

    # Calculate the total cost of the project
    total_project_cost = floor_cost_total + wall_cost_total

    # Output the results
    print(f"\nFloor area: {floor_area} square meters, Material: {floor_material}, Cost: {floor_cost_total} euros")
    print(f"Wall area: {wall_area} square meters, Material: {wall_material}, Cost: {wall_cost_total} euros")
    print(f"Total cost of the project: {total_project_cost} euros")

    # Ask if the user wants to save the estimation
    answer = input("Would you like to save this estimation? y/n: ").strip().lower()

    if answer == "y":
        # Save the output to a file
        with open("estimations.txt", 'a') as f:
            f.write(f"Floor: {floor_area} m², Material: {floor_material}, Cost: {floor_cost_total} euros\n")
            f.write(f"Walls: {wall_area} m², Material: {wall_material}, Cost: {wall_cost_total} euros\n")
            f.write(f"Total Project Cost: {total_project_cost} euros\n\n")
        print("Estimation saved successfully.")

    # Ask if the user wants to do another estimation or exit
    continue_estimation = input("Would you like to make another estimation? y/n: ").strip().lower()

    if continue_estimation == 'n':
        print("Exiting the program. Goodbye!")
        break  # Exit the loop if the user doesn't want to continue
    elif continue_estimation != 'y':
        # If they type something other than "y" or "n", ask again
        print("Invalid input, please enter 'y' or 'n'.")
        continue
