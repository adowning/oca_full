import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-account-financial-tools",
    description="Meta package for oca-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_balance_line',
        'odoo12-addon-account_chart_update',
        'odoo12-addon-account_check_deposit',
        'odoo12-addon-account_fiscal_year',
        'odoo12-addon-account_move_fiscal_year',
        'odoo12-addon-account_renumber',
        'odoo12-addon-account_type_menu',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
