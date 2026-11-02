# This function gives advice depending on the season entered
def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


# This function gives advice depending on the plant type entered
def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# Ask the user what they want gardening advice for
season = input("Enter the season (summer or winter): ").lower()
plant_type = input("Enter the plant type (flower or vegetable): ").lower()

# Get the advice from both functions
season_advice = get_season_advice(season)
plant_advice = get_plant_advice(plant_type)

# Display the gardening advice
print(season_advice)
print(plant_advice)