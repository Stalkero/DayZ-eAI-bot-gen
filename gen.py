import random
import math


def is_within_radius(startLoc, endLoc):
    dx = startLoc[0] - endLoc[0]
    dy = startLoc[1] - endLoc[1]
    dz = startLoc[2] - endLoc[2]
    distance = math.sqrt(dx*dx + dy*dy + dz*dz)
    if distance <= 4000:
        return True
    return False






# Lista miast, wiosek, baz, lasów, gór i ulic w Chernarusplus
locations = [
    (-7340.0, 9.0, -6950.0),  # Elektrozavodsk
    (-11900.0, 15.0, -12100.0),  # Berezino
    (6200.0, 69.0, 7800.0),  # Zelenogorsk
    (-6500.0, 8.0, -12150.0),  # Chernogorsk
    (12900.0, 35.0, -12900.0),  # Novodmitrovsk
    (-3200.0, 2.0, 11600.0),  # Severograd
    (-10700.0, 5.0, 4100.0),  # Svetlojarsk
    (12700.0, 73.0, 800.0),  # Kamyshovo
    (-4400.0, 9.0, -3300.0),  # Krasnostav
    (-12700.0, 5.0, -13800.0),  # Nadezhdino
    (9700.0, 35.0, -4800.0),  # Dubky
    (-7700.0, 5.0, 2600.0),  # Dolina
    (12700.0, 83.0, 5400.0),  # Nizhnoye
    (-10900.0, 9.0, -3500.0),  # Lopatino
    (-14200.0, 5.0, 12500.0),  # Balota
    (2500.0, 31.0, -12000.0),  # Krasnoe
    (-200.0, 2.0, -4700.0),  # Vyshnoye
    (7200.0, 5.0, -11300.0),  # Pusta
    (-15300.0, 4.0, 200.0),  # Kamenka
    (2700.0, 8.0, 11100.0),  # Sosnovka
    (8700.0, 25.0, -12300.0),  # Gorka
    (-4800.0, 2.0, -4700.0),  # Staroye
    (-12600.0, 5.0, -3100.0),  # Solnichniy
    (14300.0, 22.0, 14300.0),  # Komarovo
    (-4800.0, 245.0, -5300.0),  # NW Airfield
    (10600.0, 260.0, -5800.0),  # NE Airfield
    (5400.0, 7.0, -13800.0),  # Balota Airfield
    (12600.0, 520.0, -300.0),  # Tisy Military Base
    (-9300.0, 290.0, -7400.0),  # Myshkino Military Base
    (3700.0, 290.0, 100.0),  # Pavlovo Military Base
    (-3600.0, 440.0, -8600.0), # Devils Castle
    (10100.0, 1200.0, -4400.0), # Zub Castle
    (-9700.0, 60.0, 9100.0), # Black Forest
    (12900.0, 60.0, -9200.0), # Green Forest
    (-12000.0, 60.0, 13200.0), # Great Forest
    (-14100.0, 60.0, -8300.0), # Northern Forest
    (12200.0, 60.0, 11200.0), # Central Forest
    (-14500.0, 60.0, 1400.0), # Western Forest
    (-13900.0, 60.0, -14000.0), # Eastern Forest
    (13000.0, 5.0, -3300.0), # Rzeka Kamenka
    (-11400.0, 5.0, 2800.0), # Rzeka Czarny Przylądek
    (-8400.0, 5.0, -8300.0), # Rzeka Pusta
    (14800.0, 5.0, 600.0), # Rzeka Polesny Potok
    (12200.0, 5.0, -12300.0), # Rzeka Guba
    (-10600.0, 5.0, -12300.0), # Rzeka Biała
    (-12000.0, 5.0, 12900.0), # Rzeka Zbiorn
]




minX,maxX = 0, 15000
minY,maxY = 0,1200
minZ,maxZ = 0, 15000

locToGen = 100
pointsToGen = 20 
generatedPoints = 0
patrolID = 11

generated_locations = set()

while patrolID != 20:

    print("ref array<vector> patrol_" + str(patrolID) + " = ")
    print("{")

    while generatedPoints < pointsToGen:
        randomLoc = (random.randrange(minX, maxX), random.randrange(minY, maxY), random.randrange(minZ, maxZ))
        
        for loc in locations:
            if is_within_radius(randomLoc,loc) and randomLoc not in generated_locations and randomLoc[2] == loc[2] and randomLoc[0] not in range(18500,25000) and randomLoc[2] not in range(13000,15000) and randomLoc[0] not in range(14700,16500) and randomLoc[2] not in range(19500,25000) and randomLoc[0] not in range(2300,5500) and randomLoc[2] not in range(13500,16000) and randomLoc[0] not in range(3000,11000) and randomLoc[2] not in range(1000,4000):
                if generatedPoints == pointsToGen - 1:
                    print("\t\" " + str(loc[0]) + " " + str(loc[1]) +  " " + str(loc[2]) + "\"")
                    generated_locations.add(randomLoc)
                    generatedPoints += 1
                    break
                else:
                    print("\t\" " + str(loc[0]) + " " + str(loc[1]) +  " " + str(loc[2]) + "\",")
                    generated_locations.add(randomLoc)
                    generatedPoints += 1
                    break

    patrolID += 1
    generatedPoints = 0
    generated_locations.clear()  # czyszczenie zbioru dla wygenerowanych koordynatów przed następnym patrol
    print("};\n")


    
















#Przechodzenie przez wszystkie lokalizacje
#for loc in locations:
#	# Jeśli lokalizacja to rzeka
#	if loc in [(13000.0, -3300.0, 5.0), (-11400.0, 2800.0, 5.0), (-8400.0, -8300.0, 5.0), (14800.0, 600.0, 5.0), (12200.0, -12300.0, 5.0), (-10600.0, -12300.0, 5.0), (-12000.0, 12900.0, 5.0)]:
#		rivers.append(loc)
#
#	# Jeśli lokalizacja to las
#	elif loc in [(-9700.0, 9100.0, 60.0), (12900.0, -9200.0, 60.0), (-12000.0, 13200.0, 60.0), (-14100.0, -8300.0, 60.0), (12200.0, 11200.0, 60.0), (-14500.0, 1400.0, 60.0), (-13900.0, -14000.0, 60.0)]:
#		forests.append(loc)
#	# W przeciwnym przypadku, lokalizacja to miasto lub baza
#	else:
#		cities.append(loc)



#if randomLoc in [(13000.0, -3300.0, 5.0), (-11400.0, 2800.0, 5.0), (-8400.0, -8300.0, 5.0), (14800.0, 600.0, 5.0), (12200.0, -12300.0, 5.0), (-10600.0, -12300.0, 5.0), (-12000.0, 12900.0, 5.0)]:
#	rivers.append(randomLoc)

# Jeśli lokalizacja to las
#elif randomLoc in [(-9700.0, 9100.0, 60.0), (12900.0, -9200.0, 60.0), (-12000.0, 13200.0, 60.0), (-14100.0, -8300.0, 60.0), (12200.0, 11200.0, 60.0), (-14500.0, 1400.0, 60.0), (-13900.0, -14000.0, 60.0)]:
#		forests.append(randomLoc)

# W przeciwnym przypadku, lokalizacja to miasto lub baza
#else:
#	cities.append(randomLoc)

# Wypisanie listy lokalizacji








#for patrolRange in range(11,16):
#
#
#	
#	print("ref array<vector>" +  " patrol_" +  str(patrolRange) + " = \n{ ")
#
#	for loc in rivers:
#		print("\t\"" + str(loc[0])  + " , " +  str(loc[1]) + " , " + str(loc[2]) + "\"," )
#	for loc in forests:
#		print("\t\"" + str(loc[0])  + " , " +  str(loc[1]) + " , " + str(loc[2]) + "\"," )
#
#	citiesLen = cities[-1]
#	for  loc in cities:
#		if loc == citiesLen:
#			print("\t\"" + str(loc[0])  + " , " +  str(loc[1]) + " , " + str(loc[2]) + "\"" )
#		else:
#			print("\t\"" + str(loc[0])  + " , " +  str(loc[1]) + " , " + str(loc[2]) + "\"," )
#
#	print("};")
