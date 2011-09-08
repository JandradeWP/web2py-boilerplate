# coding: utf8

"""
    Settings 
    Author  :   Alvaro Lizama Molina <me@alvarolizama.net>
        
    Copyright (c) 2011, Alvaro Lizama Molina.
"""

from gluon.tools import Auth, Crud, Mail


##################################################
### Database config
##################################################
if not request.env.web2py_runtime_gae:     
    db = DAL('sqlite://storage.sqlite') 
else:
    db = DAL('google:datastore') 
    session.connect(request, response, db = db) 


##################################################
### Generic views
##################################################    
response.generic_patterns = ['*'] if request.is_local else []


##################################################
### Application data
##################################################
response.title = 'Base'
response.subtitle = 'web2py base app'
response.meta.author = 'Alvaro Lizama Molina'
response.meta.email = 'me@alvarolizama.net'
response.meta.description = ''
response.meta.keywords = ''
response.meta.copyright = 'Copyright 2011' 


##################################################
### Mail settings
##################################################
mail = Mail()      
mail.settings.server = 'logging' #'smtp.gmail.com:587'  
#mail.settings.sender = 'nekrox@gmail.com'         
#mail.settings.login = 'username:password'     


##################################################
### Auth settings
##################################################
auth = Auth(db,hmac_key=Auth.get_or_create_key()) 
auth.define_tables()                           
auth.settings.mailer = mail                    
auth.settings.create_user_groups = False
auth.settings.formstyle = 'divs'
auth.settings.remember_me_form = False


##################################################
### CRUD settings
##################################################
crud = Crud(globals(),db)                      
crud.settings.auth = None
crud.settings.formstyle = 'divs'
