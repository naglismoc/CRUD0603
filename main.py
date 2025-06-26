from CRUD_functions import *

hollidays = load_default_data()
id_counter = 3

while True:
    print_info()
    choise = input()

    match choise:
        case '1':
           print_hollidays(hollidays)
        case '2':
            id_counter +=1
            hollidays.append(create_hollidays(id_counter))
        case '3':
           edit_hollidays(hollidays)
        case '4':
           delete_hollidays(hollidays)
        case '5':
            print("programa sustabdyta")
            break
































# for hol in hollidays:
#     if hol['price'] == 70:
#         print(f"Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} parai {hol['price']}")

#===================== Neringai =) ==============================================
# search_keyword = 70
# for hol in hollidays:
#     for key in hollidays[0].keys():
#         # print(hol[key])
#         if str(search_keyword).lower() in str(hol[key]).lower():
#             print(f"Atostogos {hol['country']} {hol['city']}. Kaina gyvenant {hol['accomodation']} parai {hol['price']}")
#===================== Neringai =) ==============================================
