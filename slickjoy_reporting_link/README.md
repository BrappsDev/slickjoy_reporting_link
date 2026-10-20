# SlickJoy Reporting (Odoo link module)

A small Odoo 19 module that adds a **SlickJoy Reporting** menu so Odoo users can
sign up for, or sign in to, [SlickJoy Reporting](https://reporting.slickjoy.com).

It is a link module. It does not connect to SlickJoy, store credentials, or send
Odoo data anywhere.

## Menu

- **SlickJoy Reporting → Get SlickJoy Reporting** opens `https://reporting.slickjoy.com/signup` in a new tab.
- **SlickJoy Reporting → Sign in** opens `https://reporting.slickjoy.com/login` in a new tab.

No user data is added to these URLs.

## Install

Copy the `slickjoy_reporting_link` folder into an Odoo addons path, restart the
server, update the app list, and install **SlickJoy Reporting**.

## License

LGPL-3. See the `license` key in `__manifest__.py`.
