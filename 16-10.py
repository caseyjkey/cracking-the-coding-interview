from collections import defaultdict

# Given a list of peoples birth and death years (between 1900 and 2000)
# Calculate the year with the most people alive

peopleYears = [(1900, 2000), (1910, 1920), (1905, 1910), (1930, 1932)]

# For each pair, count how many other pairs are within its range, then find largest

def yearInRange(year, years):
    if year <= years[1] and year >= years[0]:
        return True
    return False


yearCounts = defaultdict(int)
for years in peopleYears:
    for year in range(years[0], years[1] + 1):
        for otherYears in peopleYears:
            yearCounts[year] += 1 if yearInRange(year, otherYears) else 0 

print("Year with most people alive:", max(yearCounts, key=yearCounts.get))
