from behave import given, when, then
from test.factories.user import UserFactory
from behave_django.decorators import fixtures

# -------------------------- View Login Form --------------


# @fixtures('cars.json')
@given('I am on home page without login')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')


@when('I click the login button')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('login').click()


@then('I should be shown the login form')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_name('submit').text == "Log In"
# -------------------------- END View Login Form --------------

# -------------------------- Login successfully --------------


# @fixtures('users.json')
@given('I am on the login form filled valid details')
def step_impl(context):
    br = context.browser
    u = UserFactory(username='mike@example.org', email='mike@example.org',
                    is_superuser=True, is_staff=True, is_active=True)
    u.set_password('mikeymike123')
    u.save()
    br.get(context.base_url + '/login/')
    br.find_element_by_name('username').send_keys('mike@example.org')
    br.find_element_by_name('password').send_keys('mikeymike123')


@when('I click on login')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('submit').click()


@then('I should be redirect to home page and login button should replace with a logout button')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/')
    assert br.find_element_by_name('logout').text == "Logout"

# -------------------------- END Login successfully --------------
# -------------------------- Login Failure --------------


# @fixtures('users.json')
@given('I am on the login form filled invalid details')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/login/')
    br.find_element_by_name('username').send_keys('mike@example.org')
    br.find_element_by_name('password').send_keys('mikeymike123')


# @when('I click on login')
# def step_impl(context):
#     br = context.browser
#     br.find_element_by_name('submit').click()


@then('I should be shown an error')
def step_impl(context):
    br = context.browser
    error_list = br.find_element_by_css_selector('.errorlist')
    items = error_list.find_elements_by_tag_name("li")

    assert items[
        0].text == "Please enter a correct username and password. Note that both fields may be case-sensitive."

# -------------------------- END Login Failure --------------
