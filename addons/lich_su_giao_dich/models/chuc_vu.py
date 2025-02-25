# -*- coding: utf-8 -*-
from odoo import fields, models

class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Chức vụ'

    ma_chuc_vu = fields.Char("Mã chức vụ", required=True)
    ten_chuc_vu = fields.Char("Tên chức vụ")
