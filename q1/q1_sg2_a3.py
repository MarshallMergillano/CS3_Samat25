def chinese_zodiac(birth_year):
  birth_year = int(input("Enter your birth year: "))
  if birth_year >= 1900:
    zodiacs = [ "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    year = (birth_year - 1900) % 12
    return zodiacs[year]

  else: 
    return("Invalid Year, it should not be earlier than 1900. Please input a valid year.")
result = chinese_zodiac(birth_year)
print(result)
