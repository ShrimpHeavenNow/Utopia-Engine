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

farts = ["1", "2", "3"]
print(len(farts))

print(blue("Welcome to Utopia Engine"))
print("This is a digital version of the incredible print and play board game of the same name")
print("By Nick Hayes.")
print("Be sure to check out the real thing. Look for it on BoardGameGeek.com")
day = 0
health = 30  # Make this a function as well?
# sets inventory to be empty
toolbelt = ["Paralysis Wand", "Dowsing Rod", "Focus Charm"]
stores = {"Silver": 0, "Quartz": 0, "Silica": 0, "Gum": 0, "Wax": 0, "Lead": 0}  # make limit of 4
# old artifacts = {"Seal of Balance": 0, "Hermetic Mirror": 0, "Void Gate": 0, "Golden Chassis": 0, "Scrying Lens": 0, "Crystal Battery": 0}
# old treasures = {"Ice Plate": 0, "Bracelet of Ios": 0, "Shimmering Moonlace": 0, "Scale of the Infinity Wurm": 0, "The Ancient Record": 0, "The Molten Shard": 0}
treasures = []
# DAYS, BABY
eventDays = [1, 2, 5, 8, 11, 14, 17, 20]
skullDays = [15, 16, 17, 18, 19, 20, 21, 22]
wastebasket = []
godsHand = 0


# monster class
class monster:
    def __init__(self, name, rank, spirit, attack, defense):
        self.name = name
        self.rank = rank
        self.spirit = spirit  # I guess this could have been a bool
        self.attack = attack
        self.defense = defense


# monsters
iceBear = monster("Ice Bear", 1, 0, [1], [5, 6])
rovingBandits = monster("Roving Bandits", 2, 0, [1], [6])
bloodWolves = monster("Blood Wolves", 3, 0, [1, 2], [6])
horseEaterHawk = monster("Horse Eater Hawk", 4, 0, [1, 2, 3], [6])
theHollowGiant = monster("The Hollow Giant", 5, 1, [1, 2, 3, 4], [6])
rogueThief = monster("Rogue Thief", 1, 0, [1], [5, 6])
blanketOfCrows = monster("Blanket of Crows", 2, 0, [1], [6])
hornbackBison = monster("Hornback Bison", 3, 0, [1, 2], [6])
grassybackTroll = monster("Grassyback Troll", 4, 0, [1, 2, 3], [6])
thunderKing = monster("Thunder King", 5, 0, [1, 2, 3, 4], [6])
gemscaleBoa = monster("Genscale Boa", 1, 0, [1], [5, 6])
ancientAlligator = monster("Ancient Alligator", 2, 0, [1], [6])
landShark = monster("Land Shark", 3, 0, [1, 2], [6])
abyssalLeech = monster("Abyssal Leech", 4, 1, [1, 2, 3], [6])
dwellerInTheTides = monster("Dweller in the Tides", 5, 0, [1, 2, 3, 4], [6])
fiestyGoblins = monster("Fiesty Goblins", 1, 0, [1], [5, 6])
glasswingDrake = monster("Glasswing Drake", 2, 0, [1], [6])
reachingClaws = monster("Reaching Claws", 3, 1, [1, 2], [6])
terribleWurm = monster("Terrible Wurm", 4, 0, [1], [6])
infinityWurm = monster("Infinity Wurm", 5, 1, [1, 2, 3, 4], [6])
graveRobbers = monster("Grave Robbers", 1, 0, [1], [5, 6])
ghostLights = monster("Ghost Lights", 2, 1, [1], [6])
vengefulShade = monster("Vengeful Shade", 3, 0, [1, 2], [6])
nightmareCrab = monster("Nightmare Crab", 4, 0, [1, 2, 3], [6])
theUnnamed = monster("Unnamed", 5, 0, [1, 2, 3, 4], [6])
minorImp = monster("Minor Imp", 1, 0, [1], [5, 6])
renegadeWarlock = monster("Renegade Warlock", 2, 0, [1], [6])
giantFlamingLizard = monster("Giant Flaming Lizard", 3, 0, [1, 2], [6])
sparkElemental = monster("Spark Elemental", 4, 1, [1, 2, 3], [6])
volcanoSpirit = monster("Volcano Spirit", 5, 1, [1, 2, 3, 4], [6])

# Artifacts
class artifact:
    def __init__(self, name, activated, component, linked, linkvalue,description):
        self.name = name
        self.activated = False
        self.component = component
        self.linked = False
        self.linkvalue = linkvalue
        self.description = description

sealOfBalance = artifact("Seal of Balance", False, "Quartz", False, 0, "A literal baby seal.")
hermeticMirror = artifact("Hermetic Mirror", False, "Wax", False, 0, "A mirror")
voidGate = artifact("Void Gate", False, "Silica", False, 0, "It hurts to look at")
scryingLens = artifact("Scrying Lens", False, "Lead", False, 0, "Hey guys, it's scrying its best.")
crystalBattery = artifact("Crystal Battery", False, "Gum", False, 0, "From Tesla (tm)")
goldenChassis = artifact("Golden Chassis", False, "Silver", False, 0, "A Chassis showered in gold.")

artifacts = [sealOfBalance]  # sets artifact inventory

# Set locations and their loot. I made it so you could easily add more, for some reason.
class location:
    def __init__(self, number, name, component, artifact, treasure, daysSearched, timeAdvances, encounters, event,
                 exploreAttempt):
        self.number = number
        self.name = name
        self.component = component
        self.artifact = artifact
        self.treasure = treasure
        self.daysSearched = daysSearched
        self.timeAdvances = timeAdvances
        self.encounters = encounters
        self.event = event  # 0 is none, 1 is active, 2 is fleeting, 3 is good, 4 is foul
        self.exploreAttempt = exploreAttempt


halbeardPeak = location(1, "Halbeard Peak", "Silver", sealOfBalance, "Ice Plate", 0, [0, 1, 3],
                        [iceBear, rovingBandits, bloodWolves, horseEaterHawk, theHollowGiant], 0, 0)
theGreatWilds = location(2, "The Great Wilds", "Quartz", hermeticMirror, "Bracelet of Ios", 0, [0, 3],
                         [rogueThief, blanketOfCrows, hornbackBison, grassybackTroll, thunderKing], 0, 0)
rootStrangledMarshes = location(3, "Root-Strangled Marshes", "Gum", voidGate, "Shimmering Moonlace", 0, [0, 2, 4],
                                [gemscaleBoa, ancientAlligator, landShark, abyssalLeech, dwellerInTheTides], 0, 0)
glassrockCanyon = location(4, "Glassrock Canyon", "Silica", goldenChassis, "Scale of the Infinity Wurm", 0,
                           [0, 1, 3, ], [fiestyGoblins, glasswingDrake, reachingClaws, terribleWurm, infinityWurm], 0,
                           0)
ruinedCityOfTheAncients = location(5, "Ruined City of the Ancients", "Wax", scryingLens, "Ancient Record", 0,
                                   [0, 2, 4], [graveRobbers, ghostLights, vengefulShade, nightmareCrab, theUnnamed], 0,
                                   0)
theFieryMaw = location(6, "The Fiery Maw", "Lead", crystalBattery, "Molten Shard", 0, [0, 1, 2, 4],
                       [minorImp, renegadeWarlock, giantFlamingLizard, sparkElemental, volcanoSpirit], 0, 0)

locations = [halbeardPeak,
             theGreatWilds,
             rootStrangledMarshes,
             glassrockCanyon,
             ruinedCityOfTheAncients,
             theFieryMaw]


def helper(gamePlace):
    # gives general help based off what menu they came here from.
    print("You were in the " + str(gamePlace) + " menu.")
    print("You are beyond help.")


def dayAdvance():
    # Advances time track
    global day
    day += 1
    if day in eventDays:  # check against event
        events()
    if day in skullDays:  # check against skulls
        print("You LOSE! Good DAY sir!")
        # End game somehow.
    print(red("There are " + str(skullDays[0] - day) + " days until the end of the world."))


def events():
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


def encounter(currentLocation, searchResult):
    # Monster fight!
    monsterAlive = True

    # active monster event
    if currentLocation.event == 1 and searchResult < 0:
        searchResult -= 200
    elif currentLocation == 1 and searchResult > 100:
        searchResult += 200

    # Determine monster level
    if 100 <= int(searchResult) <= 199 or -1 >= int(searchResult) >= -100:
        fighter = currentLocation.encounters[0]
        print("You encounter a " + fighter.name + "!")
    elif 200 <= int(searchResult) <= 299 or -101 >= int(searchResult) >= -200:
        fighter = currentLocation.encounters[1]
        print("You encounter a " + fighter.name + "!")
    elif 300 <= int(searchResult) <= 399 or -201 >= int(searchResult) >= -300:
        fighter = currentLocation.encounters[2]
        print("You encounter a " + fighter.name + "!")
    elif 400 <= int(searchResult) <= 499 or -301 >= int(searchResult) >= -400:
        fighter = currentLocation.encounters[3]
        print("You encounter a " + fighter.name + "!")
    elif 500 <= int(searchResult) <= 555 or -401 >= int(searchResult) >= -555:
        fighter = currentLocation.encounters[4]
        print("You encounter a " + fighter.name + "!")

    # Add alter the monster based on items
    # if "Ice Plate" in treasures: or whatever
    # have to make sure the this happens just in this function (which I think we do by declaring the fighter variable.)

    if fighter.spirit == 1:
        print("The monster is a spirit!")
        # something about an item here.

    while monsterAlive:
        input("Press enter to fight for your life!")
        rolls = [random.randint(1, 6), random.randint(1, 6)]
        print("The Monster rolled a " + str(rolls[0]))
        print("You rolled a " + str(rolls[1]))
        if rolls[0] in fighter.attack:
            hitResult = getHit()
            if hitResult == "dead":
                input(
                    "You're dead")  # Where do I do the scoring funtion? should I keep retuning until I'm in main loop?
            if hitResult == "unconscious":
                input("you're unconscious")  # kick them back to main loop?
        else:
            print("The monster misses")  # make a list with a bunch of fun descriptions and have it choose randomly
        if rolls[1] in fighter.defense:
            print(green("You hit the monster! It is slain!"))
            # make a list with a bunch of fun descriptions and have it choose randomly
            if fighter.rank == 5 and currentLocation.treasure not in treasures:
                treasures.append(currentLocation.treasure)
                print("The mighty creature was guarding an amazing treasure, the " + currentLocation.treasure + ".")
                monsterAlive = False
            else:
                print("The " + fighter.name + " drops " + currentLocation.component)
                stores[currentLocation.component] += 1
                print("You now have " + str(stores[currentLocation.component]) + " " + currentLocation.component)
                monsterAlive = False
        else:
            print("You miss!")


def displayTable(searchTable):
    # Display an amazing acii table.
    print("-------")
    print("|" + str(searchTable[0]) + "|" + str(searchTable[1]) + "|" + str(searchTable[2]) + "|")
    print("-------")
    print("|" + str(searchTable[3]) + "|" + str(searchTable[4]) + "|" + str(searchTable[5]) + "|")
    print("-------")


def displayActivateTable(searchTable):
    # Display an amazing acii table.
    print("--- --- --- ---")
    print("|" + str(searchTable[0]) + "| |" + str(searchTable[1]) + "| |" + str(searchTable[2]) + "| |" + str(
        searchTable[3]) + "|")
    print("--- --- --- ---")
    print("|" + str(searchTable[4]) + "| |" + str(searchTable[5]) + "| |" + str(searchTable[6]) + "| |" + str(
        searchTable[7]) + "|")
    print("--- --- --- ---")


def rolls(table, type):
    placedRoll = False
    rolls = [random.randint(1, 6), random.randint(1, 6)]
    print("You've rolled " + str(rolls[0]) + " and " + str(rolls[1]) + ".")

    # Place First Roll.
    while placedRoll == False:
        print("Where would you like your first roll, a " + str(rolls[0]) + " to be placed?")
        rollPlacement = input().upper()
        if rollPlacement in table:
            tablePlace = -1
            for x in table:
                tablePlace += 1
                if x == rollPlacement:
                    print("it was " + str(table[tablePlace]))
                    table[tablePlace] = rolls[0]
                    print("Now It's " + str(table[tablePlace]))
                    placedRoll = True
        elif rollPlacement == "help":
            helper("rolling")
        else:
            print("select an unassigned location")
    placedRoll = False

    # Place Second Roll
    if type == "search" or type == "link":
        displayTable(table)
    if type == "activate":
        displayActivateTable(table)

    while placedRoll == False:
        print("Where would you like your second roll, a " + str(rolls[1]) + " to be placed?")
        rollPlacement = input().upper()
        if rollPlacement in table:
            tablePlace = -1
            for x in table:
                tablePlace += 1
                if x == rollPlacement:
                    print("it was " + str(table[tablePlace]))
                    table[tablePlace] = rolls[1]
                    print("Now It's " + str(table[tablePlace]))
                    placedRoll = True
        else:
            print("select an unassigned location")


def getHit():
    global health
    global day
    print(red("You've been hurt!"))
    health -= 1
    if health == 0:
        print("As you fall unconscious, the dazzling light of your amulet teleports you to safety.")
        for x in range(5):
            day += 1
            if day in eventDays:
                eventsHappened = True
            if day in skullDays:
                print("While you're recovering, the end arrives. all is lost.")
                input("You LOSE!")
                return "time"
        print("Six days pass and you are back to full health.")
        health = 6
        print("While you've been unconscious, all your search progress has been reset.")
        for x in locations:
            x.exploreAttempt = 0
        if eventsHappened == True:
            print("The world has shifted and events have occured")
            # Event function
        return "unconscious"
    if health < 0:
        print("You have died.")
        return "dead"
    print("You have " + str(health) + " health remaining")


def searching():
    # the self contained search minigame. just spits out a number. no day advances or nothin'
    searchTable = ["A", "B", "C", "D", "E", "F"]
    matching = ["A", "B", "C", "D", "E", "F"]
    filledTable = False

    while filledTable == False:
        isThere = []
        displayTable(searchTable)  # Display an amazing acii table.
        rolls(searchTable, "search")  # rolls dice, places them.
        # A very shitty way to make sure the whole table is filled in.
        for x in matching:
            if x in searchTable:
                isThere.append(x)
            print(isThere)
        if len(isThere) == 0:
            filledTable = True
    displayTable(searchTable)
    topNumber = int(str(searchTable[0]) + str(searchTable[1]) + str(searchTable[2]))
    bottomNumber = int(str(searchTable[3]) + str(searchTable[4]) + str(searchTable[5]))
    searchResult = topNumber - bottomNumber
    # make this prettier!
    return searchResult


def locationDesciption(currentLocation):
    # Describes the location. This function could probably have been defined in the search function,
    # but I'm currently too afraid to do that yet because of scopes.
    print("Here you will find " + currentLocation.component + ".")
    if currentLocation.artifact in artifacts:
        print("Here you found " + currentLocation.artifact.name + ".")
    else:
        print("Hidden somewhere is the " + currentLocation.artifact.name + ".")
    if currentLocation.treasure in treasures:
        print("Here you found " + currentLocation.treasure + ".")
    else:
        print("It's said a powerful monster carries " + currentLocation.treasure + " here.")
    print("Searching here would advance the day following these attempts: " + str(
        currentLocation.timeAdvances))  # make this pretty.
    print("You've explored here " + str(currentLocation.exploreAttempt) + " times")
    descriptions = ["There are no events here currently.", "The monsters here are active. Combat will be more deadly.",
                    "Fleeting visions run across these lands. Its artifact will be easier to activate.",
                    "You have a good feeling about this place. Searching here should be a little easier.",
                    "The weather here is terrible. Days spent searching will take twice as long."]
    print(descriptions[currentLocation.event])  # This makes me feel so smart.
    # if currentLocation.event == 0:
    #    print("There are no events here currently.")
    # if currentLocation.event == 1:
    #    print("The monsters here are active. Combat will be more deadly.")
    # if currentLocation.event == 2:
    #    print("Fleeting visions run across these lands. Its artifact will be easier to activate.")
    # if currentLocation.event == 3:
    #    print("You have a good feeling about this place. Searching here should be a little easier.")
    # if currentLocation.event == 4:
    #    print("The weather here is terrible. Days spent searching will take twice as long.")


def checkInventory():
    # prints your inventory.
    print("You open your bag and see...")
    # List Components
    for x, y in stores.items():
        print(x, y)
    # List Artifacts
    showItems = ""
    if len(artifacts) == 0:
        print("You have no artifacts")
    else:
        for x in artifacts:
            showItems += x.name
            showItems += ", "
        print("You have the following artifacts: " + showItems + ".")  # fix formatting of last item
    # list activated artifacts
    showItems = ""
    for x in artifacts:
        if x.activated == True:
                showItems += x.name
                showItems += ", "
        if showItems != "":
            print("You have the following activated artifacts: " + showItems + ".")  # fix formatting of last item
        else:
            print("You have no activated artifacts")
    # List Treasures
    showItems = ""
    if len(treasures) == 0:
        print("You have no treasures.")
    else:
        for x in treasures:
            showItems += x
            showItems += ", "
        print("You have the following treasures: " + showItems + ".")  # fix formatting of last item
    # Add Tool belt
    showitems = ""
    if len(toolbelt) == 0:
        print("You have used all your tools")
    else:
        for x in toolbelt:
            showItems += x
            showItems += ", "
        print("You have the following tools availible: " + showItems + ".")  # fix formatting of last item
    while True:
        print("Actifact info? Tool info? or move on?")
        action = input().casefold()
        if "artifact" in action:
            print("Which artifact?")
            for x in artifacts:
                if x.activated == True:
                    showItems += x
                    showItems += ", "
                if showItems != "":
                    print("You have the following activated artifacts: " + showItems + ".")
            action = input().casefold()
             #if action in artifacts.name



def linking(artifact):
    print("lets link this bitch")


def activate(toActivate):
    print("We will now activate " + toActivate.name + ".")
    energy = 0
    numbers = activating()
    print("After processing, Your results were: " + str(numbers))  # Make prettier
    print("The artifact  whirls as it processes the results.")
    for x in numbers:
        if x < 0:
            print("The negaitve result causes the artifact to spark out of control!")
            getHit()
        elif x == 0:
            print("The artifact seems unimpressed with your result of 0.")
        else:
            print("The artifact dings pleasantly at your result.")
            energy += x
            print(str(x) + " energy has been added to your pool.")
    print("The artifact has " + str(energy) + " energy total.")
    if energy < 4:
        print("It needs 4 energy total to activate")
    elif energy == 4:
        print("You have accumulated enough enough energy!")
        print(yellow(toActivate + " has been activated!"))
        toActivate.activated = True
    elif energy > 4:
        print("You have created more than enough energy!")
        print(yellow(toActivate + " has been activated!"))
        print("Your extra energy has been absorbed by The God's Hand")
        toActivate.activated = True
        toGodhand = energy - 4
        godshand(toGodhand)

    return energy


def godshand(energy):
    global godsHand
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
    global results
    searchTable = ["A", "B", "C", "D", "E", "F", "G", "H"]
    matching = ["A", "B", "C", "D", "E", "F", "G", "H"]
    filledTable = False
    numbers = []

    while filledTable == False:
        displayActivateTable(searchTable)  # Display an amazing acii table.
        rolls(searchTable, "activate")  # rolls dice, places them.
        isThere = []
        # A very shitty way to make sure the whole table is filled in.

        for x in range(0, int(len(searchTable) / 2)):

            print(str(searchTable[x]) + " : " + str(searchTable[x - 4]))
            if searchTable[x] == searchTable[x + 4]:
                print("the identical inputs cancel out, clearing their way.")
                searchTable[x] = matching[x]
                searchTable[x + 4] = matching[x + 4]
        for x in matching:
            if x in searchTable:
                isThere.append(x)
            print(isThere)
        if len(isThere) == 0:
            filledTable = True
        # if "A" not in searchTable and "B" not in searchTable and "C" not in searchTable and "D" not in searchTable and "E" not in searchTable and "F" not in searchTable and "G" not in searchTable and "H" not in searchTable:  # This sucks and there is definitely a better way.
        #    filledTable = True
    displayActivateTable(searchTable)
    numbers.append(searchTable[0] - searchTable[4])  # I bet there's a very clever way to do this in one line.
    numbers.append(searchTable[1] - searchTable[5])
    numbers.append(searchTable[2] - searchTable[6])
    numbers.append(searchTable[3] - searchTable[7])
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
        action = input().casefold()
        if action == "yes" or action == "y":
            print("You place the focus charm against the artifact.")
            print("It hums a pleasant tone and is absorbed by the artifact.")
            print("Three energy has been added to your results!")
            results.append(3)
    return results


def lab():
    # all the things you do in your lab. this is going to be a big boy someday.
    print("You arrive at your lab.")
    while True:
        print("Would you like to Rest? Activate an artifact? Link an artifact? Leave? Do you need help?")
        action = input().casefold()
        # Rest
        if action == "rest":
            print("You rest")
        # activate
        elif action == "activate" or action == "activate an artifact":
            if len(artifacts) > 0:
                print("Lets activate some bitches")
                print("Which artifact would you like to activate?")

                while True:
                    toActivate = []
                    for x in artifacts:
                        if x.activated == False:
                            toActivate.append(x)
                    num = 0
                    for x in toActivate:
                        num += 1
                        print(str(num) + ". " + x.name)
                    print(str(len(toActivate) + 1) + ". Nevermind, none for now.")
                    print(str(len(toActivate) + 2) + ". Help?")
                    print(str(len(toActivate) + 3) + ". Check Inventory")
                    whatTo = input("Which would you like to activate? ").casefold()

                    try:
                        int(whatTo) + 1
                    except ValueError:
                        print("Please enter a number")
                        continue
                    if int(whatTo) == 1 + len(toActivate):  # back out
                        break
                    elif int(whatTo) == 2 + len(toActivate):  # go to the help menu
                        helper("activate")  # This one might be ok.
                    elif int(whatTo) == 3 + len(toActivate):  # go to the help menu
                        checkInventory()
                    elif int(whatTo) > 0 and int(whatTo) < len(toActivate) + 1:  # go to the location
                        toActivate = toActivate[int(whatTo) - 1]

                        # first attempt
                        energy = activate(toActivate)

                        #  second attempt. There's probably a better way do this,
                        #  but its max three times, so it's not TOO bad.
                        if energy < 4:
                            print("With only " + str(energy) + " energy, you must continue on.")
                            print("You work well into the night and into the next day.")
                            dayAdvance()
                            print("As the sun rises, you are ready to try again")
                            input("Press enter to continue.")
                            energy = energy + activate(toActivate)

                            # third Auto success
                            if energy < 4:
                                print("With only " + str(energy) + " energy, you must continue on.")
                                print("You work well into the night and into the next day.")
                                dayAdvance()
                                print("As the sun rises on your third attempt, you've got it!")
                                input("Press enter to continue.")
                                print(yellow(toActivate + " has been activated!"))
                                toActivate.activated = True
                        endGame()
                        break

                print("You are standing in your lab.")
            else:
                print("You have no artifacts to activate.")

        # Link
        elif action == "link" or action == "link an artifact":
            linked = []
            for x in artifacts:
                if x.linked == False:
                    linked.append(x)
            if len(linked) > 0:
                print("Lets link some bitches")
                endGame()
            else:
                print("You have no artifacts to activate.")
        elif action == "leave":
            break
        elif action == "help":
            helper("lab")
        else:
            print("Please enter a valid response")



def endGame():
    completed = []
    for x in artifacts:
        if x.linked == True and x.activated == True:
            completed.append(x.name)
        print("The following artifacts have been linked and activated:")
        print(completed)
        if len(completed) == 6:
            print("You've done it! All the artifacts are active and linked!")
            print("It's time to activate")
            print(red("THE UTOPIA ENGINE"))


def search(currentLocation):
    # Has you explore a location. Gives you loot or an encounter based off searching function.
    # also currently advances the day based on the exploreAttempt number.
    print("Day " + str(day))  # Just here for testing sanity
    print("explore attempt " + str(currentLocation.exploreAttempt))  # Ditto
    # see if its their first time exploring here
    if currentLocation.exploreAttempt == 0:
        print("You begin your search of " + currentLocation.name)
    else:
        print("You continue your search...")

    # search minigame!
    searchResult = searching()
    # searchResult = 50  # just for debuggin'
    # Checks if good fortune event is happening.
    if currentLocation.event == 3:
        print("The good fortune of this area has aided your search")
        if searchResult > 10:
            searchResult -= 10
        if searchResult <= 10:
            searchResult = 0
    print(green("Your search result is " + str(searchResult) + "."))
    if searchResult == 420 or searchResult == 69:
        print("nice.")

    if "Dowsing Rod" in toolbelt and 11 < searchResult < 99:
        print("Would you like to use your dowsing rod?")
        action = input().casefold()
        if action == "yes" or action == "y":
            searchResult = 1
    else:
        input("Press Enter to Continue.")
    # component result
    if 11 < searchResult < 100:
        print("You find component " + currentLocation.component + ".")
        if stores[currentLocation.component] == 4:
            print(green("Your stores of " + stores[currentLocation.component] + " is already full with 4 pieces."))
        else:
            stores[currentLocation.component] = stores[currentLocation.component] + 1
            print(
                green("You now have " + str(stores[currentLocation.component]) + " " + currentLocation.component + "."))

    # Inactive Artifact result
    if 11 > searchResult >= 1:
        if currentLocation.artifact.name not in artifacts:
            print(green("You find an inactive " + currentLocation.artifact.name + "!"))
            artifacts.append(currentLocation.artifact)
            print("That's an artifact! Only " + str(len(locations) - len(artifacts) + 1) + " to go!")
        else:
            print(green("You again find where " + currentLocation.artifact.name + " once lay."))

    # active artifact result
    if searchResult == 0:
        if  currentLocation.artifact not in [artifacts]:
            print("You find " + currentLocation.artifact.name + " already activated!")
            currentLocation.artifact.activated = True
            artifacts.append(currentLocation.artifact)
            print("That's an artifact! Only " + str(len(locations) - len(artifacts) + 1) + " to go!")
        else:
            print("You again find where " + currentLocation.artifact.name + " once lay.")

    # Monster! Go to encounter function.
    if searchResult < 0 or searchResult > 99:
        print("You encounter a monster!")
        encounter(currentLocation, searchResult)

    # print (currentLocation.timeAdvances)


def camp(currentLocation):
    global health
    print("You make camp.")
    if health < 6:
        health += 1
        print("You feel a little better.")
        print("Your health is " + str(health))
        dayAdvance()
    else:
        print("You're in good health and do not need to camp.")


def explore():
    # player decides where they want to explore. gives info on location.
    while True:
        print("Where would you like to explore?")
        for x in locations:
            print(str(x.number) + ". " + x.name)
        print(str(len(locations) + 1) + ". Nevermind, Back to the lab")
        print(str(len(locations) + 2) + ". Help?")
        print(str(len(locations) + 3) + ". Check Inventory")
        whereTo = input("Where to? ").casefold()

        #  see if it's a number
        try:
            int(whereTo) + 1
        except ValueError:
            print("Please enter a number")
            continue
        if int(whereTo) == 1 + len(locations):  # go to the lab
            return "lab"  # I'm not too sure about this.
        elif int(whereTo) == 2 + len(locations):  # go to the help menu
            helper("exploring")  # This one might be ok.
        elif int(whereTo) == 3 + len(locations):  # go to the help menu
            checkInventory()
        elif int(whereTo) > 0 and int(whereTo) < len(locations) + 1:  # go to the location

            currentLocation = locations[int(whereTo) - 1]

            while True:
                print("You arrive at " + currentLocation.name + ".")
                locationDesciption(currentLocation)
                print("Would you like to search or leave?")
                action = input().casefold()
                if action == "leave":
                    break
                if action == "search":
                    search(currentLocation)
                    # sees if the explore attempt advances the timeline.
                    if currentLocation.exploreAttempt in currentLocation.timeAdvances:
                        dayAdvance()
                        if currentLocation.event == 4:  # Advances another day if bad weather
                            print("The bad weather made searching take a very long time.")
                            dayAdvance()
                        print("You're exploration took all day.")
                    currentLocation.exploreAttempt += 1
                    continueSearch = True

                    #  allows player to continue search, camp or exit
                    while continueSearch:
                        print("---------------------------------")
                        print("Day " + str(day))
                        print("Explore attempt " + str(currentLocation.exploreAttempt))
                        print("You have " + str(health) + " health remaining.")
                        print(
                            "Would you like to search " + currentLocation.name + " again? Leave? Make camp? Check inventory? Info?")
                        action = input().casefold()
                        if action == "yes" or action == "y" or action == "search":
                            search(currentLocation, )
                            if currentLocation.exploreAttempt in currentLocation.timeAdvances:
                                dayAdvance()
                                print("You're exploration took all day.")
                            currentLocation.exploreAttempt += 1
                            # player finds artifacts after 6 attempts
                            if currentLocation.exploreAttempt == 6 and currentLocation.artifact not in artifacts:
                                print("After much exploring, you finally find the " + currentLocation.artifact + "!")
                                print("It is not yet activated.")
                                artifacts.append(currentLocation.artifact)
                        elif action == "camp" or action == "make camp":
                            camp(currentLocation)
                        elif action == "no" or action == "n" or action == "leave" or action == "get the fuck out of here":
                            continueSearch = False
                        elif action == "help":
                            helper(search)
                        elif action == "info":
                            locationDesciption(currentLocation)
                        elif action == "check" or action == "check inventory":
                            checkInventory()
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
    exitReason = ""  # This is not very useful yet.
    # player where/ what to do. We may not come here often, actually.
    print("The end is coming unless you can build the Utopia Engine to stop it.")
    while True:
        print("It is day " + str(day) + " of your adventure.")
        print(red("There are " + str(skullDays[0] - day) + " days until the end of the world."))
        print("What would you like to do? Explore? Check inventory? Go to the lab? Help?")
        action = input().casefold()

        if action == "explore":
            exitReason = explore()
        if action == "check inventory" or action == "check" or action == "inventory":
            checkInventory()
        if action == "go to the lab" or action == "lab" or exitReason == "lab":
            lab()
        if action == "help":
            helper("main")
        else:
            print("command Not Recognized")


mainloop()

# things I'm concerned about:
# Changing the inventory inside these functions. Will they stick? I need to get my head around global variables.
# adding what the items do will be interesting. I guess a lot of if/ then stuff.
# make a function for advancing the timeline. checking against the event and skull days.
# add item functionality
