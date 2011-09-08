# coding: utf8

"""
    Menus
    Author  :   Alvaro Lizama Molina <me@alvarolizama.net>
        
    Copyright (c) 2011, Alvaro Lizama Molina.
"""

##################################################
### General menu
##################################################

response.menu = [
        (T('Dashboard'), True, URL('default', 'index'), []),
        (T('Dropdown'), False, None, [
            (T('Submenu'), False, None, []),
            ])
        ]
