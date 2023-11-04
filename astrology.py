year = int(input("Enter your year of birth "))
rat = [1912, 1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
ox = [1913, 1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021]
tiger = [1914, 1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022]
rabbit = [1915, 1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]
dragon = [1916, 1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024]
snake = [1917, 1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013]
horse = [1918, 1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014]
goat = [1919, 1931, 1943, 1955, 1967, 1979, 1991, 2003, 2016]
monkey = [1920, 1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016]
rooster = [1921, 1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017]
dog = [1922, 1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018]
pig = [1923, 1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019]

if year in rat:
    print("The rat is a charmer and not slow to make the most of any favorable opportunity. Rats do well in real estate, public relations, and advertising. Rats are sociable, dealing easily with people from all backgrounds, and they certainly enjoy the good life. They have sharp wits and even sharper tongues. The Rat’s element is water and the color black.")
elif year in ox:
    print("The strong, conservative Ox is born to lead. Oxen don’t suffer fools gladly, are slow to change their opinions and do well in military careers or other careers where leadership is required. The Ox is loyal and patient and sooner or later, will make his or her mark in life. The Ox’s element is earth, the color is golden yellow.")
elif year in tiger:
    print("The tiger is a courageous and noble soul, but also highly sensitive and quick to take offence. Tigers are likely to leap in where less hot-headed animals would fear to tread, and they can be very hard to control. They need a career where they can be boss, or strike out on their own with no one to give them orders. The tiger’s element is wood, and the color green.")   
elif year in rabbit:
    print("The elegant, peace-loving rabbit is the soul of tact and would never dream of deliberately hurting anyone. The rabbit would prefer a simple white lie to an outright truth which could ruin a moment or damage a friendship. Rabbits are considered very lucky and do well in careers that bring out their people skills, such as law, acting, or diplomacy. The Rabbit’s element is Wood, and the color green.")  
elif year in dragon:
    print("The talented, artistic Dragons are the real show-offs of the Chinese Zodiac. They are always popular and they easily influence those around them. Dragons are determined, successful, and enthusiastic. Dragons usually find successful careers in the performing or creative arts, or in politics. Their element is earth, their color gold.")  
elif year in snake:
    print("Snakes are the most enticing creatures in the Chinese Zodiac — they have much in common with the sign of Scorpio in western astrology. Snakes are alluring and highly intelligent, and are often found in academic or scientific careers. But their great physical attraction also makes them renowned actors and entertainers. The Snake’s element is fire, the color is red.t")     
elif year in horse:
    print("The hard working, confident horse puts its shoulder to even the most difficult task without complaint. Horses are justifiably proud of their elegance and strength, and while they may tend to parade their egos, they also love company and make stimulating friends. The horse does well in sports, the military and politics. The element of the horse is fire, the color red.") 
elif year in goat:
    print("The goat is very agile and loves to climb, but tends to worry a lot. They can be charming company, but at other times they will tend to bring their friends down by complaining and imagining the worst. Goats can find success in the caring professions, where they can worry for profit, or avoid the ulcers altogether by dropping out. The goat’s element is earth, the color yellow.")     
elif year in monkey:
    print("The clever, witty monkey is never short of friends. Always the life of the party, the monkey has a paw on the pulse of life and senses trends long before anyone else. So they find success in the media, advertising, and design. The monkey can also be very tricky and needs to guard against a tendency to take advantage of slower types. The Monkey’s element is metal, and the color white.")    
elif year in rooster:
    print(" No one crows louder than the proud rooster, but few have more to crow about. The rooster is a shrewd, sharp, confident operator, who dreams big and looks to the stars. Roosters strut proudly and so choose careers where they can show off and reach impossible goals, such as the entertainment industry, or a business idea that breaks barriers and travels world wide. The element of the rooster is metal, and the color is white.")
elif year in dog:
    print("The faithful dog will always be there for family and friends. The dog takes setbacks philosophically, and find comfort in familiar, homely things. But there is a streak of adventure in the dog’s soul that will see them running with the wind on occasion. The dog will also attack when it feels a loved one is threatened, so remember the wise advice and let sleeping dogs lie. Dogs do well in professions based on caring for others, such as teaching and nursing. The dog’s element is earth, the color is yellowt")
elif year in pig:
    print("The honorable and scrupulous pig is one of the easiest signs of the Chinese Zodiac to get along with. But they are easily shocked, and also easily gulled into schemes cooked by some of the less scrupulous signs. The Pig has a creative side which should be nurtured, and will often find fulfillment, if not success, in the arts. The element of the pig is water, the color black")          
elif year < 1912:
    print("There is no way you are that old...c'mon bruh")
elif year > 2004:
    print("You must be from the future")    
else:
    print("chill bruh")    