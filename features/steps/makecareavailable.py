from behave import given, when, then, step
from test.factories.user import UserFactory
from behave_django.decorators import fixtures
from selenium.common.exceptions import NoSuchElementException

# -------------------------- Make available --------------


@fixtures('cars.json')
@given('I am on the home page with sold car and logged in')
def step_impl(context):
    br = context.browser
    # create user
    u = UserFactory(username='mike@example.org', email='mike@example.org',
                    is_superuser=True, is_staff=True, is_active=True)
    u.set_password('mikeymike123')
    u.save()
    # logged in user
    br.get(context.base_url + '/login/')
    br.find_element_by_name('username').send_keys('mike@example.org')
    br.find_element_by_name('password').send_keys('mikeymike123')
    br.find_element_by_name('submit').click()
    # buy car
    br.get(context.base_url + '/22/buy/')
    br.find_element_by_name('buyer_name').send_keys('Stive')
    br.find_element_by_name('buyer_contact').send_keys('8569565475')
    br.find_element_by_name('buycar_submit').click()
    br.get(context.base_url + '/')


@when('I click "Make available"')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('22').get_attribute(
        'value') == 'Make available'
    br.find_element_by_id('22').click()


@then('the car should appear as available for sale again')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('22').get_attribute(
        'value') != 'Make available'
    assert br.find_element_by_id('22').get_attribute('value') == 'Buy'

# -------------------------- END Make available --------------
# -------------------------- Not logged in cant make available --------------


@fixtures('cars.json')
@given('I am on the home page with sold car and not logged in')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')
    context.data = {'id':'20'}


@then('there should not be a make available button')
def step_impl(context):
    br = context.browser
    try:
        assert br.find_element_by_id(context.data.get('id')).get_attribute('value') != 'Make available'
    except NoSuchElementException:
        assert True

# -------------------------- END Not logged in cant make available --------------
# -------------------------- available cars dont have button --------------


@fixtures('cars.json')
@given('I am on the home page with unsold car and logged in')
def step_impl(context):
    br = context.browser
    # create user
    u = UserFactory(username='mike@example.org', email='mike@example.org',
                    is_superuser=True, is_staff=True, is_active=True)
    u.set_password('mikeymike123')
    u.save()
    # logged in user
    br.get(context.base_url + '/login/')
    br.find_element_by_name('username').send_keys('mike@example.org')
    br.find_element_by_name('password').send_keys('mikeymike123')
    br.find_element_by_name('submit').click()
    context.data = {'id':'22'}


# @then('there should not be a make available button')
# def step_impl(context):

#     br = context.browser
#     assert br.find_element_by_id('22').get_attribute(
#         'value') != 'Make available'
#     assert br.find_element_by_id('22').get_attribute('value') == 'Buy'

# -------------------------- END available cars dont have button --------------
