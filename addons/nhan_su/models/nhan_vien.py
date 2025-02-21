from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    
    lich_su_cong_tac_ids = fields.One2many("lich_su_cong_tac", "nhan_vien_id",
                                       string="Danh sách lịch sử công tác")
    phong_ban_id = fields.Many2one("phong_ban", string="Phòng ban")