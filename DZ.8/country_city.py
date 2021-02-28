
def main():
    data = {
    "Ukraine": ["Kiev", "Kharkiv", "Odesa", "Dnipro"],
    "France": ["Paris", "Marseille", "Lyon", "Toulouse"],
    "Austria": ["Vienna", "Graz", "Linz", "Salzburg"],
    "Germany": ["Berlin", "Hamburg", "Munich", "Frankfurt"],
    }
    city = input("Введіть місто:")
    get_country(city,data)
    groupping_data(data)

def get_country(city,data):
    for i1 in data["Ukraine"]:
        if i1 == city:
            print("Ukraine")
            break
    for i2 in data["France"]:
        if i2 == city:
            print("France")
            break
    for i3 in data["Austria"]:
        if i3 == city:
            print("Austria")
            break
    for i4 in data["Germany"]:
        if i4 == city:
            print("Germany")
            break

def groupping_data(data):
    update_data = {}
    country = []
    capital = []
    cities = []
    for i in data.keys():
        country.append(i)
    for i in data.values():
        capital.append(i[0])
        i.pop(0)
        cities.append(i)
    update_data["country"] = country
    update_data["capital"] = capital
    update_data["cities"] = cities
    print(update_data)





main()