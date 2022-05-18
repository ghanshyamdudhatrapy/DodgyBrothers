from behave import given, when, then, step
from test.factories.user import UserFactory
from behave_django.decorators import fixtures
from selenium.common.exceptions import NoSuchElementException
# -------------------------- List cars --------------


@then('I should see a list of the most recently listed cars')
def step_impl(context):
    context.execute_steps('''Given I am on the home page''')
    br = context.browser
    assert br.current_url.endswith('/')
    cars = br.find_elements_by_xpath('//table[starts-with(@class, "car-")]')
    car_ids = []
    for car_element in cars:
        car_ids.append(int(car_element.get_attribute("class").split('-')[1]))
    reverse_car_ids = [22, 21, 20, 19, 18, 17, 16, 15, 14, 13]

    assert car_ids == reverse_car_ids
# -------------------------- END List cars --------------

# -------------------------- Filter list --------------


@fixtures('cars.json')
@when('I apply a make or year filter')
def step_impl(context):
    context.execute_steps('''Given I am on the home page''')
    br = context.browser
    assert br.current_url.endswith('/')
    br.find_element_by_name('make').send_keys('Ford')
    br.find_element_by_name('year').send_keys('2022')
    br.find_element_by_name('apply_filter').click()


@then('only matching car should be shown')
def step_impl(context):
    br = context.browser

    cars_elements = br.find_elements_by_class_name("cars")
    cars = br.find_elements_by_xpath('//table')
    for car in cars:
        assert car.find_element_by_name('make').text == "Ford"
        assert car.find_element_by_name('year').text.split(" ")[-1] == "2022"
# -------------------------- END Filter list --------------

# -------------------------- Filter List - no result --------------


@fixtures('cars.json')
@given('I am on the home page with filtered result')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')
    br.find_element_by_name('make').send_keys('Ford')
    br.find_element_by_name('year').send_keys('2020')
    br.find_element_by_name('apply_filter').click()


@when('There are no match')
def step_impl(context):
    br = context.browser
    # assert br.current_url.endswith('/')
    cars_elements = br.find_elements_by_class_name("cars")
    assert False if len(cars_elements) else True


@then('I should see a message showing "No results found for your filter"')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_css_selector(
        '.result-not-found').text == "No result found for your filter"

# -------------------------- END Filter List - no result --------------
# -------------------------- Pagination --------------


@fixtures('cars.json')
@given('I am on the home page and there are no more than 10 results')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')
    cars = br.find_elements_by_xpath('//table[starts-with(@class, "car-")]')
    assert len(cars) == 10


@when('I click on page number')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('next_page').click()


@then('I should be taken to that page and the pagination bar should reflect this')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_class_name(
        "current_page").text == "Page 2 of 3."
    assert br.find_element_by_name('prev_page').text == "previous"
    # assert br.current_url.endswith('/')
# -------------------------- END Pagination --------------
