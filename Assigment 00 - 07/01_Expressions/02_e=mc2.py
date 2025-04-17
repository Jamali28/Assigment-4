
def main():
    while True:
        try:
            mass_in_kg = float(input("\nEnter kilos of mass: "))
            energy_in_joules = mass_in_kg * (C ** 2)

            print("\ne = m * C^2...")
            print(f"m = {mass_in_kg} kg")
            print(f"C = {C} m/s")
            print(f"{energy_in_joules} joules of energy!")

        except ValueError:
            print("Please enter a valid number for mass.")

        again = input("\nDo you want to convert another mass? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

# Call the main() function
if __name__ == '__main__':
    main()