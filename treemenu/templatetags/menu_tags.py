from django import template
from treemenu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(name=menu_name).order_by('id')
    menu = []
    for item in menu_items:
        children = item.children.all().order_by('id')
        is_current = item.url == current_url
        menu.append({'name': item.name, 'url': item.url,
                    'children': children, 'is_current': is_current})
    return template.loader.render_to_string('menu.html', {'menu': menu})
