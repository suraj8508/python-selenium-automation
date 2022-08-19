from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Select the Dept by alias {alias}')
def select_computers_dept(context, alias):
    context.app.HW8_all_dept_page.select_computers_dept(alias)


@when('Search for {search_word}')
def search_product(context, search_word):
    context.app.HW8_all_dept_page.search_product(search_word)


@then('Verify the {category} Dept selected')
def verify_dept_selected(context, category):
    context.app.HW8_all_dept_page.verify_dept_selected(category)
