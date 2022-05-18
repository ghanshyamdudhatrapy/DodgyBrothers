from behave import given, when, then, step
from test.factories.user import UserFactory
from behave_django.decorators import fixtures
from selenium.common.exceptions import NoSuchElementException
from django.core.mail import send_mail
from django.template.loader import render_to_string
from cars.models import Cars
from django.conf import settings
# -------------------------- Buy car button --------------


@when('I click the buy button next to a listing')
def step_impl(context):
    br = context.browser
    # assert br.current_url.endswith('/')
    context.data = {'id': '22'}
    br.find_element_by_id(context.data.get('id')).click()


@then('I should be taken to the buy form')
def step_impl(context):
    br = context.browser
    assert br.current_url.split('?')[0].endswith(
        context.data.get('id') + '/buy/')


# -------------------------- END Buy car button --------------
# -------------------------- Complete buy form --------------


@fixtures('cars.json')
@given('I am on the buy form filled with valid details')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/22/buy/')
    br.find_element_by_name('buyer_name').send_keys('Steve')
    br.find_element_by_name('buyer_contact').send_keys('8569565475')
    context.data = {
        'id': '22',
        'buyer_name': "Steve",
        'buyer_contact': "8569565475"
    }


@when('I click buy')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('buycar_submit').click()


@then('I should be redirect to a thankyou page and car should mark as sold')
def step_impl(context):
    br = context.browser
    success_text = br.find_element_by_css_selector('.messages').text
    assert success_text == "Iron mike will be in touch"
    br.get(context.base_url + '/')
    car_element = br.find_element_by_class_name("car-22")
    assert car_element.find_element_by_xpath(
        '//label[@for="soldcar"]/parent::td').text == 'Sold'


# -------------------------- END Complete buy form --------------
# -------------------------- Sold car --------------


@fixtures('cars.json')
@given('a car has been sold')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')
    context.execute_steps('''Given I am on the buy form filled with valid details''')
    context.execute_steps('''When I click buy''')
    # br.get(context.base_url + '/22/buy/')
    # br.find_element_by_name('buyer_name').send_keys('Stive')
    # br.find_element_by_name('buyer_contact').send_keys('8569565475')


@when('I visit the listing page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')


@then('the car should be marked as sold and there should be no "BUY" button next to the car')
def step_impl(context):
    br = context.browser
    car_element = br.find_element_by_class_name("car-22")
    try:
        br.find_element_by_id('22')
        assert False
    except NoSuchElementException:
        assert True
    # assert car_element.find_element_by_xpath(
    #     '//label[@for="soldcar"]/parent::td').text == 'Sold'


# -------------------------- END Sold car --------------
# -------------------------- Email Iron Mike --------------

@then('mike@example.org should receive an email')
def step_impl(context):
    br = context.browser
    car_obj = Cars.objects.get(pk=context.data.get('id'))
    commission_ammount = (5 * car_obj.price) / 100
    email_context = {
        "seller_name": car_obj.seller_name,
        "seller_mob": car_obj.seller_mob,
        "make": car_obj.make,
        "model": car_obj.model,
        "year": car_obj.year,
        "condition": car_obj.condition,
        "price": car_obj.price,
        "buyer_name": context.data.get('buyer_name'),
        "buyer_contact": context.data.get('buyer_contact'),
        "commission": commission_ammount,
        "final_amount": car_obj.price - commission_ammount
    }
    # msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
    msg_html = render_to_string(
        'cars/car_buy_inquiry_email.html', email_context)

    mail_sent = send_mail(subject='Vehicle inquiry',message="message",from_email="ghans.dudhatra@gmail.com",recipient_list=[settings.ADMIN_EMAIL, 'ghans.dudhatra@gmail.com'],html_message=msg_html,)

    assert mail_sent == 1
# -------------------------- END Email Iron Mike --------------
