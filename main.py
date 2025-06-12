from location_extractor import extract_locations

def run_cli():
    print("Location Extractor")
    while True:
        user_input = input("\nEnter a sentence (or type 'exit' to quit):\n> ")
        if user_input.lower() == "exit":
            break
        locations = extract_locations(user_input)
        if locations:
           print(f" Extracted Locations: {locations}")
        else:
            print("No locations found.")

if __name__ == "__main__":
    run_cli()


