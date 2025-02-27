from odoo import models, fields, api


class HoTroKhachHang(models.Model):
    _name = 'ho_tro_khach_hang'
    _description = 'Hỗ trợ khách hàng'

    ten_khach_hang = fields.Char("Tên khách hàng", required=True)

    phuong_thuc_lien_lac = fields.Selection([
        ('call', 'Gọi điện'),
        ('email', 'Email'),
        ('chat', 'Nhắn tin'),
        ('direct', 'Gặp trực tiếp')
    ], string="Phương thức liên lạc", required=True)

    ngay_ho_tro = fields.Datetime(string="Ngày hỗ trợ", default=fields.Datetime.now)

    mo_ta_chi_tiet = fields.Text(string="Mô tả chi tiết")

    trang_thai = fields.Selection([
        ('pending', 'Đang chờ'),
        ('in_progress', 'Đang xử lý'),
        ('resolved', 'Đã giải quyết')
    ], string="Trạng thái", default='pending')

    nhan_vien_phu_trach = fields.Char("Nhân viên phụ trách")
