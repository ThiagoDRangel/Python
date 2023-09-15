import json
import csv
from collections import Counter

def retrieve_books(file):
    return json.load(file)

def write_csv_report(file, header, rows):
    with open(file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)

if __name__ == "__main__":
    with open("books.json") as file:
        books = retrieve_books(file)

    categories = [category for book in books for category in book["categories"]]
    category_counts = Counter(categories)

    total_books = len(books)
    books_percentage_rows = [
        [category, count / total_books] for category, count in category_counts.items()
    ]

    header = ["categoria", "percentagem"]
    write_csv_report("report.csv", header, books_percentage_rows)
