from django import template

register = template.Library()


@register.simple_tag
# value will pass page number, field_name pass string page and URL
def my_url(value, field_name, urlencode=None):
    url = f'?{field_name}={value}'

    if urlencode:
        querystring = urlencode.split('&')
        # take query string list, take each string and split it by 2, if the
        # first string is equel to the field.
        filtered_querystring = filter(
            lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}'

    return url
