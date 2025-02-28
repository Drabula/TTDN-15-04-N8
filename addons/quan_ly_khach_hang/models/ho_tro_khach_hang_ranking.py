from odoo import models, fields, api

class HoTroNhanVienRanking(models.Model):  # Dùng models.Model thay vì TransientModel
    _name = 'ho_tro_nhan_vien_ranking'
    _description = 'Xếp hạng nhân viên hỗ trợ'
    _auto = False  # Không tạo bảng thực tế, lấy từ SQL View

    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên", readonly=True)
    ten_nhan_vien = fields.Char(string="Tên nhân viên", readonly=True)
    so_luong_ho_tro = fields.Integer(string="Số lượng hỗ trợ", readonly=True)

    @api.model
    def init(self):
        """Tạo SQL View tự động lấy dữ liệu từ bảng hỗ trợ khách hàng"""
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW ho_tro_nhan_vien_ranking AS (
                SELECT
                    row_number() OVER () AS id,  -- ID ảo cho model
                    htnv.id AS nhan_vien_id,
                    htnv.ten AS ten_nhan_vien,
                    COUNT(hthk.id) AS so_luong_ho_tro
                FROM ho_tro_khach_hang hthk
                JOIN nhan_vien htnv ON hthk.nhan_vien_id = htnv.id
                GROUP BY htnv.id, htnv.ten
                ORDER BY COUNT(hthk.id) DESC
            )
        """)
