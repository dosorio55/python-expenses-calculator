from date_handler import getStartAndEndDate, calculate_overlap_days
from globals import guests, externals, cost_summaries, people_in_the_house

def calculate_all_overlap_days(start_date, end_date, difference):
    total_guest_stay_days = 0
    total_external_stay_days = 0

    for guest in guests.values():
        guest["overlap_days"] = calculate_overlap_days(
            guest, start_date, end_date)
        total_guest_stay_days += guest["overlap_days"]

    for external in externals.values():
        external["overlap_days"] = calculate_overlap_days(
            external, start_date, end_date)
        total_external_stay_days += external["overlap_days"]

    return (people_in_the_house["ammount"] * difference) + total_guest_stay_days + total_external_stay_days


def calculate_guest_cost(amenity_cost, total_days_sum, amenity):
    for guest in guests.values(): 
        guest["amenities_expenses"][amenity] = (
            guest["overlap_days"] * amenity_cost) / total_days_sum

    for external in externals.values():
        external["amenities_expenses"][amenity] = (
            external["overlap_days"] * amenity_cost) / total_days_sum


def getCalculations(amenity, taxes):
    print("Calculating the expenses of ", amenity)

    amenity_cost = input(f"Enter the cost of {amenity}: ")
    amenity_cost = float(amenity_cost) + taxes

    print("The cost of ", amenity, " plus taxes is: ", amenity_cost)
    print("=====================================")

    start_date, end_date = getStartAndEndDate()

    difference = (end_date - start_date).days + 1

    print("The difference in days is: ", difference)

    print("=====================================")

    days_per_host = difference

    total_days_sum = calculate_all_overlap_days(
        start_date, end_date, difference)

    calculate_guest_cost(amenity_cost, total_days_sum, amenity)

    single_host_cost = (days_per_host * amenity_cost) / total_days_sum

    cost_summaries[amenity] = {
        "Todos": single_host_cost,
    }

    cost_summaries[amenity] = {
        "Todos": single_host_cost,
    }

    for name, guest in guests.items():
        cost_summaries[amenity].update(
            {name: guest["amenities_expenses"][amenity]})

    for name, external in externals.items():
        cost_summaries[amenity].update(
            {name: external["amenities_expenses"][amenity]})
        
    print("=====================================")


def calculateExpenses(AMMENITIES):
    print('list of expenses: \n')
    for index, amenity in enumerate(AMMENITIES):
        print(f'''{index + 1}. {amenity}\n''')

    taxes = float(input("Enter the taxes: ")) / len(AMMENITIES)

    for amenity in AMMENITIES:
        getCalculations(amenity, taxes)
