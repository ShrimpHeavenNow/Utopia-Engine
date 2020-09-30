import random

# In general, UX is horrible. I'll go back and gussie her up once its functioning.
# text color
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'
print()
print(blue(
    "##     ## ########  #######  ########  ####    ###       ######## ##    ##  ######   #### ##    ## ######## "))
print(blue(
    "##     ##    ##    ##     ## ##     ##  ##    ## ##      ##       ###   ## ##    ##   ##  ###   ## ##       "))
print(
    blue("##     ##    ##    ##     ## ##     ##  ##   ##   ##     ##       ####  ## ##         ##  ####  ## ##      "))
print(blue(
    "##     ##    ##    ##     ## ########   ##  ##     ##    ######   ## ## ## ##   ####  ##  ## ## ## ######   "))
print(blue(
    "##     ##    ##    ##     ## ##         ##  #########    ##       ##  #### ##    ##   ##  ##  #### ##       "))
print(blue("##     ##    ##    ##     ## ##         ##  ##     ##    ##       ##   ### ##    ##   ##  ##   ### ##"))
print(blue(
    " #######     ##     #######  ##        #### ##     ##    ######## ##    ##  ######   #### ##    ## ######## "))
print()
print("This is a digital version of the incredible print and play board game of the same name")
print("By Nick Hayes.")
print("Programed into python By Dean Wright IV")
print("Be sure to check out the real thing. Look for it on BoardGameGeek.com")
input("Press Enter to continue.")
print()

# I feel like defining here is fine until I want to have the ability to start a new game.
day = 0
health = 30  # Make this a function as well?
# sets inventory to be empty
toolbelt = ["Paralysis Wand", "Dowsing Rod", "Focus Charm"]
stores = {"Silver": 0, "Quartz": 0, "Silica": 0, "Gum": 0, "Wax": 0, "Lead": 0}  # make limit of 4
eventDays = [2, 5, 8, 11, 14, 17, 20]
skullDays = [15, 16, 17, 18, 19, 20, 21, 22]
wastebasket = []
godsHand = 0


# monster class
class Monster:
    """Create fightable monsters and their stats"""
    def __init__(self, name, rank, spirit, attack, defense):
        self.name = name
        self.rank = rank
        self.spirit = spirit  # I guess this could have been a bool
        self.attack = attack
        self.defense = defense


# monsters
iceBear = Monster("Ice Bear", 1, 0, [1], [5, 6])
rovingBandits = Monster("Roving Bandits", 2, 0, [1], [6])
bloodWolves = Monster("Blood Wolves", 3, 0, [1, 2], [6])
horseEaterHawk = Monster("Horse Eater Hawk", 4, 0, [1, 2, 3], [6])
theHollowGiant = Monster("The Hollow Giant", 5, 1, [1, 2, 3, 4], [6])
rogueThief = Monster("Rogue Thief", 1, 0, [1], [5, 6])
blanketOfCrows = Monster("Blanket of Crows", 2, 0, [1], [6])
hornbackBison = Monster("Hornback Bison", 3, 0, [1, 2], [6])
grassybackTroll = Monster("Grassyback Troll", 4, 0, [1, 2, 3], [6])
thunderKing = Monster("Thunder King", 5, 0, [1, 2, 3, 4], [6])
gemscaleBoa = Monster("Genscale Boa", 1, 0, [1], [5, 6])
ancientAlligator = Monster("Ancient Alligator", 2, 0, [1], [6])
landShark = Monster("Land Shark", 3, 0, [1, 2], [6])
abyssalLeech = Monster("Abyssal Leech", 4, 1, [1, 2, 3], [6])
dwellerInTheTides = Monster("Dweller in the Tides", 5, 0, [1, 2, 3, 4], [6])
fiestyGoblins = Monster("Fiesty Goblins", 1, 0, [1], [5, 6])
glasswingDrake = Monster("Glasswing Drake", 2, 0, [1], [6])
reachingClaws = Monster("Reaching Claws", 3, 1, [1, 2], [6])
terribleWurm = Monster("Terrible Wurm", 4, 0, [1], [6])
infinityWurm = Monster("Infinity Wurm", 5, 1, [1, 2, 3, 4], [6])
graveRobbers = Monster("Grave Robbers", 1, 0, [1], [5, 6])
ghostLights = Monster("Ghost Lights", 2, 1, [1], [6])
vengefulShade = Monster("Vengeful Shade", 3, 0, [1, 2], [6])
nightmareCrab = Monster("Nightmare Crab", 4, 0, [1, 2, 3], [6])
theUnnamed = Monster("Unnamed", 5, 0, [1, 2, 3, 4], [6])
minorImp = Monster("Minor Imp", 1, 0, [1], [5, 6])
renegadeWarlock = Monster("Renegade Warlock", 2, 0, [1], [6])
giantFlamingLizard = Monster("Giant Flaming Lizard", 3, 0, [1, 2], [6])
sparkElemental = Monster("Spark Elemental", 4, 1, [1, 2, 3], [6])
volcanoSpirit = Monster("Volcano Spirit", 5, 1, [1, 2, 3, 4], [6])


class Treasure:
    """Create Treasures,their description and their status"""
    def __init__(self, name, description, used):
        self.name = name
        self.description = description
        self.used = used


icePlate = Treasure("Ice Plate", "This cold half-plate makes you harder to hit by one.", False)
braceletOfIos = Treasure("Bracelet of Ios", "This ivory bracelet lets you start activations with one energy.", False)
shimmeringMoonlace = Treasure("Shimmering Moonlace", "This ethereal cape allows you to ignore encounters.", False)
scaleOfTheInfinityWurm = Treasure("Scale of the Infinity Wurm", "The ebony scale heals you one HP every event day.",
                                  False)
theAncientRecord = Treasure("The Ancient Record", "The dusty tome allows you to change one", False)
theMoltenShard = Treasure("The Molten Shard", "This glowing spike adds 1 to your attack range", False)

treasures = [theMoltenShard, theAncientRecord]


# Artifacts
class Artifact:
    """Create artifacts and all their parameters"""
    def __init__(self, name, activated, component, linked, link_value, description, key_word):
        self.name = name
        self.activated = activated
        self.component = component
        self.linked = linked
        self.link_value = link_value
        self.description = description
        self.key_word = key_word  # This is probably silly. I just need a lower case version on the title.
        # can I do casefold(thing.name) where I need to? probably...


sealOfBalance = Artifact("Seal of Balance", False, "Quartz", False, 0, "A literal baby seal.", ["seal", "balance"])
hermeticMirror = Artifact("Hermetic Mirror", False, "Wax", False, 0, "A mirror", ["hermetic", "mirror"])
voidGate = Artifact("Void Gate", False, "Silica", False, 0, "It hurts to look at", ["void", "gate"])
scryingLens = Artifact("Scrying Lens", False, "Lead", False, 0, "Hey guys, it's scrying its best.", ["scrying", "lens"])
crystalBattery = Artifact("Crystal Battery", False, "Gum", False, 0, "From Tesla (tm)", ["crystal", "battery"])
goldenChassis = Artifact("Golden Chassis", False, "Silver", False, 0, "A Chassis showered in gold.",
                         ["gold", "golden", "chassis"])

artifacts = [sealOfBalance, voidGate]  # sets artifact inventory


# Set locations and their loot. I made it so you could easily add more, for some reason.
class Location:
    """Define locations where treasures, artifacts and components are"""
    def __init__(self, number, name, component, artifact, treasure, days_searched, time_advances, encounters, event,
                 explore_attempt):
        self.number = number
        self.name = name
        self.component = component
        self.artifact = artifact
        self.treasure = treasure
        self.daysSearched = days_searched
        self.timeAdvances = time_advances
        self.encounters = encounters
        self.event = event  # 0 is none, 1 is active, 2 is fleeting, 3 is good, 4 is foul
        self.exploreAttempt = explore_attempt


halbeardPeak = Location(1, "Halbeard Peak", "Silver", sealOfBalance, icePlate, 0, [0, 1, 3],
                        [iceBear, rovingBandits, bloodWolves, horseEaterHawk, theHollowGiant], 0, 0)
theGreatWilds = Location(2, "The Great Wilds", "Quartz", hermeticMirror, braceletOfIos, 0, [0, 3],
                         [rogueThief, blanketOfCrows, hornbackBison, grassybackTroll, thunderKing], 0, 0)
rootStrangledMarshes = Location(3, "Root-Strangled Marshes", "Gum", voidGate, shimmeringMoonlace, 0, [0, 2, 4],
                                [gemscaleBoa, ancientAlligator, landShark, abyssalLeech, dwellerInTheTides], 0, 0)
glassrockCanyon = Location(4, "Glassrock Canyon", "Silica", goldenChassis, scaleOfTheInfinityWurm, 0,
                           [0, 1, 3, ], [fiestyGoblins, glasswingDrake, reachingClaws, terribleWurm, infinityWurm], 0,
                           0)
ruinedCityOfTheAncients = Location(5, "Ruined City of the Ancients", "Wax", scryingLens, theAncientRecord, 0,
                                   [0, 2, 4], [graveRobbers, ghostLights, vengefulShade, nightmareCrab, theUnnamed], 0,
                                   0)
theFieryMaw = Location(6, "The Fiery Maw", "Lead", crystalBattery, theMoltenShard, 0, [0, 1, 2, 4],
                       [minorImp, renegadeWarlock, giantFlamingLizard, sparkElemental, volcanoSpirit], 0, 0)

locations = [halbeardPeak,
             theGreatWilds,
             rootStrangledMarshes,
             glassrockCanyon,
             ruinedCityOfTheAncients,
             theFieryMaw]


def helper(game_place):
    """Give help based on what menu they came from"""
    print("You were in the " + str(game_place) + " menu.")
    print("You are beyond help.")
    # exploring
    # search
    # activate
    # link
    # rolling
    # main


def day_advance():
    """Advance the time track. Check for events and doomsday"""
    global day
    day += 1
    if day in eventDays:  # check against event
        events()
    if day in skullDays:  # check against skulls
        print("You LOSE! Good DAY sir!")
        # End game somehow.
    print(red("There are " + str(skullDays[0] - day) + " days until the end of the world."))


def events():
    """Distribute events to locations at random"""
    print(blue("Events in the world have shifted"))
    for x in locations:
        x.event = 0
    monster = locations[random.randint(0, len(locations) - 1)]
    vision = locations[random.randint(0, len(locations) - 1)]
    fortune = locations[random.randint(0, len(locations) - 1)]
    weather = locations[random.randint(0, len(locations) - 1)]

    monster.event = 1
    print("The monsters in " + monster.name + " are active. Combat will be more deadly.")
    vision.event = 2
    print("Fleeting visions run across " + vision.name + ". Its artifact will be easier to activate.")
    fortune.event = 3
    print("You have a good feeling about " + fortune.name + ". Searching here should be a little easier.")
    weather.event = 4
    print("The weather  in " + weather.name + " is terrible. Days spent searching will take twice as long.")


def encounter(current_location, search_result):
    """Fight the player against a monster"""
    # Maybe this should return success or failure to combat dying in get_hit() nesting nightmares
    monster_alive = True
    fighter = "spam"

    # active monster event
    if current_location.event == 1 and search_result < 0:
        search_result -= 200
    elif current_location == 1 and search_result > 100:
        search_result += 200

    # Determine monster level
    if 100 <= int(search_result) <= 199 or -1 >= int(search_result) >= -100:
        fighter = current_location.encounters[0]
        print("You encounter a " + fighter.name + "!")
    elif 200 <= int(search_result) <= 299 or -101 >= int(search_result) >= -200:
        fighter = current_location.encounters[1]
        print("You encounter a " + fighter.name + "!")
    elif 300 <= int(search_result) <= 399 or -201 >= int(search_result) >= -300:
        fighter = current_location.encounters[2]
        print("You encounter a " + fighter.name + "!")
    elif 400 <= int(search_result) <= 499 or -301 >= int(search_result) >= -400:
        fighter = current_location.encounters[3]
        print("You encounter a " + fighter.name + "!")
    elif 500 <= int(search_result) <= 555 or -401 >= int(search_result) >= -555:
        fighter = current_location.encounters[4]
        print("You encounter a " + fighter.name + "!")

    # Alter the monster based on items
    # if "Ice Plate" in treasures: or whatever
    # have to make sure the this happens just in this function (which I think we do by declaring the fighter variable.)

    if fighter.spirit == 1:
        print("The monster is a spirit!")
        # something about an item here.

    while monster_alive:
        input("Press enter to fight for your life!")
        fight_rolls = [random.randint(1, 6), random.randint(1, 6)]
        print("The Monster rolled a " + str(fight_rolls[0]))
        print("You rolled a " + str(fight_rolls[1]))
        if fight_rolls[0] in fighter.attack:
            hit_result = get_hit(1)
            if hit_result == "dead":
                input(
                    "You're dead")  # Where do I do the scoring funtion? should I keep retuning until I'm in main loop?
            if hit_result == "unconscious":
                input("you're unconscious")  # kick them back to main loop?
        else:
            print("The monster misses")  # make a list with a bunch of fun descriptions and have it choose randomly
        if fight_rolls[1] in fighter.defense:
            print(green("You hit the monster! It is slain!"))
            # make a list with a bunch of fun descriptions and have it choose randomly
            if fighter.rank == 5 and current_location.Treasure not in treasures:
                treasures.append(current_location.Treasure)
                print(
                    "The mighty creature was guarding an amazing treasure, the " + current_location.Treasure.name + ".")
                monster_alive = False
            else:
                print("The " + fighter.name + " drops " + current_location.component)
                stores[current_location.component] += 1
                print("You now have " + str(stores[current_location.component]) + " " + current_location.component)
                monster_alive = False
        else:
            print("You miss!")


def display_table(search_table):
    """Display table of rolls for combat"""
    print("-------")
    print("|" + str(search_table[0]) + "|" + str(search_table[1]) + "|" + str(search_table[2]) + "|")
    print("-------")
    print("|" + str(search_table[3]) + "|" + str(search_table[4]) + "|" + str(search_table[5]) + "|")
    print("-------")


def display_activate_table(search_table):
    """Display table for activation"""
    print("--- --- --- ---")
    print("|" + str(search_table[0]) + "| |" + str(search_table[1]) + "| |" + str(search_table[2]) + "| |" + str(
        search_table[3]) + "|")
    print("--- --- --- ---")
    print("|" + str(search_table[4]) + "| |" + str(search_table[5]) + "| |" + str(search_table[6]) + "| |" + str(
        search_table[7]) + "|")
    print("--- --- --- ---")


def rolls(table, type_):
    """Roll dice and assign them to a table"""
    placed_roll = False
    _rolls_ = [random.randint(1, 6), random.randint(1, 6)]
    print("You've rolled " + str(_rolls_[0]) + " and " + str(_rolls_[1]) + ".")

    # Place First Roll.
    while not placed_roll:
        print("Where would you like your first roll, a " + str(_rolls_[0]) + " to be placed?")
        _roll_Placement_ = input().upper()
        if _roll_Placement_ in table:
            _table_place_ = -1
            for x in table:
                _table_place_ += 1
                if x == _roll_Placement_:
                    print("it was " + str(table[_table_place_]))
                    table[_table_place_] = _rolls_[0]
                    print("Now It's " + str(table[_table_place_]))
                    placed_roll = True
        elif _roll_Placement_ == "help":
            helper("rolling")
        else:
            print("select an unassigned location")
    placed_roll = False

    # Place Second Roll
    if type_ == "search" or type == "link":
        display_table(table)
    if type_ == "activate":
        display_activate_table(table)

    while not placed_roll:
        print("Where would you like your second roll, a " + str(_rolls_[1]) + " to be placed?")
        _roll_Placement_ = input().upper()
        if _roll_Placement_ in table:
            _table_place_ = -1
            for x in table:
                _table_place_ += 1
                if x == _roll_Placement_:
                    print("it was " + str(table[_table_place_]))
                    table[_table_place_] = _rolls_[1]
                    print("Now It's " + str(table[_table_place_]))
                    placed_roll = True
        else:
            print("select an unassigned location")


def get_hit(deadly):
    """Reduce player health. Check for death"""
    # Utilize these returns.
    global health
    global day
    print(red("You've been hurt!"))
    health -= 1

    if deadly >= 2:
        for x in range(0, deadly):
            health -= 1
            if health <= -1:
                print("You have died.")
                return "dead"
            else:
                print("You've taken " + str(deadly) + "damage")
                health -= deadly

    if health == 0:
        print("As you fall unconscious, the dazzling light of your amulet teleports you to safety.")
        for x in range(5):
            day_advance()
        print("Six days pass and you are back to full health.")
        health = 6
        print("While you've been unconscious, all your search progress has been reset.")
        for x in locations:
            x.exploreAttempt = 0
        return "unconscious"
    print("You have " + str(health) + " health remaining")
    return None


def searching():
    """Searching minigame. Return result'"""
    _search_table = ["A", "B", "C", "D", "E", "F"]
    _matching = ["A", "B", "C", "D", "E", "F"]
    _filled_table = False

    while not _filled_table:
        _is_there = []
        display_table(_search_table)  # Display an amazing acii table.
        rolls(_search_table, "search")  # rolls dice, places them.
        # A very shitty way to make sure the whole table is filled in.
        for x in _matching:
            if x in _search_table:
                _is_there.append(x)
            print(_is_there)
        if len(_is_there) == 0:
            _filled_table = True
    display_table(_search_table)
    _top_number = int(str(_search_table[0]) + str(_search_table[1]) + str(_search_table[2]))
    _bottom_number = int(str(_search_table[3]) + str(_search_table[4]) + str(_search_table[5]))
    search_result = _top_number - _bottom_number
    # make this prettier!
    return search_result


def location_desciption(_current_location):
    """Describe location: components, artifact, treasure, time advances, event"""
    print("Here you will find " + _current_location.component + ".")
    if _current_location.artifact in artifacts:
        print("Here you found " + _current_location.artifact.name + ".")
    else:
        print("Hidden somewhere is the " + _current_location.artifact.name + ".")
    if _current_location.treasure in treasures:
        print("Here you found " + _current_location.treasure.name + ".")
    else:
        print("It's said a powerful monster carries " + _current_location.treasure.name + " here.")
    print("Searching here would advance the day following these attempts: " + str(
        _current_location.timeAdvances))  # make this pretty.
    print("You've explored here " + str(_current_location.exploreAttempt) + " times")
    _descriptions = ["There are no events here currently.", "The monsters here are active. Combat will be more deadly.",
                     "Fleeting visions run across these lands. Its artifact will be easier to activate.",
                     "You have a good feeling about this place. Searching here should be a little easier.",
                     "The weather here is terrible. Days spent searching will take twice as long."]
    print(_descriptions[_current_location.event])  # This makes me feel so smart.


# def list_objects(list, param):
# """Iterate through a list of objects for a specific parameter"""
#    showItems = ""
#    for x in list:
#        if x.param == True:  #how do I make the attribute equal the argument?
#            showItems += x.name
#            showItems += ", "
#    return showItems

def check_inventory():
    """Print the player inventory. Check item properties"""
    print("You open your bag and see...")
    # List Components
    for x, y in stores.items():
        print(x, y)
    # List Artifacts
    _show_items = ""
    if len(artifacts) == 0:
        print("You have no artifacts")
    else:
        for x in artifacts:
            _show_items += x.name
            _show_items += ", "
        print("You have the following artifacts: " + _show_items + ".")  # fix formatting of last item
    # list activated artifacts
    _show_items = ""
    for x in artifacts:
        if x.activated:
            _show_items += x.name
            _show_items += ", "
    if _show_items != "":
        print("You have the following activated artifacts: " + _show_items + ".")  # fix formatting of last item
    else:
        print("You have no activated artifacts")
    _show_items = ""
    for x in artifacts:
        if x.activated:
            _show_items += x.name
            _show_items += ", "
    if _show_items != "":
        print("You have the following activated artifacts: " + _show_items + ".")  # fix formatting of last item
    else:
        print("You have no activated artifacts")
    # List Treasures
    _show_items = ""
    if len(treasures) == 0:
        print("You have no treasures.")
    else:
        for x in treasures:
            _show_items += x.name
            _show_items += ", "
        print("You have the following treasures: " + _show_items + ".")  # fix formatting of last item
    # Add Tool belt
    _show_items = ""
    if len(toolbelt) == 0:
        print("You have used all your tools")
    else:
        for x in toolbelt:
            _show_items += x
            _show_items += ", "
        print("You have the following tools availible: " + _show_items + ".")  # fix formatting of last item
    while True:
        print("Actifact info? TreasureTool info? Or press enter to continue.")
        _action = input().casefold()
        if "artifact" in _action:
            looking = True
            while looking:
                print("Which artifact?")
                _show_items = ""
                for x in artifacts:
                    _show_items += x.name
                    _show_items += ", "
                    print("You have the following artifacts: " + _show_items + ".")  # fix formatting of last item
                _action = input().casefold()
                for x in artifacts:
                    if _action in x.key_word:  # This is stupid. I could have just done the number thing again.
                        _tell_me = x
                        print(_tell_me.name + " uses " + _tell_me.component + " to link")
                        print(_tell_me.description)
                        if not _tell_me.linked:
                            print("It is not yet linked.")
                        else:
                            print("It is linked.")
                        if not _tell_me.activated:
                            print("It is not yet activated.")
                            looking = False
                            break
                        else:
                            print("It is activated")
                            looking = False
                            break
                    else:
                        print("Please enter an artifact")
        if "tool" in _action:
            while True:
                _show_items = ""
                print("Which Tool?")
                for x in toolbelt:
                    _show_items += x
                    _show_items += ", "
                print("You have the following tools availible: " + _show_items + ".")  # fix formatting of last item
                _action = input().casefold()
                if "focus" in _action or "charm" in _action:  # Coulda done the number thing. Not as bad though.
                    print("The Focus Charm adds two energy points during activation")
                    break
                if "dowsing" in _action or "rod" in _action:
                    print("The Dowsing Rod changes a search result of 11-99 to a 1")
                    break
                if "paralysis" in _action or "wand" in _action:
                    print("The Paralysis Wand adds two to your hittable rolls for a combat")
                    break
                print("Please enter an item name")
        if "treasure" in _action:
            looking = True
            while looking:
                print("Which treasure?")
                _spam = 0
                for x in treasures:
                    _spam = + 1
                    print(str(_spam) + ". " + x.name)
                print(str(len(treasures) + 1) + ". Nevermind.")
                _where_to = input("which? ").casefold()

                #  see if it's a number
                try:
                    int(_where_to) + 1
                except ValueError:
                    print("Please enter a number")
                    continue
                if int(_where_to) == 1 + len(treasures):
                    break
                elif 0 < int(_where_to) < len(treasures) + 1:
                    tellme = treasures[int(_where_to) - 1]
                    print(tellme.description)
                    looking = False
                print("Please enter a valid number")
        if _action == "":
            return None


def linking(artifact):
    """Link an artifact"""
    print("lets link this bitch")
    print(artifact.name)
    link_value = 3
    return link_value


def activate(_to_activate):
    """Activate an artifact"""
    print("We will now activate " + _to_activate.name + ".")
    energy = 0
    numbers = activating()
    print("After processing, Your results were: " + str(numbers))  # Make prettier
    print("The artifact  whirls as it processes the results.")
    for x in numbers:
        if x < 0:
            print("The negaitve result causes the artifact to spark out of control!")
            get_hit(1)
        elif x == 0:
            print("The artifact seems unimpressed with your result of 0.")
        else:
            print("The artifact dings pleasantly at your result of" + str(x) + ".")
            energy += x
            print(str(x) + " energy has been added to your pool.")
    print("The artifact has " + str(energy) + " energy total.")
    if energy < 4:
        print("It needs 4 energy total to activate")
    elif energy == 4:
        print("You have accumulated enough enough energy!")
        print(yellow(_to_activate + " has been activated!"))
        _to_activate.activated = True
    elif energy > 4:
        print("You have created more than enough energy!")
        print(yellow(_to_activate + " has been activated!"))
        print("Your extra energy has been absorbed by The God's Hand")
        _to_activate.activated = True
        to_god_hand = energy - 4
        gods_hand(to_god_hand)
    return energy


def gods_hand(energy):
    """Add extra energy to god's hand. Remove skull days"""
    global godsHand  # I'm not sure why this needs a global here, but something like skulldays does not.
    godsHand += energy
    if godsHand >= 3:
        while godsHand >= 3:
            print("The power in the God's Hand has delayed the end of days.")
            skullDays.pop(0)
            print(red("There are " + str(skullDays[0] - day) + " days until the end of the world."))
            print("There is three less energy in the God's Hand")
            godsHand -= 3
            print("The God's Hand has " + str(godsHand) + " energy remaining inside.")
    else:
        print("The Gods hand has " + str(godsHand) + " energy inside.")
    print("With more " + str(3 - godsHand) + " energy, the God's Hand, it could push back the end of all things.")


def activating():
    """Play the activation minigame. """
    _search_table = ["A", "B", "C", "D", "E", "F", "G", "H"]
    _matching = ["A", "B", "C", "D", "E", "F", "G", "H"]
    _filled_table = False

    while not _filled_table:
        display_activate_table(_search_table)  # Display an amazing acii table.
        rolls(_search_table, "activate")  # rolls dice, places them.
        _is_there = []
        for x in range(0, int(len(_search_table) / 2)):
            if _search_table[x] == _search_table[x + 4]:
                print("the identical inputs cancel out, clearing their way.")
                _search_table[x] = _matching[x]
                _search_table[x + 4] = _matching[x + 4]
        for x in _matching:
            if x in _search_table:
                _is_there.append(x)
        if len(_is_there) == 0:
            _filled_table = True
    display_activate_table(_search_table)
    numbers = [_search_table[0] - _search_table[4], _search_table[1] - _search_table[5],
               _search_table[2] - _search_table[6], _search_table[3] - _search_table[7]]
    print(numbers)
    results = []
    for x in numbers:
        print(x)
        if x == 4:
            results.append(1)
        elif x == 5:
            results.append(2)
        elif 0 < x < 4:
            results.append(0)
        elif x < 0:
            results.append(x)

    print("Your attempt is absorbed by the artifact. Only your best rolls make an impact.")
    print(red("And your worst..."))
    if "Focus Charm" in toolbelt:
        print("You still have the Focus Charm on your toolbelt.")
        print("Using it will add three energy to the artifact.")
        print("Would you like to use it?")
        _action = input().casefold()
        if "y" in _action:
            print("You place the focus charm against the artifact.")
            print("It hums a pleasant tone and is absorbed by the artifact.")
            print("Three energy has been added to your results!")
            results.append(3)

    return results


def lab():
    """Allow player to activate an artifact, link an object or rest."""
    # all the things you do in your lab. this is going to be a big boy someday.
    print("You arrive at your lab.")
    while True:
        print("Would you like to Rest? Activate an artifact? Link an artifact? Check Inventory? "
              "Leave? Do you need help?")
        _action = input().casefold()
        # Rest
        if _action == "rest":
            print("You rest")
        elif "check" in _action:
            check_inventory()
        elif _action == "activate" or _action == "activate an artifact":
            if len(artifacts) > 0:
                print("Lets activate some bitches")
                print("Which artifact would you like to activate?")

                while True:
                    _to_activate = []
                    for x in artifacts:
                        if not x.activated:
                            _to_activate.append(x)
                    num = 0
                    for x in _to_activate:
                        num += 1
                        print(str(num) + ". " + x.name)
                    print(str(len(_to_activate) + 1) + ". Nevermind, none for now.")
                    print(str(len(_to_activate) + 2) + ". Help?")
                    print(str(len(_to_activate) + 3) + ". Check Inventory")
                    _what_to = input("Which would you like to activate? ").casefold()

                    try:
                        int(_what_to) + 1
                    except ValueError:
                        print("Please enter a number")
                        continue
                    if int(_what_to) == 1 + len(_to_activate):  # back out
                        break
                    elif int(_what_to) == 2 + len(_to_activate):  # go to the help menu
                        helper("activate")  # This one might be ok.
                    elif int(_what_to) == 3 + len(_to_activate):  # go to the help menu
                        check_inventory()
                    elif 0 < int(_what_to) < len(_to_activate) + 1:  # go to the location
                        _to_activate = _to_activate[int(_what_to) - 1]

                        # first attempt
                        energy = activate(_to_activate)

                        #  second attempt. There's probably a better way do this,
                        #  but its max three times, so it's not TOO bad.
                        if energy < 4:
                            print("With only " + str(energy) + " energy, you must continue on.")
                            print("You work well into the night and into the next day.")
                            day_advance()
                            print("As the sun rises, you are ready to try again")
                            input("Press enter to continue.")
                            energy = energy + activate(_to_activate)

                            # third Auto success
                            if energy < 4:
                                print("With only " + str(energy) + " energy, you must continue on.")
                                print("You work well into the night and into the next day.")
                                day_advance()
                                print("As the sun rises on your third attempt, you've got it!")
                                input("Press enter to continue.")
                                print(yellow(_to_activate.name + " has been activated!"))
                                _to_activate.activated = True
                        end_game()
                        break

                print("You are standing in your lab.")
            else:
                print("You have no artifacts to activate.")

        # Link
        elif _action == "link" or _action == "link an artifact":
            while True:
                unlinked = []
                for x in artifacts:
                    if not x.linked:
                        unlinked.append(x)
                if len(unlinked) > 0:
                    print("Lets link some bitches")
                    num = 0
                    for x in unlinked:
                        num += 1
                        print(str(num) + ". " + x.name)
                    print(str(len(unlinked) + 1) + ". Nevermind, none for now.")
                    print(str(len(unlinked) + 2) + ". Help?")
                    print(str(len(unlinked) + 3) + ". Check Inventory")
                    _what_to = input("Which would you like to Link? ").casefold()

                    try:
                        int(_what_to) + 1
                    except ValueError:
                        print("Please enter a number")
                        continue
                    if int(_what_to) == 1 + len(unlinked):  # back out
                        break
                    elif int(_what_to) == 2 + len(unlinked):  # go to the help menu
                        helper("link")  # This one might be ok.
                    elif int(_what_to) == 3 + len(unlinked):  # go to the help menu
                        check_inventory()
                    elif 0 < int(_what_to) < len(unlinked) + 1:  # go to the location
                        _to_link = unlinked[int(_what_to) - 1]

                        # first (only) attempt
                        link_value = linking(_to_link)
                        print(link_value)
                        end_game()

                else:
                    print("You have no artifacts to link.")
        elif _action == "leave":
            break
        elif _action == "help":
            helper("lab")
        else:
            print("Please enter a valid response")


def end_game():
    """Check if the player has triggered the end game"""
    completed = []
    for x in artifacts:
        if x.linked is True and x.activated is True:
            completed.append(x.name)
        print("The following artifacts have been linked and activated:")
        print(completed)
        if len(completed) == 6:
            print("You've done it! All the artifacts are active and linked!")
            print("It's time to activate")
            print(red("THE UTOPIA ENGINE"))


def search(_current_location):
    """Search specified location. Give loot or encounter based of result"""
    print("Day " + str(day))  # Just here for testing sanity
    print("explore attempt " + str(_current_location.exploreAttempt))  # Ditto
    if _current_location.exploreAttempt == 0:  # Check if player has been here.
        print("You begin your search of " + _current_location.name)
    else:
        print("You continue your search...")
    _search_result = searching()  # Search minigame!
    # searchResult = 1  # Just for debuggin'

    if _current_location.event == 3:  # Checks if good fortune event is happening.
        print("The good fortune of this area has aided your search")
        if _search_result > 10:  # There's probably a smarter way to do this.
            _search_result -= 10
        if _search_result <= 10:
            _search_result = 0
    print(green("Your search result is " + str(_search_result) + "."))
    if _search_result == 420 or _search_result == 69:
        print("nice.")  # Don't @ me.
    if "Dowsing Rod" in toolbelt and 11 < _search_result < 99:  # Checks dowsing rod
        print("Would you like to use your dowsing rod?")
        _action = input().casefold()
        if _action == "yes" or _action == "y":
            _search_result = 1
            toolbelt.remove("Dowsing Rod")
    else:
        input("Press Enter to Continue.")

    if 11 < _search_result < 100:  # Component result
        print("You find component " + _current_location.component + ".")
        if stores[_current_location.component] == 4:
            print(green("Your stores of " + str(stores[_current_location.component]) + " is already full with 4 pieces."))
        else:
            stores[_current_location.component] = stores[_current_location.component] + 1
            print(
                green("You now have " + str(stores[_current_location.component]) + " " + _current_location.component + "."))

    # Inactive Artifact result
    if 11 > _search_result >= 1:
        if _current_location.artifact.name not in artifacts:
            print(green("You find an inactive " + _current_location.artifact.name + "!"))
            artifacts.append(_current_location.artifact)
            print("That's an artifact! Only " + str(len(locations) - len(artifacts) + 1) + " to go!")
        else:
            print(green("You again find where " + _current_location.artifact.name + " once lay."))

    # active artifact result
    if _search_result == 0:
        if _current_location.Artifact not in [artifacts]:
            print("You find " + _current_location.Artifact.name + " already activated!")
            _current_location.artifact.activated = True
            artifacts.append(_current_location.artifact)
            print("That's an artifact! Only " + str(len(locations) - len(artifacts) + 1) + " to go!")
        else:
            print("You again find where " + _current_location.artifact.name + " once lay.")

    # Monster! Go to encounter function.
    if _search_result < 0 or _search_result > 99:
        print("You encounter a monster!")
        encounter(_current_location, _search_result)

    # print (currentLocation.timeAdvances)


def camp(_current_location):
    """Regenerate player health. Advance the day"""
    global health
    print("You make camp.")
    if health < 6:
        health += 1
        print("You feel a little better.")
        print("You spend the night under the stars of " +_current_location.name + ".")
        print("Your health is " + str(health))
        day_advance()
    else:
        print("You're in good health and do not need to camp.")


def explore():
    """Declare which location is to be searched. Give information about locations"""
    # player decides where they want to explore. gives info on location.
    while True:
        print("Where would you like to explore?")
        for x in locations:
            print(str(x.number) + ". " + x.name)
        print(str(len(locations) + 1) + ". Nevermind, Back to the lab")
        print(str(len(locations) + 2) + ". Help?")
        print(str(len(locations) + 3) + ". Check Inventory")
        _where_to = input("Where to? ").casefold()
        try:  # See if it's a number
            int(_where_to) + 1
        except ValueError:
            print("Please enter a number")
            continue

        if int(_where_to) == 1 + len(locations):  # go to the lab
            return "lab"  # I'm not too sure about this.
        elif int(_where_to) == 2 + len(locations):  # go to the help menu
            helper("exploring")  # This one might be ok.
        elif int(_where_to) == 3 + len(locations):  # go to the help menu
            check_inventory()
        elif 0 < int(_where_to) < len(locations) + 1:  # go to the location

            _current_location = locations[int(_where_to) - 1]

            while True:
                print("You arrive at " + _current_location.name + ".")
                location_desciption(_current_location)
                print("Would you like to search or leave?")
                _action = input().casefold()
                if _action == "leave":
                    break
                if _action == "search":
                    search(_current_location)
                    # sees if the explore attempt advances the timeline.
                    if _current_location.exploreAttempt in _current_location.timeAdvances:
                        day_advance()
                        if _current_location.event == 4:  # Advances another day if bad weather
                            print("The bad weather made searching take a very long time.")
                            day_advance()
                        print("You're exploration took all day.")
                    _current_location.exploreAttempt += 1

                    continue_search = True
                    while continue_search:  # Allows player to continue search, camp or exit
                        print("---------------------------------")
                        print("Day " + str(day))
                        print("Explore attempt " + str(_current_location.exploreAttempt))
                        print("You have " + str(health) + " health remaining.")
                        print(
                            "Would you like to search " + _current_location.name
                            + " again? Leave? Make camp? Check inventory? Info?")
                        _action = input().casefold()
                        if _action == "yes" or _action == "y" or _action == "search":
                            search(_current_location, )
                            if _current_location.exploreAttempt in _current_location.timeAdvances:
                                day_advance()
                                print("You're exploration took all day.")
                            _current_location.exploreAttempt += 1
                            # player finds artifacts after 6 attempts
                            if _current_location.exploreAttempt == 6 and _current_location.artifact not in artifacts:
                                print("After much exploring, you finally find the " + _current_location.artifact + "!")
                                print("It is not yet activated.")
                                artifacts.append(_current_location.artifact)
                        elif _action == "camp" or _action == "make camp":
                            camp(_current_location)
                        elif _action == "no" or _action == "n" or _action == "leave":
                            continue_search = False
                        elif _action == "help":
                            helper("search")
                        elif _action == "info":
                            location_desciption(_current_location)
                        elif _action == "check" or _action == "check inventory":
                            check_inventory()
                        else:
                            print("Please enter a correct response")

                else:
                    print("Please input a correct response")
                    continue
                print("Search again exit exits here")
                break
        else:
            print("Please enter a location number")

    # does anyone else use comments to just sorta muse?


def mainloop():
    """Allow player to choose what to do."""
    print("The end is coming unless you can build the Utopia Engine to stop it.")
    while True:
        print("It is day " + str(day) + " of your adventure.")
        print(red("There are " + str(skullDays[0] - day) + " days until the end of the world."))
        print("What would you like to do? Explore? Check inventory? Go to the lab? Help?")
        _action = input().casefold()

        if _action == "explore":
            _exit_reason = explore()
            if _exit_reason == "lab":
                lab()
        elif _action == "check inventory" or _action == "check" or _action == "inventory":
            check_inventory()
        elif _action == "go to the lab" or _action == "lab":
            lab()
        elif _action == "help":
            helper("main")
        else:
            print("command Not Recognized")


# It'd be cool be be able to stop and continue a game, but I have NO IDEA how that works yet.
# Also would be neat to have stats from each game "times explored," "times activated" and stuff
while True:
    print("Menu:")
    print("1. New game")
    print("2. Guide")
    action = input().casefold()
    if action == "1":
        # I could make a function that returns everything to starting values for repeat games.
        mainloop()
    elif action == "2":
        helper("start")
    else:
        print("Please input a number")

# things I'm concerned about:
# adding what the items do will be interesting. I guess a lot of if/ then stuff.
# add item functionality
# fix gethit events and stuff
