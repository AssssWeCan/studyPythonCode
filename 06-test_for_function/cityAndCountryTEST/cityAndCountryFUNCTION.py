def city_and_country(city_name,country_name,population_number = 0):
    """创建对应格式的"城市，国家",并返回"""
    if population_number:
        full_name = city_name.title() + ' , ' + country_name.title() + '  --  population ' + str(population_number)
    else:
        full_name = city_name.title() + ' , ' + country_name.title()
    return full_name