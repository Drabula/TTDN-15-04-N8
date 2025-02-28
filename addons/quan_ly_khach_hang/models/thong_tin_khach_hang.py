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


    don_hang_ids = fields.One2many('chi_tiet_don_hang', 'khach_hang_id', string="Đơn hàng")

    phan_loai = fields.Selection(
        [
            ('cao', 'Tiềm năng cao'),
            ('trung_binh', 'Tiềm năng trung bình'),
            ('thap', 'Tiềm năng thấp'),
        ],
        string="Phân loại khách hàng",
        default='trung_binh'
    )

    ngay_sinh = fields.Date("Ngày sinh")
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], string="Giới tính")

    facebook = fields.Char("Facebook")
    zalo = fields.Char("Zalo")
    website = fields.Char("Website cá nhân/ công ty")

    ngay_tao = fields.Datetime("Ngày tạo", default=fields.Datetime.now)
    ngay_cap_nhat = fields.Datetime("Ngày cập nhật", default=fields.Datetime.now, readonly=True)

    so_lan_mua_hang = fields.Integer("Số lần mua hàng", compute="_compute_so_lan_mua_hang", store=True)
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('cu', 'Cũ'),
    ], string="Trạng thái khách hàng", default='moi')

    muc_do_hai_long = fields.Selection([
        ('tot', 'Tốt'),
        ('binh_thuong', 'Bình thường'),
        ('kem', 'Kém')
    ], string="Mức độ hài lòng")

    ghi_chu = fields.Text("Ghi chú")
    # nguoi_phu_trach = fields.Many2one('res.users', string="Người phụ trách")

    @api.depends('don_hang_ids')
    def _compute_so_lan_mua_hang(self):
        for record in self:
            record.so_lan_mua_hang = len(record.don_hang_ids)
