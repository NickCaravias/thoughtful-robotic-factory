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
        return "rejected"

    # if any parameter is negative, return rejected because you cannot have a negative dimension or mass
    if width < 0 or height < 0 or length < 0 or mass < 0:
        return "rejected"

    # Calculate volume
    volume = width * height * length
    
    # check bulk and weight
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "rejected"
    elif is_bulky or is_heavy:
        return "special"
    else:
        return "standard"
