# Imports

import sys
from termcolor import colored, cprint
from selenium import webdriver
from main.models import *


def add_product_types():

    # Aurora Configuration
    category_name = "Sports"

    # Driver Configuration
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    for sub_category in SubCategory.objects.filter(category=Category.objects.get(name=category_name)):
        sub_category_name = sub_category.name
        ebay_url = input(f"Enter url for {sub_category_name}: ")

        if ebay_url == "//":
            continue

        driver.get(ebay_url)

        # Getting product types
        product_types = driver.find_elements_by_class_name(
            "b-textlink.b-textlink--sibling")

        # Assembling product types
        product_type_texts = []
        for product_type in product_types:
            product_type_texts.append(product_type.text)

        # Function which prints out all the product types in a certain convention
        def print_product_types():
            result = ""
            for product_type in product_types:
                result += f"    - {product_type.text} \n"
            return result

        # Getting user input
        permission = input(f"""
Do you want to add these product types?

{print_product_types()}
Category: {category_name}
Sub category: {sub_category_name}

Yes(Y) or No(N)?: """)

        # Running suitable algorithm
        if permission.upper() == "Y":
            for product_type_text in product_type_texts:
                category = Category.objects.get(name=category_name)
                sub_category = SubCategory.objects.get(
                    name=sub_category_name, category=category)
                ProductType.objects.create(
                    name=product_type_text, sub_category=sub_category)
            print(
                f"{str(len(product_type_texts))} product types added to {sub_category_name}!")
        elif permission.upper() == "N":
            print("Task aborted")
        else:
            print("Wrong input, try again...")

    driver.quit()
