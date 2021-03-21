# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored

from main.models import *


def filters():

    # ---------- General Configuration Automation ----------

    print(colored("\nGeneral Configuration Automation starting...",
                  "yellow", attrs=['bold']))

    permission_message = "Do you wish to continue?(Y/N): "

    permission = input(permission_message).title()
    if permission == "Y":
        pass
    else:
        return

    # Database

    category_name = "Fashion"
    sub_category_name = input("Enter sub category name: ")
    sub_category_url = input("Enter url: ")

    category = Category.objects.get(name=category_name)
    sub_category = SubCategory.objects.get(
        name=sub_category_name, category=category)

    # Product types information

    product_types = ProductType.objects.filter(
        sub_category=sub_category, parent_product_type="")
    product_types_with_no_name = []  # Product types with name not matching
    product_types_urls = []  # Contains all the urls of product types

    # Direct filter link

    if len(product_types) == 0:
        ProductType.objects.create(
            name=sub_category_name, sub_category=sub_category)

    product_types = ProductType.objects.filter(
        sub_category=sub_category, parent_product_type="")

    # Driver Configuration

    print("Opening web browser...")
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Printing product types

    print(colored("\nProduct types: ", attrs=['bold']))
    for product_type in product_types:
        print(colored(f"- {product_type.name}", attrs=['dark']))

    # Opening sub category webpage

    print(colored("\nOpening sub category page...", "yellow", attrs=['bold']))
    driver.get(sub_category_url)

    # Product types links

    product_types_links = driver.find_element_by_class_name(
        'b-module.b-list.b-categorynavigations.b-display--landscape').find_elements_by_class_name('b-textlink.b-textlink--sibling')

    # Getting URLS for product types
    print(colored("\nProduct types and links: ", attrs=['bold']))
    for product_type in product_types:
        x = 0
        for product_type_link in product_types_links:
            # Checking to see if the product type names from the database
            # match the product type names from eBay product type links
            if product_type_link.text == product_type.name:
                product_type_text = colored(
                    f"{product_type.name}", "blue")
                product_type_link_text = colored(
                    f"{product_type_link.get_attribute('href')}", attrs=["underline"])
                print(f"{product_type_text} - {product_type_link_text}")
                product_types_urls.append(
                    product_type_link.get_attribute('href'))
            elif product_type.name != product_type_link.text:
                x += 1

        if len(product_types) == x:
            print(
                colored(f"No matching name for {product_type.name}", "red"))
            product_types_with_no_name.append(product_type)

        if len(product_types) == 1:
            message = input(
                "Does the sub category link directly to filters?(Y/N): ").title()
            if message == "Y":
                url = input(f"\nEnter URL for {product_type.name}: ")
                product_types_urls.append(url)

    # Getting URLs for product types with no matching names

    for product_type in product_types_with_no_name:
        url = input(f"\nEnter URL for {product_type.name}: ")
        print(colored(
            f"URL successfully added for {product_type.name}!", "yellow", attrs=["bold"]))
        product_types_urls.insert(product_types.index(product_type), url)

    # ---------- Main Filter Automation ---------

    print(colored("\nMain Filter Automation starting...",
                  "yellow", attrs=['bold']))

    for product_type_url in product_types_urls:

        print(colored(
            f"\nOpening page for {product_types[product_types_urls.index(product_type_url)]}\n", "yellow", attrs=['bold']))

        driver.get(product_type_url)

        try:
            # Clicking on button that shows filters

            see_all_btn = driver.find_element_by_xpath(
                '//*[@id="s0-16-13_2-0-1[1]-0-6-0-0[0]-2[0]_1-3"]/button')
            see_all_btn.click()

            # Locating filter container

            filter_categories_container = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "x-overlay__wrapper--left"))
            )
            # Deciding which filters to include

            filter_categories = filter_categories_container.find_elements_by_class_name(
                'x-overlay-aspect')
            excluded_filter_categories = [
                "Condition",
                "Price",
                "Buying Format",
                "Item Location",
                "Delivery Options",
                "Show only",
                "Seller",
            ]
            included_filter_categories = []
            for filter_category in filter_categories:
                if filter_category.text in excluded_filter_categories:
                    pass
                else:
                    included_filter_categories.append(filter_category)

            # Clicking on each filter category to access the filters

            for filter_category in included_filter_categories:
                filter_category.click()
                filters = WebDriverWait(driver, 100).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "x-refine__multi-select.x-overlay-sub-panel__aspect-option"))
                )

                # Output
                print(colored(f"\n{filter_category.text}:",
                              "blue", attrs=["bold"]))
                for filter in filters:
                    print(colored(f" - {filter.text}",
                                  "white", attrs=['dark']))
                    Filter.objects.create(
                        name=filter.text,
                        filter_category=filter_category.text,
                        product_type=ProductType.objects.get(
                            name=product_types[product_types_urls.index(
                                product_type_url)],
                            sub_category=sub_category
                        )
                    )
        except:
            print(colored(
                f"{product_types[product_types_urls.index(product_type_url)]} skipped", "red"))
            continue

    driver.quit()


# filters()

def filters_for_product_type():

     # ---------- General Configuration Automation ----------

    print(colored("\nGeneral Configuration Automation starting...",
                  "yellow", attrs=['bold']))

    permission_message = "Do you wish to continue?(Y/N): "

    permission = input(permission_message).title()

    if permission == "Y":
        pass
    else:
        return

    # Database

    category_name = input("Category: ")
    sub_category_name = input("Sub category: ")
    product_type_name = input("Product type: ")

    product_type_url = input("Enter url: ")

    category = Category.objects.get(name=category_name)
    sub_category = SubCategory.objects.get(
        name=sub_category_name, category=category)
    product_type = ProductType.objects.get(name=product_type_name, sub_category=sub_category)

    # Driver Configuration

    print("Opening web browser...")
    PATH = "C:/Program Files (x86)/chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    # Goint to product type URL

    driver.get(product_type_url)

    # Getting and clicking on see all button

    see_all_btn = driver.find_element_by_xpath('//*[@id="s0-16-13_2-0-1[1]-0-6-0-0[0]-2[0]_1-3"]/button')

    see_all_btn.click()

    # TODO: Wait and get all filter categories

    filter_categories = WebDriverWait(driver, 100).until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "x-overlay-aspect"))
        )

    excluded_filter_categories = ["Condition", "Price", "Buying Format",
                                          "Item Location", "Delivery Options", "Show only", "Seller"]

    included_filter_categories = [
                filter_category for filter_category in filter_categories if filter_category.text not in excluded_filter_categories]

    # TODO: Loop through all categories

    for included_filter_category in included_filter_categories:

        print(colored(f"    {included_filter_category.text}", "cyan"))

        included_filter_category.click()

        # TODO: Getting all filters

        filters = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "x-refine__multi-select.x-overlay-sub-panel__aspect-option"))
                )

        for filter in filters:
            if len(Filter.objects.filter(name=filter.text, filter_category=included_filter_category.text, product_type=product_type)) == 0:
                Filter.objects.create(
                            name=filter.text, filter_category=included_filter_category.text, product_type=product_type)
                print(f"        - {filter.text}")
            else:
                print(colored(f"        - {filter.text} may have been added already", "red"))

        print("")



