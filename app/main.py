from app.book import Book
from app.display import BookDisplay
from app.printer import BookPrinter
from app.serializer import BookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            BookDisplay.display(method_type, book=book)
        elif cmd == "print":
            BookPrinter.print_book(method_type, book=book)
        elif cmd == "serialize":
            return BookSerializer.serialize(
                serialize_type=method_type,
                book=book
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
