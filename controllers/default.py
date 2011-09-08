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

    form = SQLFORM.factory(
            Field('email',
                label='Email',
                requires=IS_EMAIL()
                ),
            Field('active', 'boolean',
                label='Active'
                ),
            Field('comment', 'text',
                label='Comments'
                ),

            Field('role', 'integer', 
                label='Rol',
                requires=IS_IN_SET({1:'Admin', 2:'User'}, zero=None)
                ),
            formstyle='divs'
            )

    form.element(_type='submit')['_class']='primary'

    if form.accepts(request.vars, session):
            response.flash = 'Saved'
    elif form.errors:
        response.flash = 'Error'

    return dict(message=message, form=form)


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
    form.element(_type='submit')['_class']='primary'
    return dict(form=form)


def download():
    """
    Allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)

