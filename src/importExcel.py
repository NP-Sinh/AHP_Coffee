from pymongo import MongoClient
from bson.decimal128 import Decimal128

client = MongoClient("mongodb+srv://opolo4847:moips103@cluster0.ikaskks.mongodb.net/")
db = client["coffeeDB"]
collection = db["Khu_Vuc"]

data = [
    {
        "khu_vuc": "Gần Chợ Bến Thành",
        "quan": "Quận 1",
        "chi_phi_thue": 50000000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 20000000,
        "dien_tich_tb": 50,
        "so_luong_quan_cafe": 200,
        "luong_khach_tb_ngay": 140,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Gần Bệnh viện Nhi Đồng 2",
        "quan": "Quận 1",
        "chi_phi_thue": 41625000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 20000000,
        "dien_tich_tb": 45,
        "so_luong_quan_cafe": 165,
        "luong_khach_tb_ngay": 125,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Phố đi bộ Nguyễn Huệ",
        "quan": "Quận 1",
        "chi_phi_thue": 61875000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 23000000,
        "dien_tich_tb": 55,
        "so_luong_quan_cafe": 250,
        "luong_khach_tb_ngay": 175,
        "quy_hoach_do_thi": "Rất cao"
    },
    {
        "khu_vuc": "Khu vực quanh Phố Lê Lợi",
        "quan": "Quận 1",
        "chi_phi_thue": 49875000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 21500000,
        "dien_tich_tb": 47.5,
        "so_luong_quan_cafe": 185,
        "luong_khach_tb_ngay": 145,
        "quy_hoach_do_thi": "Rất cao"
    },
    {
        "khu_vuc": "Khu vực Phạm Ngũ Lão",
        "quan": "Quận 1",
        "chi_phi_thue": 42000000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 21500000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 250,
        "luong_khach_tb_ngay": 175,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Khu vực Đa Kao",
        "quan": "Quận 1",
        "chi_phi_thue": 50625000,
        "mat_do_dan_cu": 55000,
        "muc_thu_nhap_tb": 23000000,
        "dien_tich_tb": 45,
        "so_luong_quan_cafe": 230,
        "luong_khach_tb_ngay": 165,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Khu vực Gần Bưu điện Trung tâm",
        "quan": "Quận 1",
        "chi_phi_thue": 57000000,
        "mat_do_dan_cu": 50000,
        "muc_thu_nhap_tb": 25000000,
        "dien_tich_tb": 47.5,
        "so_luong_quan_cafe": 215,
        "luong_khach_tb_ngay": 160,
        "quy_hoach_do_thi": "Rất cao"
    },
    {
        "khu_vuc": "Khu vực Gần Nhà hát Thành phố",
        "quan": "Quận 1",
        "chi_phi_thue": 66937500,
        "mat_do_dan_cu": 55000,
        "muc_thu_nhap_tb": 26500000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 245,
        "luong_khach_tb_ngay": 185,
        "quy_hoach_do_thi": "Rất cao"
    },
    {
        "khu_vuc": "Khu vực Ven Sông Sài Gòn",
        "quan": "Quận 1",
        "chi_phi_thue": 44625000,
        "mat_do_dan_cu": 50000,
        "muc_thu_nhap_tb": 23000000,
        "dien_tich_tb": 42.5,
        "so_luong_quan_cafe": 210,
        "luong_khach_tb_ngay": 160,
        "quy_hoach_do_thi": "Trung bình"
    },
    {
        "khu_vuc": "Gần Trường Đại học Kinh tế TP.HCM",
        "quan": "Quận 3",
        "chi_phi_thue": 30000000,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 17000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 150,
        "luong_khach_tb_ngay": 105,
        "quy_hoach_do_thi": "Rất thấp"
    },
    {
        "khu_vuc": "Gần Bệnh viện Từ Dũ",
        "quan": "Quận 3",
        "chi_phi_thue": 33750000,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 17000000,
        "dien_tich_tb": 45,
        "so_luong_quan_cafe": 125,
        "luong_khach_tb_ngay": 115,
        "quy_hoach_do_thi": "Thấp"
    },
    {
        "khu_vuc": "Đường Nam Kỳ Khởi Nghĩa",
        "quan": "Quận 3",
        "chi_phi_thue": 35062500,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 18000000,
        "dien_tich_tb": 42.5,
        "so_luong_quan_cafe": 165,
        "luong_khach_tb_ngay": 115,
        "quy_hoach_do_thi": "Trung bình"
    },
    {
        "khu_vuc": "Gần phố cổ và bến xe buýt",
        "quan": "Quận 3",
        "chi_phi_thue": 30000000,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 17000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 140,
        "luong_khach_tb_ngay": 105,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Khu vực quanh đường Võ Văn Tần",
        "quan": "Quận 3",
        "chi_phi_thue": 31400000,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 18000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 145,
        "luong_khach_tb_ngay": 110,
        "quy_hoach_do_thi": "Trung bình"
    },
    {
        "khu_vuc": "Khu vực quanh đường Trần Quang Khải",
        "quan": "Quận 3",
        "chi_phi_thue": 31800000,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 18000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 150,
        "luong_khach_tb_ngay": 113,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Khu vực quanh Công viên Lê Thị Riêng",
        "quan": "Quận 3",
        "chi_phi_thue": 32400000,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 18000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 145,
        "luong_khach_tb_ngay": 110,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Khu vực gần Phố Cổ 3",
        "quan": "Quận 3",
        "chi_phi_thue": 30400000,
        "mat_do_dan_cu": 40000,
        "muc_thu_nhap_tb": 17000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 140,
        "luong_khach_tb_ngay": 105,
        "quy_hoach_do_thi": "Trung bình"
    },
    {
        "khu_vuc": "Khu vực Phố Biển",
        "quan": "Quận 3",
        "chi_phi_thue": 31800000,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 18000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 150,
        "luong_khach_tb_ngay": 113,
        "quy_hoach_do_thi": "Trung bình"
    },
    {
        "khu_vuc": "Khu vực quanh Trung tâm Giao thông Quận 3",
        "quan": "Quận 3",
        "chi_phi_thue": 32400000,
        "mat_do_dan_cu": 41000,
        "muc_thu_nhap_tb": 18000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 145,
        "luong_khach_tb_ngay": 110,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Gần Chợ Xóm Chiếu",
        "quan": "Quận 4",
        "chi_phi_thue": 24000000,
        "mat_do_dan_cu": 42500,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 100,
        "luong_khach_tb_ngay": 90,
        "quy_hoach_do_thi": "Thấp"
    },
    {
        "khu_vuc": "Gần Trường Đại học Nguyễn Tất Thành",
        "quan": "Quận 4",
        "chi_phi_thue": 26000000,
        "mat_do_dan_cu": 42000,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 115,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "Trung bình"
    },
    {
        "khu_vuc": "Đường 30/4",
        "quan": "Quận 4",
        "chi_phi_thue": 25400000,
        "mat_do_dan_cu": 41500,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 115,
        "luong_khach_tb_ngay": 95,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Gần trung tâm mua sắm và văn phòng",
        "quan": "Quận 4",
        "chi_phi_thue": 27000000,
        "mat_do_dan_cu": 42000,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 105,
        "luong_khach_tb_ngay": 90,
        "quy_hoach_do_thi": "Rất cao"
    },
    {
        "khu_vuc": "Khu vực Ven Sông Sài Gòn",
        "quan": "Quận 4",
        "chi_phi_thue": 25400000,
        "mat_do_dan_cu": 42000,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 110,
        "luong_khach_tb_ngay": 90,
        "quy_hoach_do_thi": "Trung bình"
    },
    {
        "khu_vuc": "Khu vực quanh Đường 2/4",
        "quan": "Quận 4",
        "chi_phi_thue": 27000000,
        "mat_do_dan_cu": 42000,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 120,
        "luong_khach_tb_ngay": 98,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Khu vực gần Bến xe buýt Quận 4",
        "quan": "Quận 4",
        "chi_phi_thue": 24000000,
        "mat_do_dan_cu": 42500,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 100,
        "luong_khach_tb_ngay": 90,
        "quy_hoach_do_thi": "Thấp"
    },
    {
        "khu_vuc": "Khu vực gần Trung tâm Thương Mại nhỏ",
        "quan": "Quận 4",
        "chi_phi_thue": 26400000,
        "mat_do_dan_cu": 42000,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 105,
        "luong_khach_tb_ngay": 90,
        "quy_hoach_do_thi": "Cao"
    },
    {
        "khu_vuc": "Khu vực gần Trường học và Khu dân cư mới",
        "quan": "Quận 4",
        "chi_phi_thue": 25400000,
        "mat_do_dan_cu": 42000,
        "muc_thu_nhap_tb": 14000000,
        "dien_tich_tb": 40,
        "so_luong_quan_cafe": 100,
        "luong_khach_tb_ngay": 90,
        "quy_hoach_do_thi": "Trung bình"
    },
    {
        "khu_vuc": "Đường Nguyễn Trải",
        "quan": "Quận 5",
        "chi_phi_thue": 140000000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 10000000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 60,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Trần Hưng Đạo",
        "quan": "Quận 5",
        "chi_phi_thue": 125000000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 10000000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường An Dương Vương",
        "quan": "Quận 5",
        "chi_phi_thue": 100000000,
        "mat_do_dan_cu": 40000,
        "muc_thu_nhap_tb": 8500000,
        "dien_tich_tb": 45,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 65,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Hồng Bàng",
        "quan": "Quận 5",
        "chi_phi_thue": 105000000,
        "mat_do_dan_cu": 40000,
        "muc_thu_nhap_tb": 8500000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 80,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Nguyễn Tri Phương",
        "quan": "Quận 5",
        "chi_phi_thue": 105000000,
        "mat_do_dan_cu": 40000,
        "muc_thu_nhap_tb": 8500000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 80,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Lê Hồng Phong",
        "quan": "Quận 5",
        "chi_phi_thue": 125000000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 10000000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Trần Phú",
        "quan": "Quận 5",
        "chi_phi_thue": 90000000,
        "mat_do_dan_cu": 40000,
        "muc_thu_nhap_tb": 8500000,
        "dien_tich_tb": 45,
        "so_luong_quan_cafe": 30,
        "luong_khach_tb_ngay": 65,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Ngô Quyền",
        "quan": "Quận 5",
        "chi_phi_thue": 110000000,
        "mat_do_dan_cu": 40000,
        "muc_thu_nhap_tb": 9000000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 80,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Nguyễn Chí Thanh",
        "quan": "Quận 5",
        "chi_phi_thue": 105000000,
        "mat_do_dan_cu": 40000,
        "muc_thu_nhap_tb": 8500000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 80,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Hùng Vương",
        "quan": "Quận 5",
        "chi_phi_thue": 125000000,
        "mat_do_dan_cu": 45000,
        "muc_thu_nhap_tb": 10000000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường 3 tháng 2",
        "quan": "Quận 10",
        "chi_phi_thue": 120000000,
        "mat_do_dan_cu": 37500,
        "muc_thu_nhap_tb": 9500000,
        "dien_tich_tb": 50,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Lý Thái Tổ",
        "quan": "Quận 10",
        "chi_phi_thue": 100000000,
        "mat_do_dan_cu": 37500,
        "muc_thu_nhap_tb": 9500000,
        "dien_tich_tb": 45,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 80,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Sư Vạn Hạnh",
        "quan": "Quận 10",
        "chi_phi_thue": 135000000,
        "mat_do_dan_cu": 37500,
        "muc_thu_nhap_tb": 10000000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Cách Mạng Tháng 8 ",
        "quan": "Quận 10",
        "chi_phi_thue": 100000000,
        "mat_do_dan_cu": 37500,
        "muc_thu_nhap_tb": 9500000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 80,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Bà Hạt",
        "quan": "Quận 10",
        "chi_phi_thue": 90000000,
        "mat_do_dan_cu": 37500,
        "muc_thu_nhap_tb": 8500000,
        "dien_tich_tb": 45,
        "so_luong_quan_cafe": 30,
        "luong_khach_tb_ngay": 65,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Nguyễn Thị Minh Khai",
        "quan": "Quận 10",
        "chi_phi_thue": 125000000,
        "mat_do_dan_cu": 37500,
        "muc_thu_nhap_tb": 10000000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 80,
        "quy_hoach_do_thi": "thấp"
    },
    {
        "khu_vuc": "Đường Thành Thái ",
        "quan": "Quận 10",
        "chi_phi_thue": 105000000,
        "mat_do_dan_cu": 37500,
        "muc_thu_nhap_tb": 9000000,
        "dien_tich_tb": 52.5,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 80,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Lý Thường Kiệt",
        "quan": "Quận 10",
        "chi_phi_thue": 120000000,
        "mat_do_dan_cu": 37500,
        "muc_thu_nhap_tb": 10000000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Phan Xích Long ",
        "quan": "Quận Phú Nhuận",
        "chi_phi_thue": 200000000,
        "mat_do_dan_cu": 27500,
        "muc_thu_nhap_tb": 12500000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 65,
        "luong_khach_tb_ngay": 125,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Hoàng Văn Thụ ",
        "quan": "Quận Phú Nhuận",
        "chi_phi_thue": 140000000,
        "mat_do_dan_cu": 27500,
        "muc_thu_nhap_tb": 12500000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Nguyễn Văn Trổi ",
        "quan": "Quận Phú Nhuận",
        "chi_phi_thue": 175000000,
        "mat_do_dan_cu": 27500,
        "muc_thu_nhap_tb": 12500000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Nguyễn Kiệm ",
        "quan": "Quận Phú Nhuận",
        "chi_phi_thue": 140000000,
        "mat_do_dan_cu": 27500,
        "muc_thu_nhap_tb": 12500000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Đặng Văn Ngữ ",
        "quan": "Quận Phú Nhuận",
        "chi_phi_thue": 125000000,
        "mat_do_dan_cu": 27500,
        "muc_thu_nhap_tb": 12500000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "trung bình"
    },
    {
        "khu_vuc": "Đường Trần Huy Liệu",
        "quan": "Quận Phú Nhuận",
        "chi_phi_thue": 140000000,
        "mat_do_dan_cu": 27500,
        "muc_thu_nhap_tb": 12500000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "thấp"
    },
    {
        "khu_vuc": "Đường Phổ Quang",
        "quan": "Quận Phú Nhuận",
        "chi_phi_thue": 155000000,
        "mat_do_dan_cu": 27500,
        "muc_thu_nhap_tb": 12500000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 50,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "cao"
    },
    {
        "khu_vuc": "Đường Lê Văn Sỹ",
        "quan": "Quận Phú Nhuận",
        "chi_phi_thue": 140000000,
        "mat_do_dan_cu": 27500,
        "muc_thu_nhap_tb": 12500000,
        "dien_tich_tb": 65,
        "so_luong_quan_cafe": 40,
        "luong_khach_tb_ngay": 100,
        "quy_hoach_do_thi": "trung bình"
    }
]

def convert_data(doc):
    doc["chi_phi_thue"] = Decimal128(str(doc["chi_phi_thue"]))
    doc["muc_thu_nhap_tb"] = Decimal128(str(doc["muc_thu_nhap_tb"]))
    doc["dien_tich_tb"] = float(str(doc["dien_tich_tb"]))
    return doc

data_converted = [convert_data(doc) for doc in data]

collection.insert_many(data)
print("Thành công!")
