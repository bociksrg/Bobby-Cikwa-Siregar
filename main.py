#main
from book import book
def addBuku(bookSelf, book):
    if len(bookSelf) == 0:
        bookSelf.append(book)
        return f"""Buku berhasil ditambahkan"""
    elif int(book.getStock()) < 0:
        return f"""Stock tidak boleh negatif"""
    elif int(book.getPrice()) < 0:
        return f"""Harga buku tidak boleh negatif"""
    else:
        for buku in bookSelf:
            if buku.getTitle() == book.getTitle() and buku.getWriter() == book.getWriter() and buku.getIsbn() == book.getIsbn() and int(buku.getPrice())==book.getPrice():
                buku.setStock(buku.getStock()+book.getStock())
                return f"""Buku berhasil ditambahkan"""
            else:
                continue
        bookSelf.append(book)
        return f"""Buku berhasil ditambahkan"""

def removeBook(bookSelf, bookTitle, stock):
    for buku in bookSelf:
        if buku.getTitle() == bookTitle:
            if buku.getStock()>=stock:
                buku.setStock(buku.getStock() - stock)
                return f"""berhasil mengurangi buku"""
            else:
                print(f"""Stok tersedia lebih kecil dari nilai yang hendak dikurangi""")
                return f"""Gagal mengurangi buku"""
        else:
            continue
    return "Judul Buku tidak ditemukan"

def beliBuku(bookSelf, belanja, judulBuku, stok):
    for buku in bookSelf:
        if buku.getTitle() == judulBuku:
            if buku.getStock()>=stok:
                buku.setStock(buku.getStock()-stok)
                belanja.append({'judul' :buku.getTitle(), 'totalItem': stok, 'price': buku.getPrice()})
                return "Buku masuk dalam keranjang"
            else:
                return "Maaf banyak permintaan anda lebih besar daripada stok yang tersedia"
        else:
            continue
    return "permintaan tidak bisa diproses. Buku yang anda maksud tidak ada. Cek kembali rincian permintaan anda."

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bookSelf = []
    belanja = []
    TotalHarga = 0
    addBuku(bookSelf, book("AADC", "Sil", 123456, 20000, 2))
    addBuku(bookSelf, book("AADC", "Sil", 123456, 20000, 2))
    addBuku(bookSelf, book("AADC2", "Sil", 123456, 20000, 2))
    # for book in bookSelf:
    #     book.printBookDetail()
    #
    # removeBook(bookSelf,"AADC2", 1)
    # for book in bookSelf:
    #     book.printBookDetail()
    # removeBook(bookSelf,"AADC2", 4)
    # for book in bookSelf:
    #     book.printBookDetail()
    action = 1
    try:
        while action > 0 and action <= 3:
            print(f"""
                            Selamat datang di Toko Buku Masa Depan!
                            ====================================================================================
                            Anda ingin apa?
                            ====================================================================================
                            1. Menambah buku/Mengurangi stok buku/Mengecek stok buku
                            2. Membeli buku
                            3. Keluar
                            ====================================================================================
                """)
            action = int(input())
            if action == 1:
                print(f"""
                                ====================================================================================
                                Pilih aksi yang hendak anda lakukan!
                                ====================================================================================
                                1. Menambah buku
                                2. Mengurangi stok buku
                                3. Mengecek stok buku
                                4. Kembali ke menu utama
                                5. Keluar
                                ====================================================================================
            """)
                subaction = int(input())
                if subaction == 1:
                    print("Masukkan judul buku:")
                    judul = input()
                    print("Masukkan nama penulis:")
                    penulis = input()
                    print("Masukkan ISBN")
                    ISBN = input()
                    print("Masukkan Harga buku:")
                    harga = int(input())
                    while harga < 0:
                        print("Harga buku tidak boleh negatif")
                        harga = int(input())
                    print("Masukkan stock buku")
                    stok = int(input())
                    while stok < 0:
                        print("Stok buku tidak boleh negatif")
                        stok = int(input())
                    print(addBuku(bookSelf, book(judul, penulis, ISBN, harga, stok)))
                elif subaction == 2:
                    print("Masukkan Judul buku yang ingin dihapus:")
                    judulBuku = input()
                    print("Masukkan banyak stok buku:")
                    stokBuku = int(input())
                    while stokBuku < 0:
                        print("Stok buku tidak boleh negatif")
                        stokBuku = int(input())
                    print(removeBook(bookSelf, judulBuku, stokBuku))
                elif subaction == 3:
                    i = 1
                    for buku in bookSelf:
                        print(f"""{i}. {buku.getTitle()}""")
                        buku.printBookDetail()
                        i += 1
                elif subaction == 4:
                    print(f"""
                            Selamat datang di Toko Buku Masa Depan!
                            ====================================================================================
                            Anda ingin apa?
                            ====================================================================================
                            1. Menambah buku/Mengurangi stok buku/Mengecek stok buku
                            2. Membeli buku
                            3. Keluar
                            ====================================================================================
                        """)
                    continue
                else:
                    break
            elif action == 2:
                print(f"""
                                ====================================================================================
                                Pilih aksi yang hendak anda lakukan!
                                ====================================================================================
                                1. Cek keranjang anda
                                2. Beli buku
                                3. Bayar
                                4. Kembali ke menu utama
                                5. Keluar
                                ====================================================================================
                        """)
                subaction = int(input())
                if subaction == 1:
                    if len(belanja) == 0:
                        print("Tidak ada barang dalam keranjang anda")
                    else:
                        print(f"""
                                ====================================================================================
                                List Belanja Anda
                                ====================================================================================
                        """)
                        i = 1
                        for item in belanja:
                            TotalHarga += item['price'] * item['totalItem']
                            print(f""" 
                                    {i}. {item['judul']}
                                         Harga : {item['price']}
                                         Banyak item: {item['totalItem']}   
                                ====================================================================================              
                            """)
                        print(f"""Total Harga Belanjaan: Rp.{TotalHarga}""")
                        TotalHarga = 0
                elif subaction == 2:
                    print("Masukkan Judul buku yang ingin dibeli:")
                    judulBuku = input()
                    print("Masukkan banyak buku yang ingin dibeli:")
                    stokBuku = int(input())
                    while stokBuku < 0:
                        print("Stok buku tidak boleh negatif")
                        stokBuku = int(input())
                    print(beliBuku(bookSelf, belanja, judulBuku, stokBuku))
                elif subaction == 3:
                    print(f"""Masukkan uang anda:""")
                    for item in belanja:
                        TotalHarga += item['price'] * item['totalItem']
                    while True:
                        uang = int(input())
                        if uang < TotalHarga:
                            print("Uang anda tidak cukup. Masukkan kembali:")
                        else:
                            print(f"""Transaksi berhasil. Kembalian anda : {uang - TotalHarga}""")
                            break
                    TotalHarga = 0
                    belanja = []
                    continue
                elif subaction == 4:
                    print(f"""
                                        Selamat datang di Toko Buku Masa Depan!
                                        ====================================================================================
                                        Anda ingin apa?
                                        ====================================================================================
                                        1. Menambah buku/Mengurangi stok buku/Mengecek stok buku
                                        2. Membeli buku
                                        3. Keluar
                                        ====================================================================================
                                    """)
                    continue
                else:
                    break
            else:
                break
    except:
        pass


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
