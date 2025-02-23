from odoo import models, fields, api


class ThongTinKhachHang(models.Model):
    _name = 'thong_tin_khach_hang'
    _description = 'Thông Tin Khách Hàng'
    _rec_name = 'ten_khach_hang'

    ten_khach_hang = fields.Char("Tên khách hàng", required=True)
    dia_chi = fields.Char("Địa chỉ")
    so_dien_thoai = fields.Char("Số điện thoại")
    email = fields.Char("Email")
    cong_ty = fields.Char("Công ty")
    chuc_vu = fields.Char("Chức vụ")

    don_hang_ids = fields.One2many(
        'don_hang_khach_hang', 'khach_hang_id', string="Đơn hàng"
    )

