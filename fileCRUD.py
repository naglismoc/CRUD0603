import csv

headers = ['id', 'country', 'city', 'price', 'accomodation']
def load_holidays():
    with open('lithuania_accommodation.csv', mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))
def save_holidays(holidays):
    with open('lithuania_accommodation.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(holidays)

def create_holiday(holidays):
    print("atostogų pridėjimas:")
    print("Įveskite šalį")
    country = input()
    print("Įveskite miestą")
    city = input()
    print("Įveskite apgyvendinimo tipą")
    apt = input()
    print("Įveskite kainą")
    price = input()
    new_id = str(int(holidays[-1]['id']) + 1) if len(holidays) > 0 else 1
    holidays.append(  {
                    'id': new_id,
                    "country":country,
                    "city":city,
                    "price":price,
                    "accomodation":apt
                })
    save_holidays(holidays)

def edit_holiday(holidays):
    print("atostogų redagavimas. Pasirinkite ID įrašo kurį norite redaguoti.")
    id = input()
    for hol in holidays:
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
    save_holidays(holidays)

def delete_holiday(holidays):
    print("atostogų šalinimas. Pasirinkite ID įrašo kurį norite redaguoti.")
    id = input() #3
    for hol in holidays: # 0, 1, 2
        if id == str(hol['id']): #1 2 3
            print(
                f"{hol['id']}. Šalinama: Atostogos {hol['country']} {hol['city']}. Kaina gyvenant"
                f" {hol['accomodation']} "
                f"parai {hol['price']}")
            hol_pos_in_list = holidays.index(hol)
            del holidays[hol_pos_in_list]
    save_holidays(holidays)

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti atostogu pasirinkimus")
    print("2. Įtraukti atostogas i sarasa")
    print("3. koreguoti atostogas")
    print("4. šalinti atostogas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")

def print_holidays(holidays):
    for hol in holidays:
        print(f"{hol['id']}. Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} "
              f"parai {hol['price']}")
    print("--------------------------------------------------------------------------")
