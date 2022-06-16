from core.models import *



def populate():
    # data is a list of lists
    print("populating energysource")
    energysource_data=[["Steinkohle"],
          ["Braunkohle"],
          ["Kraftstoff"],["Motorbenzin"],["Flug"],["Diesel"],["Fluessiggas"],["Kraftstoffrest"],
          ["Biokraftstoff"],
          ["Oel"],["Heiz"],["Schwer"],["Leicht"],["Rest"],
          ["Gas"],["Natur"],["Restgas"],
          ["Strom"],
          ["Fernwaerme"],
          ["Erneuerbare"],
          ["Sonstige"]
          ]
    for row in energysource_data:
        d, created = EnergySource.objects.get_or_create(name=row[0])
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))

    year_data=[]
    for i in range(1990,2021):
        year_data.append([i])
    for row in year_data:
        d, created = Year.objects.get_or_create(year_id=row[0])
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))

    application_data=[["Raumwaerme"],
                 ["Warmwasser"],
                 ["Sonstprozesswaerme"],
                 ["Klimakaelte"],
                 ["Sonstprozesskaelte"],
                 ["Mechenergie"],
                 ["IKT"],
                 ["Beleuchtung"]
                 ]

    for row in application_data:
        d, created = Application.objects.get_or_create(name=row[0])
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))


    sector_data=[["Industrie"],
                 ["Verkehr"],
                 ["Haushalte"],
                 ["Klimakaelte"],
                 ["GHD"],
                 ]

    for row in application_data:
        d, created = Sector.objects.get_or_create(name=row[0])
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))


populate()

"""
if __name__ == "__main__":
    populate()
"""

