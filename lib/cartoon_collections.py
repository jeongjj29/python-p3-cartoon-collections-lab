def roll_call_dwarves(list):
    [print(f"{i+1}. {dwarf}") for i, dwarf in enumerate(list)]
    pass

def summon_captain_planet(planeteer_calls):
    return [f"{call.title()}!" for call in planeteer_calls]
    pass

def long_planeteer_calls(list):
    return any([len(call) > 4 for call in list])
    # for item in list:
    #     if len(item) > 4:
    #         return True
    # return False    
    pass

def find_the_cheese(list):
    return next((call for call in list if call in ["cheddar", "gouda", "camembert"]), None)
    # for item in list:
    #     if item in ["cheddar", "gouda", "camembert"]:
    #         return item
    pass
