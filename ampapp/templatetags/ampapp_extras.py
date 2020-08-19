from django import template
register = template.Library()

@register.filter
def addstr(user_id, answer_id):
    return str(user_id) + "/" + str(answer_id)