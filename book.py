#book
class book:
    def __init__(self, title, writer, isbn, price, stock):
        self._title = title
        self._writer = writer
        self._isbn = isbn
        self._price = price
        self._stock = stock

    def getTitle(self):
        return self._title

    def getWriter(self):
        return self._writer

    def getIsbn(self):
        return self._isbn

    def getPrice(self):
        return self._price

    def getStock(self):
        return  self._stock

    def setWriter(self, writer):
        self._writer = writer

    def setTitle(self, title):
        self._title = title

    def setPrice(self, price):
        self._price = price

    def setIsbn(self, isbn):
        self._isbn = isbn

    def setStock(self, stock):
        self._stock = stock

    def printBookDetail(self):
        print(f"""
            Judul Buku      : {self._title}
            Penulis Buku    : {self._writer}
            ISBN            : {self._isbn}
            Harga Buku      : {self._price}
            Sisa stok       : {self._stock}
        """)