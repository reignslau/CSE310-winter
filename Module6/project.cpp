#include <iostream>
#include <vector>
#include <algorithm>

class Book {
private:
    std::string title;
    std::string author;
    bool isBorrowed;

public:
    Book(std::string title, std::string author) : title(title), author(author), isBorrowed(false) {}

    std::string getTitle() const { return title; }
    std::string getAuthor() const { return author; }
    bool getIsBorrowed() const { return isBorrowed; }

    void borrowBook() { isBorrowed = true; }

    void returnBook() { isBorrowed = false; }
};

class Library {
private:
    std::vector<Book> books;

public:
    void addBook(const Book& book) { books.push_back(book); }

    void borrowBook(const std::string& title) {
        auto it = std::find_if(books.begin(), books.end(),
            [&](const Book& book) { return book.getTitle() == title && !book.getIsBorrowed(); });

        if (it != books.end()) {
            it->borrowBook();
            std::cout << "You have borrowed the book: " << title << std::endl;
        } else {
            std::cout << "Sorry, the book \"" << title << "\" is either not available or already borrowed." << std::endl;
        }
    }

    void returnBook(const std::string& title) {
        auto it = std::find_if(books.begin(), books.end(),
            [&](const Book& book) { return book.getTitle() == title && book.getIsBorrowed(); });

        if (it != books.end()) {
            it->returnBook();
            std::cout << "You have returned the book: " << title << std::endl;
        } else {
            std::cout << "Sorry, you have not borrowed the book \"" << title << "\"." << std::endl;
        }
    }

    void displayBooks() const {
        std::cout << "Books available in the library:" << std::endl;
        for (const auto& book : books) {
            std::cout << "Title: " << book.getTitle() << ", Author: " << book.getAuthor();
            if (book.getIsBorrowed())
                std::cout << " (Borrowed)";
            std::cout << std::endl;
        }
    }
};

int main() {
    Library library;

    library.addBook(Book("The Great Gatsby", "F. Scott Fitzgerald"));
    library.addBook(Book("To Kill a Mockingbird", "Harper Lee"));
    library.addBook(Book("1984", "George Orwell"));

    int choice;
    std::string title;

    do {
        std::cout << "\nLibrary Management System\n";
        std::cout << "1. Display all books\n";
        std::cout << "2. Borrow a book\n";
        std::cout << "3. Return a book\n";
        std::cout << "4. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                library.displayBooks();
                break;
            case 2:
                std::cout << "Enter the title of the book you want to borrow: ";
                std::cin.ignore();
                std::getline(std::cin, title);
                library.borrowBook(title);
                break;
            case 3:
                std::cout << "Enter the title of the book you want to return: ";
                std::cin.ignore();
                std::getline(std::cin, title);
                library.returnBook(title);
                break;
            case 4:
                std::cout << "Exiting the program.\n";
                break;
            default:
                std::cout << "Invalid choice. Please try again.\n";
                break;
        }
    } while (choice != 4);

    return 0;
}
