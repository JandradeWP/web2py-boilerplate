# coding: utf8

"""
    Assets
    Author  :   Alvaro Lizama Molina <me@alvarolizama.net>
        
    Copyright (c) 2011, Alvaro Lizama Molina.
"""

##################################################
### Common CSS
##################################################
response.files.append(URL('static','css/bootstrap.css'))
response.files.append(URL('static','css/custom.css'))
response.files.append(URL('static','css/jquery.jgrowl.css'))
response.files.append(URL('static','css/jquery.poshytip.css'))


##################################################
### Common JS
##################################################
response.files.append(URL('static','js/jquery.js'))
response.files.append(URL('static','js/base.js'))
response.files.append(URL('static','js/jquery.growl.js'))
response.files.append(URL('static','js/jquery.poshytip.js'))
