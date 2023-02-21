import csv
import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
from logg import logging


def save_csv(file_name):
    logging.info(f"Export in csv format: {file_name}.csv")

    with open(f'{file_name}.csv', 'w', encoding="utf-8", newline="") as file_w, \
            open('telephone_book.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        fieldnames = ["id", "name", "surname", "phone", "description"]
        writer = csv.DictWriter(file_w, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
        print(f"{file_name}.csv file saved\n")


def save_json(file_name):
    logging.info(f"Export in json format: {file_name}.json")

    with open(f'{file_name}.json', 'w', encoding="utf-8", newline="") as file_w, \
            open('telephone_book.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        data_dict = {rows['id']: rows for rows in all_data}
        file_w.write(json.dumps(data_dict, indent=4, ensure_ascii=False))


def save_xml(file_name):
    logging.info(f"Export in xml format: {file_name}.xml")

    with open(f'{file_name}.xml', 'w', encoding="utf-8", newline="") as file_w, \
            open('telephone_book.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        data_dict = {rows['id']: rows for rows in all_data}
        xml_data = dicttoxml(data_dict, attr_type=False).decode()
        dom = parseString(xml_data)
        file_w.write(dom.toprettyxml())
