import csv
import re

def IND_country_code(number):
    # Remove the Left-to-Right Override (LRO) character [U+202D]
    number = re.sub(r'[\u202A\u202B\u202C\u202D\u202E]', '', number)

    # Remove any existing spaces
    number = number.replace(' ', '')

    # Remove any existing '-' symbols
    number = number.replace('-', '')

    # Check if the number is empty or doesn't contain numeric value
    if not number or not any(char.isdigit() for char in number):
        return number

    # Split the number by ":::" delimiter if present
    numbers = number.split(":::")

    # Add +91 before numbers that don't start with a country code and have 10 digits
    for i, num in enumerate(numbers):
        if not num.startswith('+') and len(num.replace(' ', '')) == 10:
            # Add +91 before the number
            num = '+91' + num.strip()  # Strip whitespace
            numbers[i] = num

    # Join the numbers back together with ":::" delimiter
    return " ::: ".join(numbers)

# def add_formating(number):
#TODO: Add space formating for phone numbers based on their country code.

def main():
    # Define paths
    path = '../Datasets/'
    output_path = '../Outputs/'
    input_file = path + 'contacts.csv'
    output_file = output_path + 'updated_contacts.csv'

    # Read contacts from CSV
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        contacts = list(reader)

    # Modify phone numbers
    for contact in contacts:
        for key in contact.keys():
            # Check if the key represents a phone number field (e.g., 'Phone 1 - Value', 'Phone 2 - Value', etc.)
            if key.startswith('Phone') and key.endswith('- Value'):
                contact[key] = IND_country_code(contact[key])

    # Write modified data to new CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = contacts[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

    print("Modified contacts saved to", output_file)

if __name__ == "__main__":
    main()