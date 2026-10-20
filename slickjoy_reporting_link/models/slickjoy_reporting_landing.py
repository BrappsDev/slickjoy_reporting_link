# -*- coding: utf-8 -*-
from odoo import fields, models

SIGNUP_URL = "https://reporting.slickjoy.com/signup"
LOGIN_URL = "https://reporting.slickjoy.com/login"


class SlickjoyReportingLanding(models.Model):
    _name = "slickjoy.reporting.landing"
    _description = "SlickJoy Reporting landing page"

    name = fields.Char(default="SlickJoy Reporting", readonly=True)

    def action_get_started(self):
        return {"type": "ir.actions.act_url", "url": SIGNUP_URL, "target": "new"}

    def action_sign_in(self):
        return {"type": "ir.actions.act_url", "url": LOGIN_URL, "target": "new"}
