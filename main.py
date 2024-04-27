from datetime import datetime
from date_handler import getStartAndEndDate
from expenses_calculator import calculateExpenses
from globals import cost_summaries, people_in_the_house, guests, externals


def finishingCalculation():
    TOTAL = {"single_host_cost": 0, "guest_cost": 0}

    time_now_code = datetime.now().strftime("%Y%m%d")

    with open(f"cost_summary_{time_now_code}.txt", "w") as file:
        for key, value in cost_summaries.items():
            TOTAL["single_host_cost"] += value["single_host_cost"]
            TOTAL["guest_cost"] += value["guest_cost"]

            rounded_host_cost = round(value["single_host_cost"], 2)
            rounded_guest_cost = round(value["guest_cost"], 2)

            print(key.upper())
            print("COST HOST: ", str(rounded_host_cost))
            print("GUEST: " + str(rounded_guest_cost))

            print("=====================================")

            file.write(key.upper() + "\n")
            file.write("COST HOST: " + str(rounded_host_cost) + "\n")
            file.write("GUEST: " + str(rounded_guest_cost) + "\n")
            file.write("=====================================\n")

        print("TOTAL COST HOST: ", round(TOTAL["single_host_cost"], 2))
        print("TOTAL GUEST: ", round(TOTAL["guest_cost"], 2))
        print("=====================================")

        print(
            f"TOTAL HOST+GUEST: {round(TOTAL['single_host_cost'] + TOTAL['guest_cost'], 2)}")
        print(
            f"Total COST: {round(TOTAL['single_host_cost'] * people_in_the_house + TOTAL['guest_cost'], 2)}")

        file.write("TOTAL COST HOST: " +
                   str(round(TOTAL["single_host_cost"], 2)) + "\n")
        file.write(
            f"TOTAL HOST+GUEST: {round(TOTAL['single_host_cost'] + TOTAL['guest_cost'], 2)}\n")
        file.write("TOTAL GUEST: " + str(round(TOTAL["guest_cost"], 2)) + "\n")

        file.write(
            f"Total COST: {round(TOTAL['single_host_cost'] * people_in_the_house + TOTAL['guest_cost'], 2)}")


def changeConfiguration():
    global people_in_the_house

    people_in_the_house = int(
        input("Enter the number of people in the house (default: 4): ") or 4)
    guests_number = int(input("Enter the number of guests (default: 1): ") or 1)

    for _ in range(guests_number):
        guest_name = input(
            f"Enter the name of the person in charge of the guest (default: Diego): ") or "Diego"
        
        guests[guest_name] = {"start_date": None, "end_date": None}

        start_date, end_date = getStartAndEndDate()

        guests[guest_name]["start_date"] = start_date
        guests[guest_name]["end_date"] = end_date

    externals_number = int(input("Enter the number of externals (default: 0): ") or 0)

    for _ in range(externals_number):
        external_name = input(f"Enter the name of the external: ")
        externals[external_name] = {"start_date": None, "end_date": None}

        start_date, end_date = getStartAndEndDate()

        externals[external_name]["start_date"] = start_date
        externals[external_name]["end_date"] = end_date


def main():
    AMMENITIES = []

    change_configuration = input(f'''calculating the expenses for {people_in_the_house} + 1 guest assigned to Diego\n
          Do you want to change the configuration? (y/n): ''')

    if change_configuration == "y":
        changeConfiguration()

    while True:
        amenity = input("Enter the name of the expense: ")

        if amenity == "":
            break

        AMMENITIES.append(amenity)

    calculateExpenses(AMMENITIES)

    finishingCalculation()


if __name__ == "__main__":
    main()
