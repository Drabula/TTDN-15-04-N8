from odoo import models, fields, api
from datetime import date

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ho_va_ten'

    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    ho_ten_dem = fields.Char("Họ tên đệm", required=True)
    ten = fields.Char("Tên", required=True)
    ho_va_ten = fields.Char("Họ và tên", compute='_compute_ho_ten_dem', store=True)
    tuoi = fields.Integer("Tuổi", compute="_compute_tuoi", store=True)

    @api.depends("ho_ten_dem", "ten")
    def _compute_ho_ten_dem(self):
        for vi in self:
            if vi.ho_ten_dem and vi.ten:
                vi.ho_va_ten = f"{vi.ho_ten_dem} {vi.ten}"

    @api.depends("ngay_sinh")
    def _compute_tuoi(self):
        today = date.today()
        for nv in self:
            if nv.ngay_sinh:
                nv.tuoi = today.year - nv.ngay_sinh.year - (
                    (today.month, today.day) < (nv.ngay_sinh.month, nv.ngay_sinh.day)
                )
            else:
                nv.tuoi = 0
