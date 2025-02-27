from odoo import models, fields, api

class LichSuGiaoDich(models.Model):
    _name = 'lich_su_giao_dich'
    _description = 'Lịch sử giao dịch khách hàng'
    _rec_name = 'ten_khach_hang'

    ten_khach_hang = fields.Many2one('thong_tin_khach_hang',string='Tên khách hàng', required=True)

    phuong_thuc_lien_lac = fields.Selection([
        ('call', 'Gọi điện'),
        ('email', 'Email'),
        ('meeting', 'Gặp mặt'),
        ('contract', 'Hợp đồng')
    ], string="Loại giao dịch", required=True)
    ngay_giao_dich = fields.Datetime(string="Ngày giao dịch", default=fields.Datetime.now)
    mo_ta_chi_tiet = fields.Text(string="Mô tả chi tiết")
    # nhan_vien_phu_trach_khach_hang = fields.Char("Nhân viên phụ trách")
    nhan_vien_phu_trach_khach_hang = fields.Many2one('nhan_vien', string='Nhân viên phụ trách', required=True)

