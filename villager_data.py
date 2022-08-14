"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species_list = set()

    opened_file = open(filename)

    for line in opened_file:
        name, species, _, _, _ = line.rstrip().split('|')
        species_list.add(species)

    return species_list

# print(all_species("villagers.csv"))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """   

    specific_species = []

    opened_file = open(filename)

    for line in opened_file:
        name, species = line.rstrip().split("|")[:2]
        if search_string == "All":
            specific_species.append(name)
        elif search_string == species:
            specific_species.append(name)

    return sorted(specific_species)

# print(get_villagers_by_species("villagers.csv"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    opened_file = open(filename)

    for line in opened_file:
        name, _, _, hobby, _ = line.rstrip().split("|")
        if hobby == 'Fitness':
            fitness.append(name)
        elif hobby == 'Nature':
            nature.append(name)
        elif hobby == 'Education':
            education.append(name)
        elif hobby == 'Music':
            music.append(name)
        elif hobby == 'Fashion':
            fashion.append(name)
        elif hobby == 'Play':
            play.append(name)
        
    return [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]

# print(all_names_by_hobby("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    opened_file = open(filename)

    for line in opened_file:
        given_animal_info = line.rstrip().split("|")
        given_animal_info = tuple(given_animal_info)
        all_data.append(given_animal_info)

    return all_data

# print(all_data("villagers.csv"))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    opened_file = open(filename)

    for line in opened_file:
        name, _, _, _, motto = line.rstrip().split("|")
        if name == villager_name:
            return motto
        
# print(find_motto("villagers.csv"))

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # gives an empty set depending on the position of the villager chosen

    same_personality = set()

    opened_file = open(filename)

    for line in opened_file:
        name, _, personality = line.rstrip().split('|')[:3]
        if villager_name == name:
            chosen_personality = personality
            break 
    
    if chosen_personality:
        for line in opened_file:
            name, _, personality = line.rstrip().split('|')[:3]
            if personality == chosen_personality:
                same_personality.add(name)

    return same_personality

print(find_likeminded_villagers('villagers.csv', 'Kyle'))
