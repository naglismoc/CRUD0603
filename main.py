from db_CRUD import *


while True:
    holidays = load_holidays()
    print_info()
    choise = input()

    match choise:
        case '1':
           print_holidays(holidays)
        case '2':
            create_holiday(holidays)
        case '3':
           edit_holiday(holidays)
        case '4':
           delete_holiday(holidays)
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
