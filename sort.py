import csv

def sort(width: float, height: float, length: float, mass: float) -> str:
    '''
    Sorts packages into three categories: standard, special, and rejected.
    Standard packages have a volume less than 1,000,000 cubic centimeters and weigh less than 20 kg.
    Special packages have a volume greater than or equal to 1,000,000 cubic centimeters or weigh 20 kg or more.
    Rejected packages are both special and have a volume greater than or equal to 1,000,000 cubic centimeters.

    @param width: float - The width of the package in centimeters.
    @param height: float - The height of the package in centimeters.
    @param length: float - The length of the package in centimeters.
    @param mass: float - The mass of the package in kilograms.
    @return: string - The category of the package.
    '''
    
    # check if any parameter is not a number
    if not all(isinstance(x, (int, float)) for x in [width, height, length, mass]):
        return "error", 0, 0

    # if any parameter is negative, return rejected because you cannot have a negative dimension or mass
    if width < 0 or height < 0 or length < 0 or mass < 0:
        return "error", 0, 0

    # Calculate volume
    volume = width * height * length
    
    # check bulk and weight
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "rejected", volume, mass
    elif is_bulky or is_heavy:
        return "special", volume, mass
    else:
        return "standard", volume, mass


if __name__ == "__main__":
    order_standards = {
        "REJECTED": {
            "mass": [],
            "volume": []
        },
        "SPECIAL": {
            "mass": [],
            "volume": []
        },
        "STANDARD": {
            "mass": [],
            "volume": []
        }
    }
    
    # open the file in read mode
    with open('packages.csv', 'r') as file:
        data = csv.reader(file)

        for row in data:

            if len(row) == 4:                
                try:
                    classifier, volume, mass = sort(float(row[0]), float(row[1]), float(row[2]), float(row[3]))

                except ValueError:
                    continue
            
                if classifier == "rejected":
                        order_standards["REJECTED"]["mass"].append(mass)
                        order_standards["REJECTED"]["volume"].append(volume)
                elif classifier == "special":
                    order_standards["SPECIAL"]["mass"].append(mass)
                    order_standards["SPECIAL"]["volume"].append(volume)
                elif classifier == "standard":
                    order_standards["STANDARD"]["mass"].append(mass)
                    order_standards["STANDARD"]["volume"].append(volume)

        for key in order_standards:
            # print order type we are viewing data for
            print(f"=== Checking data for {key} orders ===")
            print(f"Total number of packages is {len(order_standards[key]['mass'])}")

            # stats for the mass
            curr_mass_max = max(order_standards[key]['mass'])
            curr_mass_min = min(order_standards[key]['mass'])
            curr_mass_avg = sum(order_standards[key]['mass']) / len(order_standards[key]['mass'])

            print(f"Max mass: {curr_mass_max}")
            print(f"Min mass: {curr_mass_min}")
            print(f"Average mass: {curr_mass_avg}")

            # stats for the volume
            curr_vol_max = max(order_standards[key]['volume'])
            curr_vol_min = min(order_standards[key]['volume'])
            curr_vol_avg = sum(order_standards[key]['volume']) / len(order_standards[key]['volume'])

            print(f"Max volume: {curr_vol_max}")
            print(f"Min volume: {curr_vol_min}")
            print(f"Average volume: {curr_vol_avg}")

            print('\n')





            


        
        