from core.models import *
import pandasparser as parser
from django.core.exceptions import ObjectDoesNotExist

"""
energysource=enum(
    "Steinkohle",
    "Braunkohle",
    "Kraftstoff",
    "Motorbenzin",
    "Flugkraftstoff",
    "Diesel",
    "Fluessiggas",
    "Kraftstoffrest",
    "Biokraftstoff",
    "Oel",
    "Heizoel",
    "Schweroel",
    "Leichtoel",
    "Restoel",
    "Gas",
    "Naturgas",
    "Restgas",
    "Strom",
    "Fernwaerme",
    "Erneuerbare",
    "Sonstige"
)
"""



energysource_data=["Kohle","Steinkohle",
          "Braunkohle",
          "Kraftstoff","Motorbenzin","Flugkraftstoff","Diesel","Fluessiggas",["Kraftstoffrest"],
          "Biokraftstoff",
          "Oel","Heizoel","Schweroel","Leichtoel","Restoel",
          "Gas","Naturgas","Restgas",
          "Strom",
          "Fernwaerme",
          "Erneuerbare",
          "Sonstige"
          ]

application_data = ["Raumwaerme",
                    "Warmwasser",
                    "Sonstprozesswaerme",
                    "Klimakaelte",
                    "Sonstprozesskaelte",
                    "Mechenergie",
                    "IKT",
                    "Beleuchtung"
                    ]
year_data=list(range(1990,2021))

sector_data = ["Industrie",
               "Verkehr",
               "Haushalte",
               "Klimakaelte",
               "GHD",
               ]


def parseEnYear():
    for column in parser.dfColumnsEnYear:
        print(column)
        for row in parser.dfEnYear[column].keys():
            try:
                energy_source = EnergySource.objects.get(name=parser.row2EnergySource[row])
            except ObjectDoesNotExist:
                print("EnergySource: ",parser.row2EnergySource[row] ," does not exist.")
            try:
                year = Year.objects.get(year=column)
            except ObjectDoesNotExist:
                print("Year: ", year, " does not exist.")
            d, created = EnYear.objects.get_or_create(fk_energy_source=energy_source,
                                                      fk_year=year, petajoule=parser.dfEnYear[column][row])
            print("- Data: {0}, Created: {1}".format(str(d), str(created)))


def parseEnYearSect():
    for column in parser.dfColumnsYearSect:
        print(column)
        for row in parser.row2EnSect.keys():
            try:
                data=parser.row2EnSect[row][1]
                category="energy_source"
                energy_source_obj = EnergySource.objects.get(name=data)
                data=column
                category = "year"
                year_obj = Year.objects.get(year=column)
                data = parser.row2EnSect[row][0]
                category = "sector"
                sector_obj = Sector.objects.get(name=data)
                petajoule_obj=parser.dfEnYearSect[column][row]


                d, created = EnYearSect.objects.get_or_create(fk_energy_source=energy_source_obj,
                                                              fk_year=year_obj, fk_sector=sector_obj,
                                                              petajoule=petajoule_obj)
                print("- Data: {0}, Created: {1}".format(str(d), str(created)))

            except ObjectDoesNotExist:
                print(category,": ",data ," does not exist.")

def parseEnYearAppl():
    offset=1
    enApplList=["Oel","Gas","Strom","Fernwaerme","Kohle","Erneuerbare","Sonstige"]
    for column in parser.dfColumnsYearAppl:
        print(column)
        i = -1
        for application in  application_data:
            i+=1
            j = -1
            print(application)
            for energy_source in enApplList:
                j+=1
                print(energy_source)
                try:
                    data = energy_source
                    category = "energy_source"
                    energy_source_obj = EnergySource.objects.get(name=data)
                    data = column
                    category = "year"
                    year_obj = Year.objects.get(year=column)
                    data = application
                    category = "application"
                    application_obj = Application.objects.get(name=data)

                    index=offset+i*len(application_data)+j
                    print(index)
                    petajoule_obj = parser.dfEnYearAppl[column][index]

                    d, created = EnYearAppl.objects.get_or_create(fk_energy_source=energy_source_obj,
                                                                  fk_year=year_obj, fk_application=application_obj,
                                                                  petajoule=petajoule_obj)
                    print("- Data: {0}, Created: {1}".format(str(d), str(created)))

                except ObjectDoesNotExist:
                    print(category, ": ", data, " does not exist.")

def parseEnYearSectAppl():
    for column in parser.dfEnYearSectApplColumns:
        print(column)
        datadict=parser.row2SectApplEn
        for row in  datadict.keys():
            try:

                data = datadict[row][2]
                category = "energy_source"
                energy_source_obj = EnergySource.objects.get(name=data)

                data = column
                category = "year"
                year_obj = Year.objects.get(year=column)

                data = datadict[row][1]
                category = "application"
                application_obj = Application.objects.get(name=data)

                data = datadict[row][0]
                category = "sector"
                sector_obj = Sector.objects.get(name=data)



                petajoule_obj = parser.dfEnYearSectAppl[column][row]

                d, created = EnYearSectAppl.objects.get_or_create(fk_energy_source=energy_source_obj,
                                                              fk_year=year_obj, fk_application=application_obj,
                                                              fk_sector=sector_obj, petajoule=petajoule_obj)
                print("- Data: {0}, Created: {1}".format(str(d), str(created)))

            except ObjectDoesNotExist:
                print(category, ": ", data, " does not exist.")



def parseSample():
    for index, row in parser.dfSample.iterrows():
        try:
            d, created = Sample.objects.get_or_create(username=row["Username"],
                                                          identifier=row[" Identifier"], firstname=row["First name"],
                                                          lastname=row["Last name"])
            print("- Data: {0}, Created: {1}".format(str(d), str(created)))

        except ObjectDoesNotExist:
            print("error")

def parseSample2():
    for index, row in parser.dfSample2.iterrows():
        try:
            d, created = Sample2.objects.get_or_create(identifier=row["Identifier"], accessCode=row["Access code"],
                recCode = row["Recovery code"], firstname=row["First name"], lastname=row["Last name"],
                department = row["Department"], location = row["Location"])
            print("- Data: {0}, Created: {1}".format(str(d), str(created)))

        except ObjectDoesNotExist:
            print("error")


def populate():
    # data is a list of lists
    print("populating energysource")
    #print(Energysource.Strom)

    for row in energysource_data:
        d, created = EnergySource.objects.get_or_create(name=row)
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))


    for year in year_data:
        d, created = Year.objects.get_or_create(year=year)
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))



    for row in application_data:
        d, created = Application.objects.get_or_create(name=row)
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))




    for row in sector_data:
        d, created = Sector.objects.get_or_create(name=row)
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))



populate()



#parseEnYear()
#parseEnYearSect()
#parseEnYearAppl()
#parseEnYearSectAppl()
#parseSample()
parseSample2()

"""
if __name__ == "__main__":
    populate()
"""

