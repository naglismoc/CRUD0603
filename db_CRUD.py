# pip install mysql-connector-python
import mysql.connector

DB_CONFIG = {
    'host':'localhost', #127.0.0.1 alternatyva rasymui "localhost" ;)
    'port': 3312,
    'user':'root',
    'password':"root",
    'database':'holidays'
}

headers = ['id', 'country', 'city', 'accomodation', 'price']
def get_conn():
    return mysql.connector.connect(**DB_CONFIG)


def load_holidays():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from holidays")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    # print(rows)

    holidays = []
    for row in rows:
        holiday = {}
        for i in range(len(headers)):
            holiday[headers[i]] = str(row[i])
        holidays.append(holiday)
    # holidays = [dict(zip(headers, map(str, row))) for row in rows] #fancy pantsy alternatyva tam paciam
    return holidays


def create_holiday(holidays):
    print("atostogų pridėjimas:")
    print("Įveskite šalį")
    country = input()
    print("Įveskite miestą")
    city = input()
    print("Įveskite apgyvendinimo tipą")
    accomodation = input()
    print("Įveskite kainą")
    price = input()

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("INSERT INTO holidays(country, city, accomodation, price) VALUES (%s, %s, %s, %s)",
                (country,city,accomodation,price))
    conn.commit()

    cur.close()
    conn.close()


def edit_holiday(holidays):
    print("atostogų redagavimas. Pasirinkite ID įrašo kurį norite redaguoti.")
    id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from holidays WHERE id = %s",(id,))
    row = cur.fetchone()
    if row:
        print(f"{row[0]}. Atostogos {row[1]} {row[2]}. Kaina gyvenant {row[3]} "
              f"parai {row[4]}")
        print("Įveskite šalį")
        country = input()
        print("Įveskite miestą")
        city = input()
        print("Įveskite apgyvendinimo tipą")
        accomodation = input()
        print("Įveskite kainą")
        price = input()
        cur.execute('UPDATE `holidays` SET `country` = %s, `city` = %s,`accomodation` = %s, `price` =%s           '
                    'WHERE `id` = %s;',
                    (country,city,accomodation,price,id))
        conn.commit()
    cur.close()
    conn.close()

def delete_holiday(holidays):
    print("atostogų šalinimas. Pasirinkite ID įrašo kurį norite redaguoti.")
    id = input() #3

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("DELETE FROM holidays WHERE id = %s",(id,))
    conn.commit()

    cur.close()
    conn.close()
    print("Atlikome trinimo veiksma")




















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
