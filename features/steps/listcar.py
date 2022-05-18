from behave import given, when, then, step
from test.factories.user import UserFactory
from behave_django.decorators import fixtures


# -------------------------- Scenario I am on the home page --------------
@fixtures('cars.json')
@given('I am on the home page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')


@when('I click the List Car button')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('listcar').click()


@then('I should be shown the form')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_xpath(
        '//label[@for="id_seller_name"]/parent::p').text == "Seller name:"
    assert br.find_element_by_xpath(
        '//label[@for="id_seller_mob"]/parent::p').text == "Seller mob:"
    assert br.find_element_by_xpath(
        '//label[@for="id_make"]/parent::p').text == "Make:"
    assert br.find_element_by_xpath(
        '//label[@for="id_model"]/parent::p').text == "Model:"
    assert br.find_element_by_xpath(
        '//label[@for="id_year"]/parent::p').text == "Year:"
    # assert br.find_element_by_xpath(
    #     '//label[@for="id_condition"]/parent::p').text == "Condition:"
    assert br.find_element_by_xpath(
        '//label[@for="id_price"]/parent::p').text == "Price:"

# -------------------------- END Scenario I am on the home page --------------

# -------------------------- List a car --------------


@step('I am on the list car form')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/add/')


@when('I fill the details and click submit')
def step_impl(context):
    br = context.browser
    # Fill login form and submit it (valid version)
    br.find_element_by_name('seller_name').send_keys('Mike Jonson ')
    br.find_element_by_name('seller_mob').send_keys('5689478562')
    br.find_element_by_name('make').send_keys('jeep')
    br.find_element_by_name('model').send_keys('Patriot Sport')
    br.find_element_by_name('year').send_keys('02/02/2016')
    br.find_element_by_name('condition').send_keys('good')
    br.find_element_by_name('price').send_keys('14295')
    br.find_element_by_name('listcar_submit').click()


@then('I should be shown the thankyou page')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/add/')
    success_text = br.find_element_by_css_selector('.messages').text
    assert success_text == "Form submission successful"
# -------------------------- END List a car --------------

# -------------------------- Incomplete form --------------

@step('I have filled in some if the details and click submit')
def step_impl(context):

    context.execute_steps('''When I am on the list car form''')

    br = context.browser

    # Fill login form and submit it (valid version)
    br.find_element_by_name('seller_name').send_keys('Mike Jonson')
    br.find_element_by_name('seller_mob').send_keys('5689478562')
    br.find_element_by_name('make').send_keys('jeep')
    br.find_element_by_name('model').send_keys('Patriot Sport')
    br.find_element_by_name('year').send_keys('02/02/2016')
    br.find_element_by_name('condition').send_keys('good')
    br.find_element_by_name('price').send_keys('589614295')  # invalid input
    br.find_element_by_name('listcar_submit').click()


@then('the form should show an error and the parts of the form that are missing or incorrect should be highlighted')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/add/')

    ul_error_list = br.find_element_by_css_selector('.errorlist')
    items = ul_error_list.find_elements_by_tag_name("li")
    assert items[0].text == "Ensure this value is less than or equal to 100000."
    error_field = br.find_element_by_css_selector('.error').text
    # assert success_text != "Form submission successful"
# -------------------------- END Incomplete form --------------


# @when('I add car details')
# def step_impl(context):
#     br = context.browser
#     br.get(context.base_url + '/')

#     # Checks for Cross-Site Request Forgery protection input
#     br.find_element_by_id('listcar').click()

#     # Fill login form and submit it (valid version)
#     br.find_element_by_name('seller_name').send_keys('Mike Jonson ')
#     br.find_element_by_name('seller_mob').send_keys('5689478562')
#     br.find_element_by_name('make').send_keys('jeep')
#     br.find_element_by_name('model').send_keys('Patriot Sport')
#     br.find_element_by_name('year').send_keys('02/02/2016')
#     br.find_element_by_name('condition').send_keys('good')
#     br.find_element_by_name('price').send_keys('14295')

#     # br.find_element_by_name('password').send_keys('mikeymike123')
#     br.find_element_by_name("listcar_submit").click()
#     # br.find_element_by_xpath("//input[@type='submit']").click()


# @then('I am redirected to the car added success page')
# def step_impl(context):
#     br = context.browser
#     assert br.current_url.endswith('/add/')
#     success_text = br.find_element_by_css_selector('.messages').text
#     assert success_text == "Form submission successful"


# @then('I can see listing on home page and buy car')
# def step_impl(context):
#     br = context.browser
#     br.get(context.base_url + '/')

#     cars = br.find_elements_by_css_selector(".cars")
#     # items = error_list.find_elements_by_tag_name("li")

#     # assert len(cars) == 1
#     br.find_element_by_xpath("//input[@type='submit' and @id=20]").click()


# @then('I can fill buyer detail form')
# def step_impl(context):
#     br = context.browser
#     # Checks redirection URL
#     current_url = br.current_url.split('?')[0]
#     assert current_url.endswith('/20/buy/')
#     br.find_element_by_name('buyer_name').send_keys('Mike Steve')
#     br.find_element_by_name('buyer_contact').send_keys('2365894585')
#     br.find_element_by_name("buycar_submit").click()


# @then('I can see thank you page')
# def step_impl(context):
#     br = context.browser
#     # Checks redirection URL
#     current_url = br.current_url.split('?')[0]
#     assert current_url.endswith('/20/buy/')
#     success_text = br.find_element_by_css_selector('.messages').text
#     assert success_text == "Iron mike will be in touch"


# @then('I can see sold on bought car')
# def step_impl(context):
#     br = context.browser
#     # Checks redirection URL
#     br.get(context.base_url + '/')

#     assert br.find_element_by_xpath(
#         '//label[@for="soldcar"]/parent::td').text == 'Sold'

# # -------------------------- Scenario change -----------------------------


# @fixtures('cars.json')
# @given('add bulk cars')
# def step_impl(context):
#     pass


# @when('I can move to next page')
# def step_impl(context):
#     br = context.browser
#     br.get(context.base_url + '/')
#     br.find_element_by_name("next_page").click()
#     assert br.find_element_by_css_selector(
#         '.current_page').text == "Page 2 of 3."


# @then('I can move back to prev page')
# def step_impl(context):
#     br = context.browser
#     br.get(context.base_url + '/')
#     br.find_element_by_name("next_page").click()
#     assert br.find_element_by_css_selector(
#         '.current_page').text == "Page 2 of 3."


# # -------------------------- Scenario change -----------------------------

# @when('I add missing/invalid car details')
# def step_impl(context):
#     br = context.browser
#     br.get(context.base_url + '/')

#     # Checks for Cross-Site Request Forgery protection input
#     br.find_element_by_id('listcar').click()

#     # Fill login form and submit it (valid version)
#     br.find_element_by_name('seller_name').send_keys('Mike Jonson ')
#     br.find_element_by_name('seller_mob').send_keys('5689478562')
#     br.find_element_by_name('make').send_keys('jeep')
#     br.find_element_by_name('year').send_keys('02/02/2016')
#     br.find_element_by_name('condition').send_keys('good')
#     br.find_element_by_name('price').send_keys('14295')

#     # br.find_element_by_name('password').send_keys('mikeymike123')
#     br.find_element_by_name("listcar_submit").click()
#     # br.find_element_by_xpath("//input[@type='submit']").click()


# @then('I am getting validation errors')
# def step_impl(context):
#     br = context.browser
#     # assert br.current_url.endswith('/add/')
#     assert br.find_element_by_css_selector(
#         '.messages').text == "Form submission successful"
