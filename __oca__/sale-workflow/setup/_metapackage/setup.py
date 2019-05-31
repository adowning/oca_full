import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-sale_commercial_partner',
        'odoo12-addon-sale_double_validation',
        'odoo12-addon-sale_last_price_info',
        'odoo12-addon-sale_order_archive',
        'odoo12-addon-sale_order_line_sequence',
        'odoo12-addon-sale_order_type',
        'odoo12-addon-sale_partner_incoterm',
        'odoo12-addon-sale_product_set',
        'odoo12-addon-sale_stock_picking_blocking',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
