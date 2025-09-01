import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        book = Book("Algoritma", "Budi", 2022)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Matematika")
        self.assertFalse(removed)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        book1 = Book("Java Programming", "Andi", 2020)
        book2 = Book("Python Basics", "Andi", 2021)
        book3 = Book("Database Systems", "Budi", 2022)
        
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)
        
        books_by_andi = self.book_manager.find_books_by_author("Andi")
        self.assertEqual(2, len(books_by_andi))
        self.assertTrue(all(book.author == "Andi" for book in books_by_andi))

    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        book1 = Book("Book 1", "Author 1", 2020)
        book2 = Book("Book 2", "Author 2", 2021)
        
        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        
        all_books = self.book_manager.get_all_books()
        self.assertEqual(2, len(all_books))
        self.assertIn(book1, all_books)
        self.assertIn(book2, all_books)

    def test_validation_null_title(self):
        """Test validasi judul null"""
        with self.assertRaises(ValueError):
            Book(None, "Author", 2020)

    def test_validation_invalid_year(self):
        """Test validasi tahun invalid"""
        with self.assertRaises(ValueError):
            Book("Title", "Author", 1999)

if _name_ == '_main_':
    unittest.main()