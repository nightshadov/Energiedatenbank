from core.models import *

export DJANGO_SETTINGS_MODULE=evtvisu.settings



def populate():
    # data is a list of lists
    data=[["Steinkohle"],["Braunkohle"],["Kraftstoff"]]
    for row in data:
        data1 = row[0]
        d, created = EnergySource.objects.get_or_create(name=data1)
        print("- Data: {0}, Created: {1}".format(str(d), str(created)))


if __name__ == "__main__":
    populate()