import requests
import re

class PseudoHacker:
    def get_info(phone):
        data = requests.get(f'https://fincalculator.ru/api/tel/{phone}').json()
        phoned = data['phone']
        if phoned == "":
            phoned = phone
        country = data['country']
        if country == "":
            country = "Unknown"
        region = data['region']
        if region == "":
            region = "Unknown"
        operator = data['operator']
        if operator == "":
            operator = "Unknown"
        return f"""
    Phone:  {phoned}
    Country:  {country}
    Region:  {region}
    Operator:  {operator}
"""

    def is_phone(phone):
        pattern = r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'
        return re.match(pattern, phone)
    
    def checkphone(phone=None):
        if phone == None:
            print("Invalid phone number")
        if not PseudoHacker.is_phone(phone):
            print("Invalid phone number")
        else:
            print(PseudoHacker.get_info(phone))
            
if __name__ == "__main__":
    print(PseudoHacker.checkphone("77772242210"))