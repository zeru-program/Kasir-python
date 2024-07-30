# let's create a kasir 
import time
import random
from datetime import datetime

welcome1 = "Welcome to zekasir!"

print(welcome1.center(65))
print('')

p0 = [0, "roti aoka", 2000]
p1 = [1, "teh gelas", 1500]
p2 = [2, "kopi kapal api", 5000]
p3 = [3, "mie instan indomie", 2500]
p4 = [4, "keripik singkong", 1000]
p5 = [5, "biskuit roma", 3000]
p6 = [6, "susu ultra", 6000]
p7 = [7, "kecap bango", 7000]
p8 = [8, "saus abc", 5000]
p9 = [9, "minyak goreng bimoli", 15000]
p10 = [10, "gula pasir gulaku", 13000]
p11 = [11, "beras rojolele", 12000]
p12 = [12, "telur ayam negeri", 1500]
p13 = [13, "ayam potong", 40000]
p14 = [14, "ikan teri medan", 20000]
p15 = [15, "daging sapi", 90000]
p16 = [16, "sayur bayam", 3000]
p17 = [17, "sayur kangkung", 2000]
p18 = [18, "tempe", 3000]
p19 = [19, "tahu", 2500]
p20 = [20, "buah jeruk", 8000]
p21 = [21, "buah apel", 15000]
p22 = [22, "buah pisang", 10000]
p23 = [23, "buah mangga", 12000]
p24 = [24, "buah pepaya", 5000]
p25 = [25, "jus buah buavita", 8000]
p26 = [26, "air mineral aqua", 3000]
p27 = [27, "minuman isotonik pocari sweat", 7000]
p28 = [28, "snack chitato", 8000]
p29 = [29, "snack taro", 6000]
p30 = [30, "snack anak mas", 2000]
p31 = [31, "permen kopiko", 3000]
p32 = [32, "permen kiss", 2000]
p33 = [33, "coklat silverqueen", 15000]
p34 = [34, "coklat delfi", 10000]
p35 = [35, "es krim walls", 12000]
p36 = [36, "roti sari roti", 8000]
p37 = [37, "sari kelapa", 5000]
p38 = [38, "es teh manis", 4000]
p39 = [39, "kopi hitam abc", 4000]
p40 = [40, "kopi luwak white koffie", 5000]
p41 = [41, "kopi good day", 3500]
p42 = [42, "minuman berenergi kratingdaeng", 8000]
p43 = [43, "susu kental manis frisian flag", 10000]
p44 = [44, "minuman ringan fanta", 6000]
p45 = [45, "minuman ringan sprite", 6000]
p46 = [46, "minuman ringan coca-cola", 6000]
p47 = [47, "yoghurt cimory", 12000]
p48 = [48, "teh botol sosro", 5000]
p49 = [49, "minuman sari kacang hijau", 4000]
p50 = [50, "minuman sari buah", 7000]

all_products = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45, p46, p47, p48, p49, p50]

def findCode(code):
    for product in all_products:
        if product[0] == code:
            return product
    return None

def sumPrices(input_string):
    codes = input_string.split('+')
    total_price = 0
    produkOutputs = []
    
    for code in codes:
        product = findCode(int(code))
        if product is not None:
            total_price += product[2]
            produkOutputs.append(product)
        else:
            print(f"Product with code {code} not found.")
    
    return total_price, produkOutputs

# Menampilkan daftar produk yang tersedia
print("Jika ada barang lain yang ingin ditambah silakan gunakan operator '+' untuk saling menambahkan barang antar barang, hasil dihitung oleh sistem, operator tidak bisa '-' 'x' maupun sejenis nya.")
print("Silahkan masukan kode produk yang tersedia berikut ini:")
for product in all_products:
    kode, nama, harga = product 
    print(f" {kode} {nama} Rp{harga}")

print('')
iptBarang = input('Masukan input kode barang: ')
total_price, products = sumPrices(iptBarang)

if products:
    print(f"Total belanja: Rp{total_price}")
    confirmOrder = input("Confirm order? (y/n): ")
    if confirmOrder == "" or confirmOrder == "y":
        iptMoneyUser = int(input(" Masukan nominal uang pembeli : Rp"))
        if iptMoneyUser < total_price:
            print(' Uang tidak cukup!')
            exit()
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        codePay = random.randint(0, 1000000000)
        print("""
=====================================
              ZeruKasir
       https://zerupgmm.web.app
              @zerr.ace
=====================================
       """)
        print(f" {current_time}")
        print("          STRUK PEMBAYARAN   ")
        print(f" Kode pembayaran : {codePay}")
        print(f"""
=====================================
        """)
        for x in products:
            print(f" {x[0]} {x[1]} {x[2]}")
        print(f"""
 Total Harga    :       Rp{total_price}
 Uang pembeli   :       Rp{iptMoneyUser}
 Uang kembalian :       Rp{total_price - iptMoneyUser}
 
=====================================
   Terima kasih sudah berbelanja!
    Kritik dan saran di website
     https://zerupgmm.web.app
    kode pembayaran : {codePay}
        {current_time}
=====================================
        """)
    else:
        print('Order dibatalkan.')
else:
    print("Produk tidak ditemukan.")
