from datetime import datetime

def getStartAndEndDate():
    start_day = input("Enter the start day: ")
    start_month = input("Enter the start month: ")
    start_year = input("Enter the start year (default 2024): ") or "2024"

    start_date = datetime.strptime(
        f"{start_day}/{start_month}/{start_year}", "%d/%m/%Y")

    print("The start date is: ", start_date)

    end_day = input("Enter the end day: ")

    if end_day == "":
        end_date = datetime.strptime("31/12/3000", "%d/%m/%Y")
    else:
        end_month = input("Enter the end month: ")
        end_year = input("Enter the end year (default 2024): ") or "2024"
        end_date = datetime.strptime(
            f"{end_day}/{end_month}/{end_year}", "%d/%m/%Y")
    
    print("The end date is: ", end_date)
    
    return start_date, end_date

def calculate_overlap_days(guest, start_date, end_date):
    if guest["start_date"] > end_date or guest["end_date"] < start_date:
        return 0

    guest_start_date = max(guest["start_date"], start_date)
    guest_end_date = min(guest["end_date"], end_date)

    return (guest_end_date - guest_start_date).days + 1