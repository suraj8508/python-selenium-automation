from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ADD_CART_BTN = (By.CSS_SELECTOR, 'input#add-to-cart-button[name="submit.add-to-cart"]')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon Product {product_id} page')
def open_prod_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when('Click on add to Cart button')
def add_to_cart(context):
    context.driver.find_element(*ADD_CART_BTN).click()


@then('Verify User can Click over the Colors')
def verify_dress_colors(context):
    # expected_colors = ['Black Iris', 'Black', 'White']
    # expected_colors_jeans = ['Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage''Dark Indigo/Rinsed']
    expected_colors_sweat = ['Army Green', 'Black', 'Blue', 'Brown', 'Burgundy']

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    actual_colors = []

    for color in colors[:5]:
        color.click()
        # actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
        actual_colors.append(context.driver.find_element(*CURRENT_COLOR).text)
        print(f"Actual Color: ", actual_colors)

    # assert expected_colors == actual_colors, f"Expected colors {expected_colors}  but got {actual_colors}"
    # assert expected_colors_jeans == actual_colors, f"Expected colors {expected_colors_jeans}  but got {actual_colors}"
    assert expected_colors_sweat == actual_colors, f"Expected colors {expected_colors_sweat}  but got {actual_colors}"


@then('Add the product to the cart')
def cart_addition(context):
    context.app.product_page.add_to_cart()
