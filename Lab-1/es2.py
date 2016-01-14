import functools

alkaline_earth_materials = [("barium", 56), ("beryllium", 4), ("calcium", 20), ("magnesium", 12), ("radium", 88), ("strontium", 38)]

def highest_atomic_number(materials):
    return functools.reduce(lambda x,y: x if x[1] > y[1] else y, materials)
if __name__ == '__main__':
    print (highest_atomic_number(alkaline_earth_materials))
    alkaline_earth_materials.sort(key=lambda x : x[1])
    print (alkaline_earth_materials)
    alkaline_dict = {x : y for (x,y) in alkaline_earth_materials}
    print (alkaline_dict)
    noble_gases = {"helium" : 2, "neon" : 10 , "argon" : 18, "krypton" : 36, "xenon" : 54, "radon" : 86}
    mixed = noble_gases.copy()
    mixed.update(alkaline_dict)
    print("\n".join(["{0} : {1}".format(x, mixed[x]) for x in sorted(mixed.keys())]))
