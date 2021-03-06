############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,\
        name):

        """Initialize a melon."""

        self.code = code
        self.color = color
        self.first_harvest = first_harvest
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True,True,"Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", False,False,"Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        # print(f"{melon.name} pairs with:")
        print("{} pairs with: ".format(melon.name))

        for pairing in melon.pairings:
            print("- {}".format(pairing))
        print ("")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict

print_pairing_info(make_melon_types())
print (make_melon_type_lookup(make_melon_types()))


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_field, harvester):

        """Initialize a melon."""

        self.type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvester = harvester


    def is_sellable(self):
        if self.color_rating > 5 and self.harvested_field != 3 and self.shape_rating > 5:
            return True
        else:
            return False


def make_melons():
    """Returns a list of Melon objects."""

    all_melons = []

    melon_1 = Melon("yw", 9, 7, 2, "Sheila")
    all_melons.append(melon_1)

    melon_2 = Melon("yw", 3, 4, 2, "Sheila")
    all_melons.append(melon_2)

    melon_3 = Melon("yw", 9, 8, 3, "Sheila")
    all_melons.append(melon_3)

    melon_4 = Melon("cas", 10, 6, 35, "Sheila")
    all_melons.append(melon_4)

    melon_5 = Melon("cren", 8, 9, 35, "Michael")
    all_melons.append(melon_5)

    melon_6 = Melon("cren", 8, 2, 35, "Michael")
    all_melons.append(melon_6)

    melon_7 = Melon("cren", 2, 3, 4, "Michael")
    all_melons.append(melon_7)

    melon_8 = Melon("musk", 6, 7, 4, "Michael")
    all_melons.append(melon_8)

    melon_9 = Melon("yw", 7, 10, 3, "Sheila")
    all_melons.append(melon_9)

    return all_melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable == True:
            print ("Harvested by {} from Field {} (CAN BE SOLD)".format(melon.harvester,melon.harvested_field))
        else:
            print ("Harvested by {} from Field {} (NOT SELLABLE)".format(melon.harvester,melon.harvested_field))


lst = make_melons()
get_sellability_report(lst)

