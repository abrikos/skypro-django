def main_menu_f(request):
    """Define main menu links for context"""
    menu = [
        {'route': 'home', 'title': 'Home'},
        {'route': 'catalog_list', 'title': 'Catalog'},
        {'route': 'blog_posts', 'title': 'Blog'},
        {'route': 'about', 'title': 'About'},
        {'route': 'contacts', 'title': 'Contacts'},

    ]
    if request.user.id:
        menu.append({'route': 'cabinet', 'title': request.user.email})
    else:
        menu.append({'route': 'login', 'title': 'Login'})
        menu.append({'route': 'register', 'title': 'Register'})
    return {"main_menu": menu}
