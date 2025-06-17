def main_menu_f(request):
    """Define main menu links for context"""
    return {"main_menu":[
        {'url':'home', 'title':'Home'},
        {'url':'about', 'title':'About'},
        {'url':'contacts', 'title':'Contacts'},
    ]}