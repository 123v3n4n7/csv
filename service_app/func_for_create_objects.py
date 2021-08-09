from decimal import Decimal, InvalidOperation
from .models import CSVObject


def bulk_create_objects(file_data):
    objects_list = []
    lines = file_data.split("\n")
    for line in lines[1:]:
        fields = line.split(";")
        try:
            price = Decimal(fields[5])
        except InvalidOperation:
            price = None
        try:
            price_sp = Decimal(fields[5])
        except InvalidOperation:
            price_sp = None
        try:
            joint_purchases = int(fields[9])
        except ValueError:
            joint_purchases = None
        try:
            amount = int(fields[7])
        except ValueError:
            amount = None
        objects_list.append(CSVObject(
            code=fields[0],
            name=fields[1],
            level_1=fields[2],
            level_2=fields[3],
            level_3=fields[4],
            price=price,
            price_sp=price_sp,
            amount=amount,
            fields_of_options=fields[8],
            joint_purchases=joint_purchases,
            unit=fields[10],
            image=fields[11],
            show_on_main_page=fields[12],
            description=fields[13]
        ))
    CSVObject.objects.bulk_create(objects_list)
