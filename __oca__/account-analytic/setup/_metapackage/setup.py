import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-account-analytic",
    description="Meta package for oca-account-analytic Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_analytic_parent',
        'odoo12-addon-account_analytic_sequence',
        'odoo12-addon-analytic_partner',
        'odoo12-addon-analytic_partner_hr_timesheet',
        'odoo12-addon-mrp_analytic',
        'odoo12-addon-procurement_mto_analytic',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
