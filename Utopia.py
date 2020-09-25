import random
#In general, UX is horrible. I'll go back and gussie her up once its functioning.


print ("Welcome to Utopia Engine")
day = 0 # make a day function, or a function that references this variable.
exploreAttempt = 0 #I'm absolutely sure I'm fucking up the scopes of these variables and functions.
health = 6
#sets inventory to be empty
toolbelt = ["Paralysis Wand", "Dowsing rod", "Focus Charm"]
stores = {"Silver": 0, "Quartz": 0, "Silica":0, "Gum" :0, "Wax": 0, "Lead" :0}
# old artifacts = {"Seal of Balance": 0, "Hermetic Mirror": 0, "Void Gate": 0, "Golden Chassis": 0, "Scrying Lens": 0, "Crystal Battery": 0}
artifacts = []
activated = []
#old treasures = {"Ice Plate": 0, "Bracelet of Ios": 0, "Shimmering Moonlace": 0, "Scale of the Infinity Wurm": 0, "The Ancient Record": 0, "The Molten Shard": 0}
treasures = []
#DAYS, BABY
eventDays = [2, 5, 8, 11, 14, 17, 20]
skullDays = [15, 16, 17, 18, 19, 20, 21, 22]

#Set locations and their loot. I made it so you could easily add more, for some reason.
class location:
    def __init__(self, number, name, component, artifact, treasure, daysSearched, timeAdvances):
        self.number = number
        self.name = name
        self.component = component
        self.artifact = artifact
        self.treasure = treasure
        self.daysSearched = daysSearched
        self.timeAdvances = timeAdvances
        #should I add en encounter property or even a function here? with the monster list specific to the area. Ugh, spirits are ganna fuck this up.
        #Good lord, should I make a monster class? that sounds miserable.

halbeardPeak = location(1, "Halbeard Peak", "Silver", "Seal of Balance", "Ice Plate", 0, [0, 1, 3])
theGreatWilds = location(2, "The Great Wilds", "Quartz", "Hermetic Mirror", "Bracelet of Ios", 0, [0,3])
rootStrangledMarshes = location(3, "Root-Strangled Marshes", "Gum", "Void Gate", "Shimmering Moonlace", 0, [0,2,4])
glassrockCanyon = location(4, "Glassrock Canyon", "Silica", "Golden Chassis", "Scale of the Infinity Wurm", 0, [0,1,3])
ruinedCityOfTheAncients = location(5, "Ruined City of the Ancients", "Wax", "Scrying Lens", "The Ancient Record", 0, [0,2,4])
theFieryMaw = location(6, "The Fiery Maw", "Lead", "Crystal Battery", "The Molten Shard", 0, [0,1,2,4])

locations = [halbeardPeak,
            theGreatWilds,
            rootStrangledMarshes,
            glassrockCanyon,
            ruinedCityOfTheAncients,
            theFieryMaw]


def helper(gamePlace):
    #gives general help based off what menu they came here from.
    print ("You were in the " + str(gamePlace) + " menu.")
    print ("You are beyond help.")

def encounter(currentLocation):
    print ("You have encounted a monster from

def searching():
    #the self contained search minigame. just spits out a number. no day advances or nothin'
    searchTable = ["A","B","C","D","E","F"]
    for x in range(3):
        print ("We gonna roll some dice now, son. Check this shit out:")
        #Display an amazing acii table.
        print ("-------")
        print ("|" + str(searchTable[0]) + "|" + str(searchTable[1]) + "|" + str(searchTable[2]) + "|")
        print ("-------")
        print ("|" + str(searchTable[3]) + "|" + str(searchTable[4]) + "|" + str(searchTable[5]) + "|")
        print ("-------")
        rolls = [random.randint(1,6),random.randint(1,6)]
        print ("You've rolled "+ str(rolls[0]) + " and " + str(rolls[1]) + ".")
        #place Rolls
        print ("Where would you like your roll of "+ str(rolls[0]) + " to be placed?")
        rollPlacement = input().upper()
        if rollPlacement in searchTable:
            tablePlace = -1
            for x in searchTable:
                tablePlace += 1
                if x == rollPlacement:
                    print ("it was " + str(searchTable[tablePlace]))
                    searchTable[tablePlace] = rolls[0]
                    print ("Now It's " + str(searchTable[tablePlace]))

        #I'm of two minds about showing the whole table again here.

        print ("Where would you like your roll of "+ str(rolls[1]) + " to be placed?")
        rollPlacement = input().upper()
        if rollPlacement in searchTable:
            tablePlace = -1
            for x in searchTable:
                tablePlace += 1
                if x == rollPlacement:
                    print ("it was " + str(searchTable[tablePlace]))
                    searchTable[tablePlace] = rolls[1]
                    print ("Now It's " + str(searchTable[tablePlace]))

        #Figure out a way to address the imput not being a number, or already used. Maybe a try? make the input into a function?


    topNumber = int(str(searchTable[0]) + str(searchTable[1]) + str(searchTable[2]))
    print ("Your top number is " + str(topNumber) + ".")
    bottomNumber = int(str(searchTable[3]) + str(searchTable[4]) + str(searchTable[5]))
    print ("Your bottom number is " + str(bottomNumber) + ".")
    searchResult = topNumber - bottomNumber
    # make this prettier!
    return searchResult


def checkInventory():
    #prints your inventory.
    print ("You open your bag and see...")
    #List Components
    for x, y in stores.items():
        print(x, y)
    #List Artifacts

    #list activated artifacts

    #List Treasures

    mainloop()

def lab():
    #all the things you do in your lab. this is going to be a big boy someday.
    print("You arrive at your lab.")
    #Rest

    #activate

    #link

    #final activation

    #Probably a help secion here to. Should help sections be specific to the area they're in or a general help for everything? I guess I could have a fancy help that does both.

def search(currentLocation):
    #Has you explore a location. Gives you loot or an encounter based off searching function.
    #also currently advances the day based on the exploreattempt number.
    global day
    global exploreAttempt
    print ("Day " + str(day))
    print ("explore attempt " + str(exploreAttempt))
    #see if its their first time exploring here
    if exploreAttempt == 0:
        print ("You begin your search of " + currentLocation.name)
    else:
        print ("You continue your search...")

    #search minigame!
    searchResult = searching()
    #searchResult = 0 #just for debuggin'
    print ("Your search result is "+ str(searchResult) +".")

    #add something to use your dowsing rod here

    #component result
    if searchResult > 11 and searchResult < 100:
        print("You find component " + currentLocation.component + ".")
        print (str(stores[currentLocation.component]))
        stores[currentLocation.component] = stores[currentLocation.component] +1
        print (str(stores[currentLocation.component]))

    #Inactive Artifact result
    if searchResult < 11 and searchResult > 1:
        print ("You find an inactive " + currentLocation.artifact + ".")

    #active artifact result
    if searchResult == 0:
        print ("You find " + currentLocation.artifact + " already activated!")
        activated.append(currentLocation.artifact)
        print (activated)

    #Monster!
    if searchResult < 0 or searchResult >99:
        print ("You encounter a monster!")
        #encounter(currentLocation) #I should probably make this.

    #sees if the explore attempt advances the timeline.
    if exploreAttempt in currentLocation.timeAdvances:
        day += 1
        print ("You're exploration took all day.")
        exploreAttempt += 1

    print (currentLocation.timeAdvances)
    print ("Day " + str(day))
    print ("Explore attempt " + str(exploreAttempt))

    #from here, they can explore this location again or leave it. Leave it kicks them back to the main loop.
    #Staying would explore again, going through this all again, advancing the exploreAttemps and maybe the days.
    #the above functionality is in the explore function for now. probalby forever.




def explore():
    #player decides where they want to explore. gives info on location.
    print ("Where would you like to explore?")
    for x in locations:
        print (str(x.number) + ". " + x.name)
    print (str(len(locations)+1) + ". Nevermind, Back to the lab")
    whereTo = input("Where to? ")

    if int(whereTo) == 1+len(locations):
        lab() #I feel like this is dumb. Am I going to get into nested function hell?

    elif int(whereTo) > 0 and int(whereTo) < len(locations):

        currentLocation = locations[int(whereTo)-1]

        #Add something to check if there's an event happening here

        print ("You arrive at " +currentLocation.name + ".")
        print ("Here you will find " + currentLocation.component + ".")
        if currentLocation.artifact in artifacts:
            print ("Here you found " + currentLocation.artifact + ".")
        else:
            print ("Hidden somewhere is the " + currentLocation.artifact + ".")
        if currentLocation.treasure in treasures:
            print ("Here you found " + currentLocation.treasure + ".")
        else:
            print ("It's said a powerful monster carries " + currentLocation.treasure + " here.")
        print ("Searching here would advance the day following these attempts: " + str(currentLocation.timeAdvances)) #make this pretty.
        print ("Would you like to search or leave?")
        action = input().casefold()
        if action == "leave":
            mainloop() #I feel like this is dumb. Am I going to get into nested function hell?
        if action == "search":
            search(currentLocation)

            #see if they want to continure or move along. THis needs touching up for work infinitely AND check if you've had 6 conecutive attempts.
            #I remember when I learned basic/ programed on my ti83 calculator, there was the "goto" function. I miss that sometimes.
            #I'm sure a while or for loop is what I need, but I'm too hungry to think about it right now.
            print ("Would you like to search " +currentLocation.name + " again? Y or N")
            action = input().casefold()
            if action == "y":
                search(currentLocation)
            else:
                exploreAttemps = 0
                mainloop() #I feel like this is dumb. Am I going to get into nested function hell?


        else:
            explore() #I feel like this is dumb. Am I going to get into nested function hell?
    else:
        print ("Please enter a location number")
        explore() #I feel like this is dumb. Am I going to get into nested function hell?


    #does anyone else use comments to just sorta muse?


def mainloop():
    #player where/ what to do.
    print ("The end is coming unless you can build the Utopia Engine to stop it.")
    print ("It is day " + str(day) +" of your adventure.")
    print ("What would you like to do? Explore? Check inventory? Go to the lab? Help?")
    action = input().casefold()

    if action == "explore":
        explore()

    elif action == "check inventory" or action == "check" or action == "inventory":
        checkInventory()
        mainloop() #I feel like this is dumb. Am I going to get into nested function hell?

    elif action == "go to the lab" or action == "lab":
            lab()

    elif action == "help":
        helper("main")
    else:
        print ("command Not Recognized")
        mainloop() #I feel like this is dumb. Am I going to get into nested function hell?

mainloop()

#things I'm concerned about:
#functions in functions in functions...
#Changing the inventory inside these functions. Will they stick? I need to get my head around global variables.
#adding what the items do will be interesting. I guess a lot of if/ then stuff.
#make a function for advancing the timeline. checking against the event and skull days.
