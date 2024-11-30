def earliest_safe_day(infection_data, destination_city_index):
    # Iterate through the days
    for day in range(len(infection_data)):
        # Check if the destination city is infected
        if infection_data[day][destination_city_index] == '0':
            return day + 1  # Days are 1-indexed as per the problem description
    return -1  # In case there is no safe day

def main():
    # Sample input based on the description
    infection_data = [
        "00000",  # Day 1
        "00000",  # Day 2
        "00110",  # Day 3
        "01100",  # Day 4
        "01000",  # Day 5
        "10010",  # Day 6
    ]
    
    # Assuming the destination city is at index 3 (4th city)
    destination_city_index = 3
    
    # Find the earliest safe day
    safe_day = earliest_safe_day(infection_data, destination_city_index)
    
    # Output the result
    print(safe_day)

if __name__ == "__main__":
    main()