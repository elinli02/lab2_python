import json
import re
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', help="с какого файла считываются данные input")
parser.add_argument('output', help="куда сохранятся валидные данные output")
args = parser.parse_args()


class Validator:
    def __init__(self):
        pass

    def check_email(email: str) -> bool:
        if re.match(r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$", email) is not None:
            return True
        return False

    def check_weight(weight: str) -> bool:
        if re.match(r"[\d]+", str(weight)) is not None:
            return True
        return False

    def check_snils(snils: str) -> bool:
        if re.match(r"[\d]{11}", snils) is not None:
            return True
        return False

    def check_passport_number(passport_number: str) -> bool:
        if re.match(r"[0-9]{6}", str(passport_number)) is not None:
            return True
        return False

    def check_occupation(occupation: str) -> bool:
        if re.match(r"^[\D]+", occupation) is not None:
            return True
        return False

    def check_age(age: int) -> bool:
        if re.match(r"^\d+", str(age)) is not None:
            return True
        return False

    def check_political_views(political_views: str) -> bool:
        if re.match(r"^\D+$", political_views) is not None:
            return True
        return False

    def check_worldview(worldview: str) -> bool:
        if re.match(r"^[\D]+$", worldview) is not None:
            return True
        return False

    def check_address(address: str) -> bool:
        if re.match(r"[а-яА-Я.\s\d-]+\s+[0-9]+$", address) is not None:
            return True
        return False


data = json.load(open(args.input, encoding='windows-1251'))

email = 0
weight = 0
snils = 0
passport_number = 0
occupation = 0
age = 0
political_views = 0
worldview = 0
address = 0

validate_data = list()
with tqdm(total=len(data)) as progressbar:
    for i in data:
        field = True
        if not Validator.check_email(i['email']):
            email += 1
            field = False
        if not Validator.check_weight(i['weight']):
            weight += 1
            field = False
        if not Validator.check_snils(i['snils']):
            snils += 1
            field = False
        if not Validator.check_passport_number(i['passport_number']):
            passport_number += 1
            field = False
        if not Validator.check_occupation(i['occupation']):
            occupation += 1
            field = False
        if not Validator.check_age(i['age']):
            age += 1
            field = False
        if not Validator.check_political_views(i['political_views']):
            political_views += 1
            field = False
        if not Validator.check_worldview(i['worldview']):
            worldview += 1
            field = False
        if not Validator.check_address(i['address']):
            address += 1
            field = False
        if field:
            validate_data.append(i)
        progressbar.update(1)

output_file = open(args.output, 'w')
data_file = json.dumps(validate_data, ensure_ascii=False, indent=4)
output_file.write(data_file)
output_file.close()

print("Количество валидных записей: ", len(validate_data))
print("Количество невалидных записей: ", len(data)-len(validate_data))
print(f'Количество неправильного email: {email}')
print(f'Количество неправильного weight: {weight}')
print(f'Количество неправильного snils: {snils}')
print(f'Количество неправильного passport_number: {passport_number}')
print(f'Количество неправильного occupation: {occupation}')
print(f'Количество неправильного age: {age}')
print(f'Количество неправильного political_views: {political_views}')
print(f'Количество неправильного worldview: {worldview}')
print(f'Количество неправильного address: {address}')



