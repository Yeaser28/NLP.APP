import phonenumbers # type: ignore
from phonenumbers import geocoder, carrier # type: ignore

phonenumber1 = input("Enter phone number with country code (e.g., +1234567890): ")
parsed_number = phonenumbers.parse(phonenumber1)
country = geocoder.description_for_number(parsed_number, "en")
service_provider = carrier.name_for_number(parsed_number, "en")

print(f"Country: {country}")
print(f"Service Provider: {service_provider}")