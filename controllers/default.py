# -*- coding: utf-8 -*-

"""
    Boilerplate default controller 
    Author  :   Alvaro Lizama Molina <me@alvarolizama.net>
        
    Copyright (c) 2011, Alvaro Lizama Molina.
"""

##################################################
### Default controller
##################################################


def index():
    """
    Default action  http://..../[app]/default/index
    Render views/default/index.html or views/generic.html
    on views/layout.html
    """

    message = T('Hello World')

    return dict(message=message)


def user():
    """
    Render the auth system:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """

    form = auth()

    return dict(form=form)


def download():
    """
    Allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)

