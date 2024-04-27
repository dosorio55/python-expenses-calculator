from datetime import datetime
from date_handler import getStartAndEndDate
from expenses_calculator import calculateExpenses
from globals import cost_summaries, guests, externals, people_in_the_house

def finishingCalculation():
    TOTAL = {}

    time_now_code = datetime.now().strftime("%Y%m%d")

    with open(f"cost_summary_{time_now_code}.txt", "w") as file:
        for key, value in cost_summaries.items():
            print(key.upper())
            file.write(key.upper() + "\n")

            for person in value:
                value_to_pay = value[person] if person not in guests else value['Todos'] + guests[person]["amenities_expenses"][key]

                print(f"{person.upper()} PAGA: {round(value_to_pay, 2)}")
                file.write(f"{person.upper()} PAGA: {round(value_to_pay, 2)}\n")

                TOTAL[person] = TOTAL.get(person, 0) + value_to_pay
                
            file.write("=====================================\n")
            print("=====================================")
            
        print("=====================================")
        file.write("=====================================\n")
        
        for person, valueToPay in TOTAL.items():
            print(f"{person.upper()} PAGA: {round(valueToPay, 2)}")
            file.write(f"{person.upper()} PAGA: {round(valueToPay, 2)}\n")
        



def changeConfiguration():
    people_in_the_house["ammount"] = int(
        input("Enter the number of people in the house (default: 4): ") or 4)
    guests_number = int(input("Enter the number of guests (default: 1): ") or 1)

    for _ in range(guests_number):
        guest_name = input(
            f"Enter the name of the person in charge of the guest (default: Diego): ") or "Diego"
        
        guests[guest_name] = {"start_date": None, "end_date": None, "overlap_days": 0, "amenities_expenses": {}}

        start_date, end_date = getStartAndEndDate()

        guests[guest_name]["start_date"] = start_date
        guests[guest_name]["end_date"] = end_date

    externals_number = int(input("Enter the number of externals (default: 0): ") or 0)

    for _ in range(externals_number):
        external_name = input(f"Enter the name of the external: ")
        externals[external_name] = {"start_date": None, "end_date": None, "overlap_days": 0, "amenities_expenses": {}}

        start_date, end_date = getStartAndEndDate()

        externals[external_name]["start_date"] = start_date
        externals[external_name]["end_date"] = end_date


def main():
    global people_in_the_house

    AMMENITIES = []

    change_configuration = input(f'''calculating the expenses for {people_in_the_house["ammount"]} + 1 guest assigned to Diego\n
          Do you want to change the configuration? (y/n): ''')

    if change_configuration == "y" or change_configuration == "Y":
        changeConfiguration()

    print("=====================================")

    while True:
        amenity = input("Enter the name of the expense: ")

        if amenity == "":
            break

        AMMENITIES.append(amenity)

    calculateExpenses(AMMENITIES)

    finishingCalculation()


if __name__ == "__main__":
    main()
