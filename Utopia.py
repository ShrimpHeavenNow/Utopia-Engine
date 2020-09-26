import random

# In general, UX is horrible. I'll go back and gussie her up once its functioning.


print("Welcome to Utopia Engine")
day = 0
health = 6  # Make this a function as well?
# sets inventory to be empty
toolbelt = ["Paralysis Wand", "Dowsing rod", "Focus Charm"]
stores = {"Silver": 0, "Quartz": 0, "Silica": 0, "Gum": 0, "Wax": 0, "Lead": 0}
# old artifacts = {"Seal of Balance": 0, "Hermetic Mirror": 0, "Void Gate": 0, "Golden Chassis": 0, "Scrying Lens": 0, "Crystal Battery": 0}
artifacts = []
activated = []
# old treasures = {"Ice Plate": 0, "Bracelet of Ios": 0, "Shimmering Moonlace": 0, "Scale of the Infinity Wurm": 0, "The Ancient Record": 0, "The Molten Shard": 0}
treasures = []
# DAYS, BABY
eventDays = [2, 5, 8, 11, 14, 17, 20]
skullDays = [15, 16, 17, 18, 19, 20, 21, 22]


# monster class
class monster:
    def __init__(self, name, rank, spirit, attack, defense):
        self.name = name
        self.rank = rank
        self.spirit = spirit
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


# Set locations and their loot. I made it so you could easily add more, for some reason.
class location:
    def __init__(self, number, name, component, artifact, treasure, daysSearched, timeAdvances, encounters, event):
        self.number = number
        self.name = name
        self.component = component
        self.artifact = artifact
        self.treasure = treasure
        self.daysSearched = daysSearched
        self.timeAdvances = timeAdvances
        self.encounters = encounters
        self.event = event # 0 is none, 1 is active, 2 is fleeting, 3 is good, 4 is foul


halbeardPeak = location(1, "Halbeard Peak", "Silver", "Seal of Balance", "Ice Plate", 0, [0, 1, 3],
                        [iceBear, rovingBandits, bloodWolves, horseEaterHawk, theHollowGiant], 0)
theGreatWilds = location(2, "The Great Wilds", "Quartz", "Hermetic Mirror", "Bracelet of Ios", 0, [0, 3],
                         [rogueThief, blanketOfCrows, hornbackBison, grassybackTroll, thunderKing], 0)
rootStrangledMarshes = location(3, "Root-Strangled Marshes", "Gum", "Void Gate", "Shimmering Moonlace", 0, [0, 2, 4],
                                [gemscaleBoa, ancientAlligator, landShark, abyssalLeech, dwellerInTheTides], 0)
glassrockCanyon = location(4, "Glassrock Canyon", "Silica", "Golden Chassis", "Scale of the Infinity Wurm", 0,
                           [0, 1, 3, ], [fiestyGoblins, glasswingDrake, reachingClaws, terribleWurm, infinityWurm], 0)
ruinedCityOfTheAncients = location(5, "Ruined City of the Ancients", "Wax", "Scrying Lens", "Ancient Record", 0,
                                   [0, 2, 4], [graveRobbers, ghostLights, vengefulShade, nightmareCrab, theUnnamed], 0)
theFieryMaw = location(6, "The Fiery Maw", "Lead", "Crystal Battery", "Molten Shard", 0, [0, 1, 2, 4],
                       [minorImp, renegadeWarlock, giantFlamingLizard, sparkElemental, volcanoSpirit], 0)

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
    # check against event
    # add events to location
    # check skulls
    # End Game

def encounter(currentLocation, searchResult):
    # Monster fight!
    global health
    monsterAlive = True
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

    while monsterAlive:
        rolls = [random.randint(1, 6), random.randint(1, 6)]
        print("The Monster rolled a " + str(rolls[0]))
        print("You rolled a " + str(rolls[1]))
        if rolls[0] in fighter.attack:
            print("It hits you!")  # make a list with a bunch of fun descriptions and have it choose randomly)
            health -= 1  # make a takes damage function
            print("Your health is " + str(health))
            #  like a whole thing to see if they're dead
        else:
            print("The monster misses")  # make a list with a bunch of fun descriptions and have it choose randomly)
        if rolls[1] in fighter.defense:
            print(
                "You hit the monster! It is slain!")  # make a list with a bunch of fun descriptions and have it choose randomly)
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

def searching():
    # the self contained search minigame. just spits out a number. no day advances or nothin'
    searchTable = ["A", "B", "C", "D", "E", "F"]
    filledTable = False

    while filledTable == False:
        placedRoll = False
        print("We gonna roll some dice now, son. Check this shit out:")
        # Display an amazing acii table.
        displayTable(searchTable)
        rolls = [random.randint(1, 6), random.randint(1, 6)]
        print("You've rolled " + str(rolls[0]) + " and " + str(rolls[1]) + ".")

        # Place First Roll. Yes, I should have made this a function.
        # Actually, I should. I can use it in the activation steps. Wow!
        while placedRoll == False:
            print("Where would you like your first roll, a " + str(rolls[0]) + " to be placed?")
            rollPlacement = input().upper()
            if rollPlacement in searchTable:
                tablePlace = -1
                for x in searchTable:
                    tablePlace += 1
                    if x == rollPlacement:
                        print("it was " + str(searchTable[tablePlace]))
                        searchTable[tablePlace] = rolls[0]
                        print("Now It's " + str(searchTable[tablePlace]))
                        placedRoll = True
            else:
                print("select an unassigned location")
        placedRoll = False

        # Place Second Roll
        displayTable(searchTable)
        while placedRoll == False:
            print("Where would you like your second roll, a " + str(rolls[1]) + " to be placed?")
            rollPlacement = input().upper()
            if rollPlacement in searchTable:
                tablePlace = -1
                for x in searchTable:
                    tablePlace += 1
                    if x == rollPlacement:
                        print("it was " + str(searchTable[tablePlace]))
                        searchTable[tablePlace] = rolls[1]
                        print("Now It's " + str(searchTable[tablePlace]))
                        placedRoll = True
            else:
                print("select an unassigned location")
        # A very shitty way to make sure the whole table is filled in.
        if "A" not in searchTable and "B" not in searchTable and "C" not in searchTable and "D" not in searchTable and "E" not in searchTable and "F" not in searchTable:  # This sucks and there is definitely a better way.
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
        print("Here you found " + currentLocation.artifact + ".")
    else:
        print("Hidden somewhere is the " + currentLocation.artifact + ".")
    if currentLocation.treasure in treasures:
        print("Here you found " + currentLocation.treasure + ".")
    else:
        print("It's said a powerful monster carries " + currentLocation.treasure + " here.")
    print("Searching here would advance the day following these attempts: " + str(
        currentLocation.timeAdvances))  # make this pretty.


def checkInventory():
    # prints your inventory.
    print("You open your bag and see...")
    # List Components
    for x, y in stores.items():
        print(x, y)
    # List Artifacts
    showItems = ""
    for x in artifacts:
        showItems += x
        showItems += ", "
    print("You have the following artifacts: " + showItems + ".")  # fix formatting of last item
    # list activated artifacts
    showItems = ""
    for x in activated:
        showItems += x
        showItems += ", "
    print("You have the following artifacts: " + showItems + ".")  # fix formatting of last item
    # List Treasures
    showItems = ""
    for x in treasures:
        showItems += x
        showItems += ", "
    print("You have the following artifacts: " + showItems + ".")  # fix formatting of last item


def lab():
    # all the things you do in your lab. this is going to be a big boy someday.
    print("You arrive at your lab.")
    # Rest

    # activate

    # link

    # final activation

    # Probably a help section here to. Should help sections be specific to the area they're in or a general help for
    # everything? I guess I could have a fancy help that does both.


def search(currentLocation, exploreAttempt):
    # Has you explore a location. Gives you loot or an encounter based off searching function.
    # also currently advances the day based on the exploreAttempt number.
    print("Day " + str(day))  # Just here for testing sanity
    print("explore attempt " + str(exploreAttempt))  # Ditto
    # see if its their first time exploring here
    if exploreAttempt == 0:
        print("You begin your search of " + currentLocation.name)
    else:
        print("You continue your search...")

    # search minigame!
    searchResult = searching()
    #  searchResult = 50  # just for debuggin'
    print("Your search result is " + str(searchResult) + ".")
    input("Press Enter to Continue.")

    # add something to use your dowsing rod here

    # component result
    if 11 < searchResult < 100:
        print("You find component " + currentLocation.component + ".")
        stores[currentLocation.component] = stores[currentLocation.component] + 1
        print("You now have " + str(stores[currentLocation.component]) + " " + currentLocation.component + ".")

    # Inactive Artifact result
    if 11 > searchResult > 1:
        print("You find an inactive " + currentLocation.artifact + ".")
        artifacts.append(currentLocation.artifact)

    # active artifact result
    if searchResult == 0:
        print("You find " + currentLocation.artifact + " already activated!")
        activated.append(currentLocation.artifact)
        print(activated)

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
    exploreAttempt = 0
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
        elif int(whereTo) > 0 and int(whereTo) < len(locations):  # go to the location

            currentLocation = locations[int(whereTo) - 1]

            # Add something to check if there's an event happening here
            while True:
                print("You arrive at " + currentLocation.name + ".")
                locationDesciption(currentLocation)
                print("Would you like to search or leave?")
                action = input().casefold()
                if action == "leave":
                    break
                if action == "search":
                    search(currentLocation, exploreAttempt)
                    # sees if the explore attempt advances the timeline.
                    if exploreAttempt in currentLocation.timeAdvances:
                        dayAdvance()
                        print("You're exploration took all day.")
                    exploreAttempt += 1
                    continueSearch = True

                    #  allows player to continue search, camp or exit
                    while continueSearch:
                        print("Day " + str(day))
                        print("Explore attempt " + str(exploreAttempt))
                        print("Would you like to search " + currentLocation.name + " again? Leave? Make camp? Info?")
                        action = input().casefold()
                        if action == "yes" or action == "y" or action == "search":
                            search(currentLocation, exploreAttempt)
                            if exploreAttempt in currentLocation.timeAdvances:
                                dayAdvance()
                                print("You're exploration took all day.")
                            exploreAttempt += 1
                            # player finds artifacts after 6 attempts
                            if exploreAttempt == 6 and currentLocation.artifact not in artifacts:
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
        print("What would you like to do? Explore? Check inventory? Go to the lab? Help?")
        action = input().casefold()

        if action == "explore":
            exitReason = explore()
        elif action == "check inventory" or action == "check" or action == "inventory":
            checkInventory()
        elif action == "go to the lab" or action == "lab" or exitReason == "lab":
            lab()
        elif action == "help":
            helper("main")
        else:
            print("command Not Recognized")


mainloop()

# things I'm concerned about:
# Changing the inventory inside these functions. Will they stick? I need to get my head around global variables.
# adding what the items do will be interesting. I guess a lot of if/ then stuff.
# make a function for advancing the timeline. checking against the event and skull days.
