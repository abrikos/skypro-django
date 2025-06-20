def main_menu_f(request):
    """Define main menu links for context"""
    return {"main_menu":[
        {'route':'/', 'title':'Home'},
        {'route':'catalog_list', 'title':'Catalog'},
        {'route':'blog_posts', 'title':'Blog'},
        {'route':'about', 'title':'About'},
        {'route':'contacts', 'title':'Contacts'},
    ]}