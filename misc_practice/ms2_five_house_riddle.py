import copy

# The Brit lives in the red house
# The Swede keeps dogs as pets
# The Dane drinks tea
# The green house is on the left of the white house
# The person who smokes Pall Malls rears birds
# The owner of the yellow house smokes Dunhill
# The green house’s owner drinks coffee
# The man living in the center house drinks milk
# The Norwegian lives in the first (leftmost) house
# The man who smokes Blends lives next to the one who keeps cats
# The man who keeps horses lives next to the man who smokes Dunhill
# The owner who smokes BlueMaster drinks beer
# The German smokes Princes
# The Norwegian lives next to the blue house
# -----
# The man who smokes Blends has a neighbor who drinks water

options = {
    "owner": [ "brit", "dane", "german", "norwegian", "swede" ],
    "position": [ 0, 1, 2, 3, 4 ], # 0 = far left, 4 = far right
    "color": [ "blue", "green", "red", "white", "yellow" ],
    "beverage": [ "beer", "coffee", "tea", "milk", "water" ],
    "cigar": [ "blend", "bluemaster", "dunhill", "pallmall", "prince" ],
    "pet": [ "birds", "cats", "dogs", "fish", "horses" ],
}

# encode the conditions from the above riddle in whatever format you prefer
conditions = [
    ("equal", "owner", "brit", "color", "red"),
    ("equal", "owner", "swede", "pet", "dogs"),
    ("equal", "owner", "dane", "beverage", "tea"),
    ("left", "color", "green", "color", "white"),
    ("equal", "cigar", "pallmall", "pet", "birds"),
    ("equal", "color", "yellow", "cigar", "dunhill"),
    ("equal", "color", "green", "beverage", "coffee"),
    ("position", "beverage", "milk", "position", 2),
    ("position", "owner", "norwegian", "position", 0),
    ("adjacent", "cigar", "blend", "pet", "cats"),
    ("adjacent", "pet", "horses", "cigar", "dunhill"),
    ("equal", "cigar", "bluemaster", "beverage", "beer"),
    ("equal", "owner", "german", "cigar", "prince"),
    ("adjacent", "owner", "norwegian", "color", "blue"),
    ("adjacent", "cigar", "blend", "beverage", "water")
]

# return the nationality of the owner who has the fish as a string
def whoOwnsTheFish( options, conditions ):
    # discard position array from options
    # instead use array indices in our solution map to represent house position
    options.pop("position")
    solution_map = [{} for n in range(5)]
    answer = generatePermutations(solution_map, options, conditions)
    return answer if answer else "No Solution"

# recursive function to test all permutation branches until we find our solution
def generatePermutations(solution_map, options, conditions, next_options=[], next_category=""):
    # generate hash-table to lookup house number by category in O(1) time
    lookup_house_number = generateLookupTable(solution_map)
    # at the beginning of every permutation recurse, check if conditions still pass
    # if not exit and stop evaluating this branch
    if not testConditions(lookup_house_number, conditions):
        return ""

    if not options and not next_options:
        house_number = lookup_house_number["pet"]["fish"]
        return solution_map[house_number]["owner"]
    
    if not next_options:
        next_category = list(options.keys())[0]
        options = copy.deepcopy(options)
        next_options = options.pop(next_category)

    next_house_number = len(next_options) - 1
    for i in range(len(next_options)):
        solution_map = copy.deepcopy(solution_map)
        solution_map[next_house_number][next_category] = next_options[i]
        next_permutation = generatePermutations(solution_map, options, conditions, next_options[:i] + next_options[i+1:], next_category)
        if next_permutation:
            return next_permutation
    
    return ""

##----------------------- Assertion Tests ---------------------------##
# check that the condition A and B have same house number
# if condition A or B have not been assigned yet, skip test
def assertEqual(lookup_house_number, category_a, value_a, category_b, value_b):
    if value_a not in lookup_house_number[category_a] or value_b not in lookup_house_number[category_b]:
        return True
    return lookup_house_number[category_a][value_a] == lookup_house_number[category_b][value_b]

# check that condition A is left of condition B
def assertLeft(lookup_house_number, category_a, value_a, category_b, value_b):
    if value_a not in lookup_house_number[category_a] or value_b not in lookup_house_number[category_b]:
        return True
    return lookup_house_number[category_a][value_a] == lookup_house_number[category_b][value_b] - 1

# check that condition A is right of condition B
def assertRight(lookup_house_number, category_a, value_a, category_b, value_b):
    if value_a not in lookup_house_number[category_a] or value_b not in lookup_house_number[category_b]:
        return True
    return lookup_house_number[category_a][value_a] == lookup_house_number[category_b][value_b] + 1

# check that condition A has given house number
def assertPosition(lookup_house_number, category_a, value_a, position):
    if value_a not in lookup_house_number[category_a]:
        return True
    return lookup_house_number[category_a][value_a] == position

# check that Condition A is left or right of condition B
def assertAdjacent(lookup_house_number, category_a, value_a, category_b, value_b):
    if value_a not in lookup_house_number[category_a] or value_b not in lookup_house_number[category_b]:
        return True
    isLeft = assertLeft(lookup_house_number, category_a, value_a, category_b, value_b)
    isRight = assertRight(lookup_house_number, category_a, value_a, category_b, value_b)
    return isLeft or isRight

# test all conditions, if any fail, return False
def testConditions(lookup_house_number, conditions):
    for condition in conditions:
        assertionType = condition[0]
        category_a, value_a = condition[1], condition[2]
        category_b, value_b = condition[3], condition[4]

        match assertionType:
            case "equal":
                if not assertEqual(lookup_house_number, category_a, value_a, category_b, value_b):
                    return False
            case "position":
                if not assertPosition(lookup_house_number, category_a, value_a, value_b):
                    return False
            case "left":
                if not assertLeft(lookup_house_number, category_a, value_a, category_b, value_b):
                    return False
            case "right":
                if not assertRight(lookup_house_number, category_a, value_a, category_b, value_b):
                    return False
            case "adjacent":
                if not assertAdjacent(lookup_house_number, category_a, value_a, category_b, value_b):
                    return False
    return True

# convert solution map into a hash-table
def generateLookupTable(solution_map):
    lookup_house_number = {
        "owner": {},
        "color": {},
        "beverage": {},
        "cigar": {},
        "pet": {},
    }

    for i in range(len(solution_map)):
        next_house = solution_map[i]
        for category, value in next_house.items():
            lookup_house_number[category][value] = i

    return lookup_house_number

correct_solution = [
    {"owner": "norwegian", "color": "yellow", "cigar": "dunhill", "pet": "cats", "beverage": "water"},
    {"owner": "dane", "color": "blue", "cigar": "blend", "pet": "horses", "beverage": "tea"},
    {"owner": "brit", "color": "red", "cigar": "pallmall", "pet": "birds", "beverage": "milk"},
    {"owner": "german", "color": "green", "cigar": "prince", "pet": "fish", "beverage": "coffee"},
    {"owner": "swede", "color": "white", "cigar": "bluemaster", "pet": "dogs", "beverage": "beer"},
]

correct_lookup = generateLookupTable(correct_solution)

# print(testConditions(correct_lookup, conditions))

print(whoOwnsTheFish(options, conditions))