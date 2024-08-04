import ujson as ujs


class StrategiesAndUnits:

    def __init__(self):
        self.resource_names = ['supplies', 'components', 'fuel', 'electronics', 'rares', 'manpower', 'money']
        # Units
        with open("units.json", "r") as f:
            self.units = ujs.load(f)

        # Buildings
        with open("buildings.json", "r") as f:
            self.buildings = ujs.load(f)

        # Naval Stacks
        self.frigates_r_us = {
            'units': [
                self.units['elite_frigate'],
                self.units['frigate']
            ],
            'amounts': [1, 4],
            'levels': [3, 7]
        }
        self.cruising_my_way_down_town = {
            'units': [
                self.units['cruiser'],
                self.units['naval_officer']
            ],
            'amounts': [4, 1],
            'levels': [5, 5]
        }
        self.early_game_navy = {
            'units': [
                self.units['frigate']
            ],
            'amounts': [2],
            'levels': [3]
        }

        # Ground Stacks
        self.samadar = {
            'units': [
                self.units["mobile_sam_launcher"],
                self.units["mobile_radar"],
                self.units["national_guard"]
            ],
            'amounts': [4, 1, 1],
            'levels': [4, 3, 3]
        }
        self.rockets_go_nyooooom = {
            'units': [
                self.units["multiple_rocket_launcher"],
                self.units["national_guard"]
            ],
            'amounts': [5, 2],
            'levels': [5, 3]
        }
        self.bullet_sponges = {
            'units': [
                self.units["national_guard"],
                self.units["main_battle_tank"]
            ],
            'amounts': [2, 2],
            'levels': [3, 1]
        }
        self.rails = {
            'units': [
                self.units["elite_railgun"]
            ],
            'amounts': [5],
            'levels': [3]
        }
        self.rebellion_suppressors = {
            'units': [
                self.units["mercenary"]
            ],
            'amounts': [1],
            'levels': [1]
        }
        self.missile_defense = {
            'units': [
                self.units["theater_defense_system"]
            ],
            'amounts': [3],
            'levels': [7]
        }
        self.ng = {
            'units': [
                self.units["national_guard"]
            ],
            'amounts': [1],
            'levels': [3]
        }
        self.radar = {
            'units': [
                self.units["mobile_radar"]
            ],
            'amounts': [1],
            'levels': [3]
        }
        self.towed_artillery = {
            "towed_artillery": 5,
            'levels': 7
        }
        self.maa = {
            "mobile_anti_air_vehicle": 5,
            'levels': 7
        }
        self.early_game_ground_force = {
            'units': [
                self.units["combat_recon_vehicle"],
                self.units["national_guard"]
            ],
            'amounts': [7, 3],
            'levels': [3, 3]
        }

        # Air Stacks
        self.officer_heli = {
            'units': [
                self.units["elite_attack_helicopter"],
                self.units["rotary_wing_officer"]
            ],
            'amounts': [4, 1],
            'levels': [3, 6]
        }
        self.elite_helis = {
            'units': [
                self.units["elite_attack_helicopter"]
            ],
            'amounts': [5],
            'levels': [3]
        }
        self.mid_game_elite_helis = {
            'units': [
                self.units["elite_attack_helicopter"]
            ],
            'amounts': [3],
            'levels': [1]
        }
        self.early_game_helis = {
            'units': [
                self.units["helicopter_gunship"]
            ],
            'amounts': [3],
            'levels': [1]
        }
        self.mid_game_helis = {
            'units': [
                self.units["helicopter_gunship"],
                self.units["attack_helicopter"]
            ],
            'amounts': [2, 3],
            'levels': [1, 3]
        }
        self.early_game_asf = {
            'units': [
                self.units["air_superiority_fighter"]
            ],
            'amounts': [3],
            'levels': [3]
        }
        self.mid_game_asf = {
            'units': [
                self.units["air_superiority_fighter"]
            ],
            'amounts': [4],
            'levels': [4]
        }
        self.late_game_asf = {
            'units': [
                self.units["air_superiority_fighter"]
            ],
            'amounts': [5],
            'levels': [7]
        }

    def _cities(self, stack_ratios: dict, number_of_land_cities: int, number_of_ocean_cities: int) -> dict:
        cities = []
        for i in range(number_of_land_cities):
            cities.append({
                'type': 'land',
                "arms_industry": 4,
                "recruiting_office": 3,
                "secret_weapons_lab": 0,
                "army_base": 0,
                "air_base": 0
            })
        for i in range(number_of_ocean_cities):
            cities.append({
                'type': 'ocean',
                "arms_industry": 4,
                "recruiting_office": 3,
                "secret_weapons_lab": 0,
                "army_base": 0,
                "air_base": 0,
                "naval_base": 1,
            })

        all_units_amounts = {}

        for i in range(len(stack_ratios['stacks'])):
            stack = stack_ratios['stacks'][i]
            num_of_stack = stack_ratios['amounts'][i]
            for x in range(len(stack['units'])):
                # go through each unit in the stack, take its amount, add it to the
                unit = stack['units'][x]
                name = unit['name']
                num_of_unit = stack['amounts'][x]
                all_units_amounts[name] = num_of_unit * num_of_stack

        lowest_unit_amount = 999999999
        num_of_units = 0
        unit_names = list(all_units_amounts.keys())
        for i in range(len(unit_names)):
            num_of_units += all_units_amounts[unit_names[i]]
            if 0 < all_units_amounts[unit_names[i]] < lowest_unit_amount:
                lowest_unit_amount = all_units_amounts[unit_names[i]]

        unit_ratios = all_units_amounts
        for i in range(len(unit_names)):
            unit_ratios[unit_names[i]] /= num_of_units

        base_ratios = {
            "air_base": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "army_base": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "naval_base": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "arms_industry": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "recruiting_office": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "secret_weapons_lab": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0}
        }
        for i in range(len(unit_names)):
            bases = list(base_ratios.keys())
            for x in range(len(bases)):
                base = self.units[unit_names[i]][list(self.units[unit_names[i]].keys())[-1]]['building_req'][bases[x]]
                if base < 3 and bases[x] in ['arms_industry', 'recruiting_office']:
                    base = 3
                if base > 0:
                    base_ratios[bases[x]]['total'] += unit_ratios[unit_names[i]]
                    base_ratios[bases[x]][f'lvl{base}'] += unit_ratios[unit_names[i]]

        base_cities = {
            "air_base": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "army_base": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "naval_base": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "arms_industry": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "recruiting_office": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0},
            "secret_weapons_lab": {"lvl1": 0, "lvl2": 0, "lvl3": 0, "lvl4": 0, "lvl5": 0, "total": 0}
        }
        bases = list(base_ratios.keys())
        print(f'\n-- Cities for Bases --')
        for i in range(len(bases)):
            base_cities[bases[i]]["total"] = round(
                (base_ratios[bases[i]]['total'] * (number_of_land_cities + number_of_ocean_cities)) + 0.5
            )
            base_levels = list(base_cities[bases[i]].keys())
            for x in range(len(base_levels)):
                if base_levels[x] != 'total':
                    base_cities[bases[i]][base_levels[x]] = round(
                        ((base_ratios[bases[i]][base_levels[x]] * base_cities[bases[i]]["total"]) * base_cities[bases[i]]["total"]) + 0.5
                    )
            placed_bases = 0
            for x in range(len(base_levels)):
                if base_levels[-x] != 'total':
                    for y in range(base_cities[bases[i]][base_levels[-x]]):
                        if placed_bases == base_cities[bases[i]]['total']:
                            base_cities[bases[i]][base_levels[-x]] -= 1
                        elif placed_bases < base_cities[bases[i]]['total']:
                            placed_bases += 1

                    if base_cities[bases[i]][base_levels[-x]] < 0:
                        base_cities[bases[i]][base_levels[-x]] = 0

            if bases[i] not in ['arms_industry', 'recruiting_office'] and base_cities[bases[i]]["total"] > 0:
                printed_statement = f'{base_cities[bases[i]]["total"]} | {bases[i]} - '
                for x in range(len(base_levels)):
                    if base_cities[bases[i]][base_levels[x]] > 0 and base_levels[x] != 'total':
                        if base_cities[bases[i]][base_levels[x]] > 1:
                            printed_statement += f'{base_cities[bases[i]][base_levels[x]]} {base_levels[x].upper()}s | '
                        else:
                            printed_statement += f'{base_cities[bases[i]][base_levels[x]]} {base_levels[x].upper()} | '
                print(printed_statement)

        return base_cities

    def _resource_ratios(self, stack_ratios: dict, label: str, buildings_to_be_made: dict, resource_multiplier):
        unit_costs = {
            'supplies': 0,
            'components': 0,
            'fuel': 0,
            'electronics': 0,
            'rares': 0,
            'manpower': 0,
            'money': 0
        }

        for i in range(len(stack_ratios['stacks'])):
            stack = stack_ratios['stacks'][i]
            num_of_stack = stack_ratios['amounts'][i]
            for x in range(len(stack['units'])):
                # go through each unit in the stack, take its cost of production,
                # multiply it by how many are in that stack,
                # multiply it by the ratio, and add it to the early_game_cost_of_upkeep
                unit = stack['units'][x]
                num_of_unit = stack['amounts'][x]
                level_of_unit = stack['levels'][x]
                upkeep = unit[f'lvl{level_of_unit}']['upkeep']
                production = unit[f'lvl{level_of_unit}']['cost']
                for y in range(len(self.resource_names)):
                    unit_costs[self.resource_names[y]] += (upkeep[self.resource_names[y]] * num_of_unit * num_of_stack)
                    unit_costs[self.resource_names[y]] += (production[self.resource_names[y]] * num_of_unit * num_of_stack)

        building_costs = {
            'supplies': 4250,
            'components': 3750,
            'fuel': 2500,
            'electronics': 1750,
            'rares': 1500,
            'manpower': 12500,
            'money': 10000
        }
        buildings = list(buildings_to_be_made.keys())
        for i in range(len(buildings_to_be_made)):
            building_levels = list(buildings_to_be_made[buildings[i]].keys())
            for x in range(len(building_levels)):
                if building_levels[x] != 'total':
                    costs = self.buildings[buildings[i]][building_levels[x]]['costs']
                    for y in range(len(self.resource_names)):
                        if self.resource_names[y] != 'manpower':
                            building_costs[self.resource_names[y]] += \
                                costs[self.resource_names[y]] * buildings_to_be_made[buildings[i]][building_levels[x]]

        lowest_resource_amount = 999999999
        for i in range(len(self.resource_names)):
            unit_costs[self.resource_names[i]] += building_costs[self.resource_names[i]] / 2
            if self.resource_names[i] == 'supplies':
                unit_costs['rares'] += unit_costs['supplies'] * 0.7
                unit_costs['supplies'] += unit_costs['supplies'] * 0.5
            if 0 < unit_costs[self.resource_names[i]] < lowest_resource_amount:
                lowest_resource_amount = unit_costs[self.resource_names[i]]

        print(f'\n-- {label} Resource Ratios --')
        for i in range(len(self.resource_names)):
            print(f'{round((unit_costs[self.resource_names[i]] / lowest_resource_amount) * resource_multiplier, 2)} | '
                  f'{self.resource_names[i]}')

    def death_march(self, number_of_cities, number_of_land_cities, number_of_ocean_cities, resource_multiplier):
        early_game_stack_ratios = {
            'stacks': [
                self.early_game_ground_force,
                self.early_game_asf,
                self.early_game_navy,
                self.ng
            ],
            'amounts': [3, 3, 1, 3]
        }
        mid_game_stack_ratios = {
            'stacks': [
                self.mid_game_asf,
                self.frigates_r_us,
                self.ng,
                self.rebellion_suppressors,
                self.rails,
            ],
            'amounts': [4, 4, 8, 8, 2]
        }
        end_game_stack_ratios = {
            'stacks': [
                self.rockets_go_nyooooom,
                self.bullet_sponges,
                self.samadar,
                self.rebellion_suppressors,
                self.ng,
                self.frigates_r_us,
                self.missile_defense,
                self.rails,
                self.late_game_asf,
            ],
            'amounts': [2, 3, 2, 8, 4, 4, number_of_cities / 2, 1, 2]
        }

        early_game_buildings = self._cities(early_game_stack_ratios, number_of_land_cities, number_of_ocean_cities)
        self._resource_ratios(early_game_stack_ratios, 'Early Game', early_game_buildings, resource_multiplier)

        mid_game_buildings = self._cities(mid_game_stack_ratios, number_of_land_cities, number_of_ocean_cities)
        self._resource_ratios(mid_game_stack_ratios, 'Mid Game', mid_game_buildings, resource_multiplier)

        end_game_buildings = self._cities(end_game_stack_ratios, number_of_land_cities, number_of_ocean_cities)
        self._resource_ratios(end_game_stack_ratios, 'End Game', end_game_buildings, resource_multiplier)



w = StrategiesAndUnits()
w.death_march(number_of_cities=6, number_of_land_cities=3, number_of_ocean_cities=3, resource_multiplier=)
