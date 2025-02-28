# -*- coding: utf-8 -*-
{
    'name': "quan_ly_khach_hang",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "minhvu",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/chi_tiet_don_hang.xml',
        'views/chi_tiet_san_pham.xml',
        'views/thong_tin_khach_hang.xml',
        'views/lich_su_giao_dich.xml',
        'views/ho_tro_khach_hang.xml',
        'views/chuc_vu.xml',
        'views/nhan_vien.xml',
        'views/phong_ban.xml',
        'views/lich_su.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
