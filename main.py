from datetime import datetime

# globals
people_in_the_house = 4
guests = {"Diego": {"start_date": None, "end_date": None}}
externals = {}
cost_summaries = {}


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

        print(f"TOTAL HOST+GUEST: {round(TOTAL['single_host_cost'] + TOTAL['guest_cost'], 2)}")
        print(f"Total COST: {round(TOTAL['single_host_cost'] * people_in_the_house + TOTAL['guest_cost'], 2)}")

        file.write("TOTAL COST HOST: " + str(round(TOTAL["single_host_cost"], 2)) + "\n")
        file.write(f"TOTAL HOST+GUEST: {round(TOTAL['single_host_cost'] + TOTAL['guest_cost'], 2)}\n")
        file.write("TOTAL GUEST: " + str(round(TOTAL["guest_cost"], 2)) + "\n")

        file.write(f"Total COST: {round(TOTAL['single_host_cost'] * people_in_the_house + TOTAL['guest_cost'], 2)}")

def getStartAndEndDate():
    start_day = input("Enter the start day: ")
    start_month = input("Enter the start month: ")
    start_year = input("Enter the start year (default 2024): ") or "2024"

    start_date = datetime.strptime(
        f"{start_day}/{start_month}/{start_year}", "%d/%m/%Y")

    print("The start date is: ", start_date)

    end_day = input("Enter the end day: ")
    end_month = input("Enter the end month: ")
    end_year = input("Enter the end year (default 2024): ") or "2024"

    end_date = datetime.strptime(
        f"{end_day}/{end_month}/{end_year}", "%d/%m/%Y")
    
    return start_date, end_date

def calculateExpenses(amenity, taxes):
    print("Calculating the expenses of ", amenity)

    amenity_cost = input(f"Enter the cost of {amenity}: ")
    amenity_cost = float(amenity_cost) + taxes

    print("The cost of ", amenity, " plus taxes is: ", amenity_cost)
    print("=====================================")

    start_date, end_date = getStartAndEndDate()

    difference = (end_date - start_date).days + 1

    print("The difference in days is: ", difference)

    print("=====================================")

    guest_stay_days = int(
        input("Enter the number of days the guest stayed: "))

    total_days_sum = (difference *
                        people_in_the_house) + guest_stay_days
    days_per_host = difference

    single_host_cost = (days_per_host * amenity_cost) / total_days_sum

    guest_cost = (guest_stay_days * amenity_cost) / total_days_sum

    cost_summaries[amenity] = {
        "single_host_cost": single_host_cost,
        "guest_cost": guest_cost
    }

    print("=====================================")
  
def changeConfiguration():
    global people_in_the_house

    people_in_the_house = int(input("Enter the number of people in the house: "))
    guests = int(input("Enter the number of guests (default: 1): ") or 1)

    for guest in range(guests):
        guest_name = input(f"Enter the name of the person in charge of the guest: ")
        guests[guest_name] = {"start_date": None, "end_date": None}

        start_date, end_date = getStartAndEndDate()

        guests[guest_name]["start_date"] = start_date
        guests[guest_name]["end_date"] = end_date

    externals = int(input("Enter the number of externals (default: 0): ") or 0)

    for external in range(externals):
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

    print('list of expenses: \n')
    for index, amenity in enumerate(AMMENITIES):
           print(f'''{index + 1}. {amenity} \n''')
    
    taxes = float(input("Enter the taxes: ")) / len(AMMENITIES)

    for amenity in AMMENITIES:
        calculateExpenses(amenity, taxes)

    finishingCalculation()


if __name__ == "__main__":
    main()
