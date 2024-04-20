# This is a VCF (vCard) fixer
import re

def IND_country_code(number):
    # Removes Unicode control characters, spaces, hyphens, and parentheses from 'number'
    number = re.sub(r'[\u202A\u202B\u202C\u202D\u202E \-\(\)]', '', number)

    # Check if the number is empty or doesn't contain numeric value
    if not number or not any(char.isdigit() for char in number):
        return number

    # Add +91 before numbers that don't start with a country code and have 10 digits
    if not number.startswith('+') and len(number) == 10:
        # Add +91 before the number
        number = '+91' + number.strip()  # Strip whitespace
    return number

def read_vcf(vcf_file):
    with open(vcf_file, 'r', encoding='utf-8') as file:
        vcf_content = file.read()
    return vcf_content

def write_vcf(contacts, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(contacts)

def modify_vcf(vcf_content):
    # Split vCard content by 'BEGIN:VCARD' and 'END:VCARD' to extract individual contacts
    contacts = vcf_content.split('BEGIN:VCARD')[1:]

    # Iterate over each contact
    for i, contact in enumerate(contacts):
        # Extract phone numbers using regex
        phone_numbers = re.findall(r'TEL.*?:(.*?)\n', contact)

        # Modify each phone number
        modified_numbers = [IND_country_code(num) for num in phone_numbers]

        # Replace original phone numbers with modified ones
        for orig_num, mod_num in zip(phone_numbers, modified_numbers):
            contact = contact.replace(orig_num, mod_num)

        # Update the contact in the list
        contacts[i] = 'BEGIN:VCARD' + contact

    # Join the modified contacts
    modified_vcf_content = ''.join(contacts)
    return modified_vcf_content

def main():
    # Define paths
    path = '../Datasets/'
    output_path = '../Outputs/'
    input_file = path + 'contacts.vcf'
    output_file = output_path + 'updated_contacts.vcf'

    # Read vCard content
    vcf_content = read_vcf(input_file)

    # Modify vCard content
    modified_vcf_content = modify_vcf(vcf_content)

    # Write modified vCard content to a new file
    write_vcf(modified_vcf_content, output_file)

    print("Modified contacts saved to", output_file)

if __name__ == "__main__":
    main()