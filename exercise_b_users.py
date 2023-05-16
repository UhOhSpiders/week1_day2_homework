users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}
#1
jonathans_twitter_handle = users["Jonathan"]["twitter"]
print(jonathans_twitter_handle)

#2
eriks_home_town = users["Erik"]["home_town"]
print(eriks_home_town)

#3
eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
print(eriks_lottery_numbers)

#4
avrils_pet_species = users["Avril"]["pets"][0]["species"]
print(avrils_pet_species)

#5
eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
print(min(eriks_lottery_numbers))

#6
avrils_lottery_numbers = users["Avril"]["lottery_numbers"]
evensList = [x for x in avrils_lottery_numbers if x % 2 == 0]
print(evensList)

#7
eriks_lottery_numbers = users["Erik"]["lottery_numbers"]
eriks_lottery_numbers.append(7)
print(eriks_lottery_numbers)

#8
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])





# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary
