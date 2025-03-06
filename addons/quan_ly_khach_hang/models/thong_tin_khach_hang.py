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
    ho_tro_ids = fields.One2many(
        'ho_tro_khach_hang',  # Model liên kết
        'ten_khach_hang',  # Trường Many2one trong model ho_tro_khach_hang
        string="Hỗ trợ khách hàng"
    )
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

    muc_do_hai_long = fields.Selection(
        [
            ('tot', 'Tốt'),
            ('binh_thuong', 'Bình thường'),
            ('kem', 'Kém')
        ],
        string="Mức độ hài lòng",
        compute="_compute_muc_do_hai_long",
        store=True
    )

    tong_tien_chi_tieu = fields.Float("Tổng tiền đã chi tiêu", compute="_compute_tong_tien_chi_tieu", store=True)

    ghi_chu = fields.Text("Ghi chú")
    # nguoi_phu_trach = fields.Many2one('res.users', string="Người phụ trách")

    @api.depends('don_hang_ids')
    def _compute_so_lan_mua_hang(self):
        for record in self:
            record.so_lan_mua_hang = len(record.don_hang_ids)

    @api.depends('don_hang_ids.subtotal')
    def _compute_tong_tien_chi_tieu(self):
        for record in self:
            record.tong_tien_chi_tieu = sum(record.don_hang_ids.mapped('subtotal'))

    @api.depends('ho_tro_ids')
    def _compute_so_lan_ho_tro(self):
        for record in self:
            record.so_lan_ho_tro = len(record.ho_tro_ids)

    @api.depends('ho_tro_ids.diem_danh_gia')
    def _compute_muc_do_hai_long(self):
        for record in self:
            if record.ho_tro_ids:
                # Tính điểm trung bình
                tong_diem = sum(record.ho_tro_ids.mapped('diem_danh_gia'))
                diem_trung_binh = tong_diem / len(record.ho_tro_ids)
                # Xác định mức độ hài lòng
                if diem_trung_binh >= 4:
                    record.muc_do_hai_long = 'tot'
                elif diem_trung_binh >= 2:
                    record.muc_do_hai_long = 'binh_thuong'
                else:
                    record.muc_do_hai_long = 'kem'
            else:
                record.muc_do_hai_long = False
