import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ==========================================
# 1. NHAP 2 HAM SO VA TU DONG TIM GIAO DIEM
# ==========================================
x_sym = sp.symbols('x')

print("--- Chuong trinh tu dong tim giao diem, tinh the tich & ve do thi doi ---")
print("Luu y nhap dung dinh dang Python (Vi du: x**2, 2*x, sqrt(x), sin(x),...)")
print("-" * 75)

try:
    # Nhap hai ham so tu ban phim
    chuoi_f = input("1. Nhap ham so f(x): ")
    chuoi_g = input("2. Nhap ham so g(x): ")

    # Chuyen doi sang bieu thuc SymPy
    f_sym = sp.sympify(chuoi_f)
    g_sym = sp.sympify(chuoi_g)

    # TU DONG GIAI PHUONG TRINH HOANH DO GIAO DIEM: f(x) = g(x) -> f(x) - g(x) = 0
    nghiem_all = sp.solve(f_sym - g_sym, x_sym)
    
    # Loc lay cac nghiem thuc mot cach an toan bang cach kiem tra .is_real
    giao_diem = []
    for val in nghiem_all:
        if val.is_real:  
            giao_diem.append(float(val))
    
    giao_diem = sorted(list(set(giao_diem))) # Loai bo nghiem trung va sap xep tu nho den lon

    # Kiem tra xem co du so luong giao diem de tao thanh hinh phang kin hay khong
    if len(giao_diem) < 2:
        print("\n[Loi] Hai ham so khong cat nhau tai du 2 diem de tao thanh mot hinh phang gioi han!")
        print(f"Cac giao diem tim thay: {giao_diem}")
    else:
        # Laye giao diem nho nhat lam can duoi va lon nhat lam can tren
        can_a_val = giao_diem[0]
        can_b_val = giao_diem[-1]

        # Ap dung cong thuc the tich khoi tron xoay quanh Ox gioi han boi 2 duong ham so:
        # V = pi * tich phan tu a den b cua |f^2(x) - g^2(x)| dx
        bieu_thuc_tich_phan = sp.Abs(f_sym**2 - g_sym**2)
        V_sym = sp.pi * sp.integrate(bieu_thuc_tich_phan, (x_sym, can_a_val, can_b_val))

        print("-" * 75)
        print(f"-> Tu dong tim thay {len(giao_diem)} giao diem thuc: {giao_diem}")
        print(f"-> Mien phang tinh toan gioi han trong doan tu x = {can_a_val} den x = {can_b_val}")
        print(f"-> The tich khroi tron xoay chinh xac V = {V_sym}")
        print(f"-> Gia tri xap xi so thap phan:    V ~ {float(V_sym):.4f}")
        print("-" * 75)

        # Dinh nghia lai bien khoang_cach phuoc vu ve truc toa do Ox
        khoang_cach = can_b_val - can_a_val if can_b_val != can_a_val else 1.0

        # ==========================================
        # 2. KHOI TAO KHUNG VE DO THI (CHI DU`NG 3D)
        # ==========================================
        fig = plt.figure(figsize=(9, 6))
        f_num = sp.lambdify(x_sym, f_sym, 'numpy')
        g_num = sp.lambdify(x_sym, g_sym, 'numpy')

        ax3d = fig.add_subplot(111, projection='3d')

        # Luoi toa do quay trong pham vi [a, b]
        x_vals_3d = np.linspace(can_a_val, can_b_val, 100)
        theta = np.linspace(0, 2 * np.pi, 100)
        X, Theta = np.meshgrid(x_vals_3d, theta)
# Tinh ban kinh cua hai mat cong tron xoay tai moi diem x
        R_f = np.abs(f_num(X))
        R_g = np.abs(g_num(X))

        # Phan dinh mat ngoai (ban kinh lon hon) va mat trong (ban kinh nho hon)
        R_outer = np.maximum(R_f, R_g)
        R_inner = np.minimum(R_f, R_g)

        # Dung va hien thi mat cong bao boc ben ngoai vat the
        Y_out = R_outer * np.cos(Theta)
        Z_out = R_outer * np.sin(Theta)
        surf_out = ax3d.plot_surface(X, Y_out, Z_out, cmap='plasma', alpha=0.6, edgecolor='none')

        # Dung va hien thi long loi ben trong vat the (neu co khoang trong)
        if not np.allclose(R_inner, R_outer):
            Y_in = R_inner * np.cos(Theta)
            Z_in = R_inner * np.sin(Theta)
            ax3d.plot_surface(X, Y_in, Z_in, cmap='winter', alpha=0.3, edgecolor='none')

        # Ve 2 mat phang cat chan hai dau tai cac diem giao
        ax3d.plot_surface(np.full_like(X, can_a_val), Y_out, Z_out, color='gray', alpha=0.15)
        ax3d.plot_surface(np.full_like(X, can_b_val), Y_out, Z_out, color='gray', alpha=0.15)
        ax3d.plot([can_a_val - khoang_cach*0.1, can_b_val + khoang_cach*0.1], [0, 0], [0, 0], color='black', linestyle='--', linewidth=2, label='Truc Ox')
        
        ax3d.set_title('Khoi tron xoay rong/dac 3D tao thanh', fontsize=11, fontweight='bold')

        ax3d.set_xlabel('Truc X')
        ax3d.set_ylabel('Y')
        ax3d.set_zlabel('Z')
        ax3d.legend(loc='upper left')
        
        # Can chinh can bang ty le hien thi giua cac truc 3D
        ptp_x = np.ptp(x_vals_3d)
        ptp_y = np.ptp(Y_out)
        ptp_z = np.ptp(Z_out)
        
        aspect_x = ptp_x if ptp_x > 0 else 1.0
        aspect_y = ptp_y if ptp_y > 0 else 1.0
        aspect_z = ptp_z if ptp_z > 0 else 1.0
        
        ax3d.set_box_aspect((aspect_x, aspect_y, aspect_z))

        plt.suptitle('Mo phong tu dong khoi tron xoay giao nhau giua 2 do thi quanh Ox', fontsize=13, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.show()

except Exception as e:
    print(f"\nDa xay ra loi he thong: {e}")
    print("Vui long kiem tra lai dinh dang ham so (Vi du viet dau nhan '*', dau mu '**').")