book class Book:
    def _init_(self, title: str, author: str, year: int):
        if title is None or not title.strip():
            raise ValueError("Judul tidak boleh kosong")
        if author is None or not author.strip():
            raise ValueError("Penulis tidak boleh kosong")
        if year < 2000 or year > 2100:
            raise ValueError("Tahun hanya bisa diisi dari tahun 2000 sampai 2100")

        self.title = title.strip()
        self.author = author.strip()
        self.year = year

    def _str_(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

    def _eq_(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and
                self.author == other.author and
                self.year == other.year)

    def _hash_(self) -> int:
        return hash((self.title, self.author, self.year))