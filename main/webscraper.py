# Imports
from os import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
from main.models import *
import winsound


def permission():

    permission = input("\nDo you want to proceed?(Y/N): ").title()

    if permission == "Y":
        category_name = input("Category: ")
        sub_category_name = input("Sub-category: ")
        sub_category_url = input("Sub-category URL: ")

        permission2 = input(
            "Which algorithm do you want to run?(CPTs[C]/PPTs Filters[PF])]CPTs Filters[CF]: ").upper()
        if permission2 == "C":
            add_child_product_types(
                category_name, sub_category_name, sub_category_url)
        elif permission2 == "PF":
            add_filters_for_PPTs(
                category_name, sub_category_name, sub_category_url)
        elif permission2 == "CF":
            add_filters_for_CPTs(
                category_name, sub_category_name, sub_category_url)
        elif permission2 == "ALL":
            add_child_product_types(
                category_name, sub_category_name, sub_category_url)
            add_filters_for_PPTs(
                category_name, sub_category_name, sub_category_url)
            add_filters_for_CPTs(
                category_name, sub_category_name, sub_category_url)
        else:
            return

        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

    else:
        return


def main_header(text):

    print(colored(text, "yellow", attrs=["bold"]))


def add_child_product_types(category_name, sub_category_name, sub_category_url):

    main_header("\nInitiation web scraper...\n")

    # Database setup

    category = Category.objects.get(name=category_name)
    sub_category = SubCategory.objects.get(
        name=sub_category_name, category=category)
    product_types = ProductType.objects.filter(sub_category=sub_category)

    parent_product_types = ProductType.objects.filter(
        sub_category=sub_category, parent_product_type="")

    # --- Output 1 ---

    print(colored("Category: ", "blue") + category.name)
    print(colored("Sub-category: ", "blue") + sub_category.name)
    print(colored("Product types: ", "blue"))
    for product_type in product_types:
        print(f" - {product_type.name}")

    # Data

    sub_category_url = sub_category_url

    # Driver Configuration

    main_header("\nOpening web browser...")

    PATH = 'C:/Program Files (x86)/chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    # TODO: Going to sub-category page

    driver.get(sub_category_url)

    # TODO: Getting Parent Product type elements

    parent_product_type_elements = driver.find_element_by_class_name(
        "b-module.b-list.b-categorynavigations.b-display--landscape").find_elements_by_class_name("b-textlink.b-textlink--sibling")

    # TODO: Getting Parent Product Type links and sorting links according to Parent Product Types

    parent_product_type_links = [parent_product_type_element.get_attribute(
        'href') for parent_product_type in parent_product_types for parent_product_type_element in parent_product_type_elements if parent_product_type.name == parent_product_type_element.text]

    # --- Output 2 ---

    print("")
    for parent_product_type_link in parent_product_type_links:
        print(colored(parent_product_types[parent_product_type_links.index(
            parent_product_type_link)].name, "magenta") + f" - {parent_product_type_link}")
    print("")

    # TODO: Going to each link

    for parent_product_type_link in parent_product_type_links:

        print(colored(parent_product_types[parent_product_type_links.index(
            parent_product_type_link)].name, "cyan"))

        driver.get(parent_product_type_link)

        # TODO: Getting Child Product Type Elements

        try:
            more_btn = driver.find_element_by_class_name(
                "b-list__footer-resetbutton.b-list__footer--viewall")

            more_btn.click()

            child_product_type_elements = driver.find_element_by_class_name(
                "b-module.b-list.b-categorynavigations.b-display--landscape").find_elements_by_class_name("b-textlink.b-textlink--sibling")

            # TODO: Getting text from Child Product Type Elements

            child_product_type_elements_text = [
                child_product_type_element.text for child_product_type_element in child_product_type_elements]

            for child_product_type_element_text in child_product_type_elements_text:
                if len(ProductType.objects.filter(name=child_product_type_element_text, sub_category=sub_category, parent_product_type="")) == 0:
                    ProductType.objects.create(name=child_product_type_element_text, sub_category=sub_category, parent_product_type=parent_product_types[parent_product_type_links.index(
                        parent_product_type_link)].name)
                    print(f" - {child_product_type_element_text}")
                else:
                    print(colored(
                        f" - {child_product_type_element_text} is a Parent Product Type or may have already been added.", "red"))
            print("")
        except:
            child_product_type_elements = driver.find_element_by_class_name(
                "b-module.b-list.b-categorynavigations.b-display--landscape").find_elements_by_class_name("b-textlink.b-textlink--sibling")

            # TODO: Getting text from Child Product Type Elements

            child_product_type_elements_text = [
                child_product_type_element.text for child_product_type_element in child_product_type_elements]

            for child_product_type_element_text in child_product_type_elements_text:
                if len(ProductType.objects.filter(name=child_product_type_element_text, sub_category=sub_category, parent_product_type="")) == 0:
                    ProductType.objects.create(name=child_product_type_element_text, sub_category=sub_category, parent_product_type=parent_product_types[parent_product_type_links.index(
                        parent_product_type_link)].name)
                    print(f" - {child_product_type_element_text}")
                else:
                    print(colored(
                        f" - {child_product_type_element_text} is a Parent Product Type or may have already been added.", "red"))
            print("")

    driver.quit()


def add_filters_for_PPTs(category_name, sub_category_name, sub_category_url):

    main_header("\nInitiation web scraper...\n")

    # Database setup

    category = Category.objects.get(name=category_name)
    sub_category = SubCategory.objects.get(
        name=sub_category_name, category=category)
    product_types = ProductType.objects.filter(sub_category=sub_category)

    parent_product_types = ProductType.objects.filter(
        sub_category=sub_category, parent_product_type="")

    # --- Output 1 ---

    print(colored("Category: ", "blue") + category.name)
    print(colored("Sub-category: ", "blue") + sub_category.name)
    print(colored("Product types: ", "blue"))
    for product_type in product_types:
        print(f" - {product_type.name}")

    # Data

    sub_category_url = sub_category_url

    # Driver Configuration

    main_header("\nOpening web browser...")

    PATH = 'C:/Program Files (x86)/chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    # TODO: Going to sub-category Page

    driver.get(sub_category_url)

    # TODO: Getting Parent Product Type elements

    # parent_product_type_elements = driver.find_element_by_class_name(
    #     "b-module.b-list.b-categorynavigations.b-display--landscape").find_elements_by_class_name("b-textlink.b-textlink--sibling")

    parent_product_type_elements = driver.find_elements_by_class_name(
        "b-textlink.b-textlink--sibling")

    # TODO: Getting Parent Product Type links and sorting links according to Parent Product Types

    parent_product_type_links = [parent_product_type_element.get_attribute(
        'href') for parent_product_type in parent_product_types for parent_product_type_element in parent_product_type_elements if parent_product_type.name == parent_product_type_element.text]

    if len(product_types) == 0:
        ProductType.objects.create(
            name=sub_category.name, sub_category=sub_category)
        parent_product_type_links = [sub_category_url]
        product_types = ProductType.objects.filter(sub_category=sub_category)
        parent_product_types = ProductType.objects.filter(
            sub_category=sub_category, parent_product_type="")
    elif len(product_types) == 1:
        parent_product_type_links = [sub_category_url]

    # --- Output 2 ---

    print("")
    for parent_product_type_link in parent_product_type_links:
        print(colored(parent_product_types[parent_product_type_links.index(
            parent_product_type_link)].name, "magenta") + f" - {parent_product_type_link}")
    print("")

    # Direct filter integration

    # TODO: Going to each link

    for parent_product_type_link in parent_product_type_links:

        print(colored(parent_product_types[parent_product_type_links.index(
            parent_product_type_link)].name, "cyan"))

        driver.get(parent_product_type_link)

        # TODO: Getting and clicking on see all button

        try:
            # see_all_btn = driver.find_element_by_xpath(
            #     '//*[@id="s0-16-13_2-0-1[1]-0-6-0-0[0]-2[0]_1-3"]/button')
            see_all_btn = driver.find_element_by_xpath(
                '//*[@id="s0-16-13_2-0-1[1]-0-6-0-0[0]-2[0]_1-3"]/button')
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
                    parent_product_type = parent_product_types[parent_product_type_links.index(
                        parent_product_type_link)]
                    if len(Filter.objects.filter(name=filter.text, filter_category=included_filter_category.text, product_type=parent_product_type)) == 0:
                        Filter.objects.create(
                            name=filter.text, filter_category=included_filter_category.text, product_type=parent_product_type)
                        print(f"        - {filter.text}")
                    else:
                        print(colored(
                            f"        - {filter.text} may have been added already", "red"))

            print("")
        except:
            continue

    # Direct filter integration

    driver.quit()


def add_filters_for_CPTs(category_name, sub_category_name, sub_category_url):

    main_header("\nInitiation web scraper...\n")

    # Database setup

    category = Category.objects.get(name=category_name)
    sub_category = SubCategory.objects.get(
        name=sub_category_name, category=category)
    product_types = ProductType.objects.filter(sub_category=sub_category)

    parent_product_types = ProductType.objects.filter(
        sub_category=sub_category, parent_product_type="")

    # --- Output 1 ---

    print(colored("Category: ", "blue") + category.name)
    print(colored("Sub-category: ", "blue") + sub_category.name)
    print(colored("Product types: ", "blue"))
    for product_type in product_types:
        print(f" - {product_type.name}")

    # Data

    sub_category_url = sub_category_url

    # Driver Configuration

    main_header("\nOpening web browser...")

    PATH = 'C:/Program Files (x86)/chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    # TODO: Going to sub-category Page

    driver.get(sub_category_url)

    # TODO: Getting Parent Product Type elements

    parent_product_type_elements = driver.find_element_by_class_name(
        "b-module.b-list.b-categorynavigations.b-display--landscape").find_elements_by_class_name("b-textlink.b-textlink--sibling")

    # TODO: Getting Parent Product Type links and sorting links according to Parent Product Types

    parent_product_type_links = [parent_product_type_element.get_attribute(
        'href') for parent_product_type in parent_product_types for parent_product_type_element in parent_product_type_elements if parent_product_type.name == parent_product_type_element.text]

    # --- Output 2 ---

    print("")
    for parent_product_type_link in parent_product_type_links:
        print(colored(parent_product_types[parent_product_type_links.index(
            parent_product_type_link)].name, "magenta") + f" - {parent_product_type_link}")
    print("")

    # TODO: Going to each link

    for parent_product_type_link in parent_product_type_links:

        print(colored(parent_product_types[parent_product_type_links.index(
            parent_product_type_link)].name, "cyan"))

        driver.get(parent_product_type_link)

        # TODO: Getting Children Product Type elements

        try:
            more_btn = driver.find_element_by_class_name(
                "b-list__footer-resetbutton.b-list__footer--viewall")

            more_btn.click()

            child_product_type_elements = driver.find_element_by_class_name(
                "b-module.b-list.b-categorynavigations.b-display--landscape").find_elements_by_class_name("b-textlink.b-textlink--sibling")

            # TODO: Getting Children Product Type links and sorting links according to Children Product Types

            child_product_types = ProductType.objects.filter(parent_product_type=parent_product_types[parent_product_type_links.index(
                parent_product_type_link)].name)

            child_product_type_links = [children_product_type_element.get_attribute(
                'href') for children_product_type in child_product_types for children_product_type_element in child_product_type_elements if children_product_type.name == children_product_type_element.text]

            # --- Output 3 ---

            for child_product_type_link in child_product_type_links:
                child_product_type = child_product_types[child_product_type_links.index(
                    child_product_type_link)]
                print("    " + colored(child_product_type.name,
                                       "magenta") + " - " + child_product_type_link)
            print("")
        except:
            child_product_type_elements = driver.find_element_by_class_name(
                "b-module.b-list.b-categorynavigations.b-display--landscape").find_elements_by_class_name("b-textlink.b-textlink--sibling")

            # TODO: Getting Children Product Type links and sorting links according to Children Product Types

            child_product_types = ProductType.objects.filter(parent_product_type=parent_product_types[parent_product_type_links.index(
                parent_product_type_link)].name)

            child_product_type_links = [children_product_type_element.get_attribute(
                'href') for children_product_type in child_product_types for children_product_type_element in child_product_type_elements if children_product_type.name == children_product_type_element.text]

            # --- Output 3 ---

            for child_product_type_link in child_product_type_links:
                child_product_type = child_product_types[child_product_type_links.index(
                    child_product_type_link)]
                print("    " + colored(child_product_type.name,
                                       "magenta") + " - " + child_product_type_link)
            print("")

        # TODO: Going to each link

        for child_product_type_link in child_product_type_links:

            print("    " + colored(child_product_types[child_product_type_links.index(
                child_product_type_link)].name, "cyan"))

            driver.get(child_product_type_link)

            # TODO: Getting and clicking on see all button
            try:

                see_all_btn = driver.find_element_by_xpath(
                    '//*[@id="s0-16-13_2-0-1[1]-0-6-0-0[0]-2[0]_1-3"]/button')
                see_all_btn.click()

                # TODO: Wait and get all filter categories

                filter_categories = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "x-overlay-aspect"))
                )

                excluded_filter_categories = ["Condition", "Price", "Buying Format",
                                              "Item Location", "Delivery Options", "Show only", "Seller"]

                included_filter_categories = [
                    filter_category for filter_category in filter_categories if filter_category.text not in excluded_filter_categories]

                # TODO: Loop through all categories

                for included_filter_category in included_filter_categories:

                    print(
                        colored(f"        {included_filter_category.text}", "cyan"))

                    included_filter_category.click()

                    # TODO: Getting all filters

                    filters = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located(
                            (By.CLASS_NAME, "x-refine__multi-select.x-overlay-sub-panel__aspect-option"))
                    )

                    for filter in filters:
                        child_product_type = child_product_types[child_product_type_links.index(
                            child_product_type_link)]
                        if len(Filter.objects.filter(name=filter.text, filter_category=included_filter_category.text, product_type=child_product_type)) == 0:
                            Filter.objects.create(
                                name=filter.text, filter_category=included_filter_category.text, product_type=child_product_type)
                            print(f"            - {filter.text}")
                        else:
                            print(colored(
                                f"            - {filter.text} may have been added already", "red"))

                    print("")
            except:
                continue

    driver.quit()
