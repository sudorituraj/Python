name = input("what is your name? ")

match name:
    case "Ritu" | "Mahi" | "Raj":
        print("omega")

    case "Suraj" :
        print("kota")

    case _:
        print("who")
