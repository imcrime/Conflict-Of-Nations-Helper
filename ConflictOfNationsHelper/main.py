import strategies

strat = strategies.StrategiesAndUnits()

num_of_cities = 5  # Number of cities you have that can produce units
num_of_ocean_cities = 3  # Number of those cities that can be used for making naval
num_of_land_cities = 2  # Number of cities that cant be used for making naval
resource_multiplier = 1  # Used to increase all the ratios of resources, to match current production amounts

strat.death_march(
    number_of_cities=num_of_cities,
    number_of_land_cities=num_of_land_cities,
    number_of_ocean_cities=num_of_ocean_cities,
    resource_multiplier=resource_multiplier
)
