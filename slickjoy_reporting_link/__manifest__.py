# -*- coding: utf-8 -*-
{
    "name": "SlickJoy Reporting",
    "summary": "Ask your Odoo data a question and get a live chart, with the query behind it.",
    "description": "Adds SlickJoy Reporting to your Odoo menu. SlickJoy Reporting builds live "
                   "charts and scheduled pages from your Odoo data in plain language, with "
                   "the exact read-only query behind each chart.",
    "version": "20.0.1.0.0",
    "category": "Accounting",
    "license": "LGPL-3",
    "author": "SlickJoy",
    "website": "https://reporting.slickjoy.com",
    "depends": ["base", "web"],
    "data": [
        "security/ir.access.csv",
        "views/menu.xml",
    ],
    "images": ["static/description/banner.png", "static/description/main_screenshot.png"],
    "application": True,
    "installable": True,
    "auto_install": False,
}
