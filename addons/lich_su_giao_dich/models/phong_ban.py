# -*- coding: utf-8 -*-
from odoo import fields, models

class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Phòng Ban'

    ma_phong_ban = fields.Char("Mã phòng ban", required=True)
    ten_phong_ban = fields.Char("Tên phòng ban")
