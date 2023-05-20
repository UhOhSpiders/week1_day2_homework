united_kingdom = [
  {
    "name": "Scotland",
    "population": 2,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 10,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 20,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["capital"] = "Cardiff"

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append(
    {
    "name": "Northern Ireland",
    "population": 8,
    "capital": "Belfast"
  }
)
# print(united_kingdom)
# 3. Use a loop to print the names of all the countries in the UK.
for country in united_kingdom:
  print(country["name"])
# 4. Use a loop to find the total population of the UK.
total_pop = 0
for country in united_kingdom:
  total_pop += country["population"]
print(total_pop)
