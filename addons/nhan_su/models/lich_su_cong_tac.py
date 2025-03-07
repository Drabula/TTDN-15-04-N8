from odoo import models, fields, api


class LichSuCongTac(models.Model):
    _name = 'lich_su_cong_tac'
    _description = 'Bảng chứa thông tin lịch sử công tác'
    
    ngay_bat_dau = fields.Date("Ngày bắt đầu")
    ngay_ket_thuc = fields.Date("Ngày kết thúc")
    nhan_vien_id = fields.Many2one(comodel_name="nhan_vien", string="Nhân viên", required=True, ondelete='cascade')
    chuc_vu_id = fields.Many2one(comodel_name="chuc_vu", string="Chức vụ", ondelete='set null')
    phong_ban_id = fields.Many2one(comodel_name="phong_ban", string="Phòng ban", required=True, ondelete='restrict')
    