# -*- coding: utf-8 -*-
{
    'name': "Test Product using owl",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Mohiuddin",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', "website"],

    'data': [
        'views/views.xml',
    ],
    "assets": {
        "web.assets_frontend": [
            "test_product_using_owl/static/src/components/ProductSearchPage/*",
            "test_product_using_owl/static/src/components/ProductCard/*",
        ]
     },
}
