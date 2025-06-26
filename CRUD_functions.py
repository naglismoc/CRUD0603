def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")


def load_default_data():
    return [
            {
                'id': 1,
                "country":"Lithuania",
                "city":"Palanga",
                "price":20,
                "accomodation":"hotel"
            },
            {
                'id': 2,
                "country":"Turkija",
                "city":"Alanya",
                "price":60,
                "accomodation":"hostel"
            },
            {
                'id': 3,
                "country":"Cyprus",
                "city":"Larnaka",
                "price":70,
                "accomodation":"apartaments"
            }
        ]


def print_hollidays(hollidays):
    for hol in hollidays:
        print(f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} "
              f"parai {hol['price']}")
    print("--------------------------------------------------------------------------")

def create_hollidays(id_counter):
    print("atostogų pridėjimas:")
    print("Įveskite šalį")
    country = input()
    print("Įveskite miestą")
    city = input()
    print("Įveskite apgyvendinimo tipą")
    apt = input()
    print("Įveskite kainą")
    price = input()
    return   {
                    'id': id_counter,
                    "country":country,
                    "city":city,
                    "price":price,
                    "accomodation":apt
                }

def edit_hollidays(hollidays):
    print("atostogų redagavimas. Pasirinkite ID įrašo kurį norite redaguoti.")
    id = input()
    for hol in hollidays:
        if id == str(hol['id']):
            print(f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} "
                  f"parai {hol['price']}")

            print("Įveskite šalį")
            hol['country'] = input()
            print("Įveskite miestą")
            hol['city'] = input()
            print("Įveskite apgyvendinimo tipą")
            hol['accomodation'] = input()
            print("Įveskite kainą")
            hol['price'] = input()
            break

def delete_hollidays(hollidays):
    print("atostogų šalinimas. Pasirinkite ID įrašo kurį norite redaguoti.")
    id = input() #3
    for hol in hollidays: # 0, 1, 2
        if id == str(hol['id']): #1 2 3
            print(
                f"{hol['id']}. Šalinama: Atostogos {hol['country']} {hol['city']}. Kaina gyvenant"
                f" {hol['accomodation']} "
                f"parai {hol['price']}")
            hol_pos_in_list = hollidays.index(hol)
            del hollidays[hol_pos_in_list]
