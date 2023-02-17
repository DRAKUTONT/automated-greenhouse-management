from csv import DictWriter


def create_table(data: list, filename: str):
    with open(filename, 'w', newline='', encoding="utf8") as file:
        writer = DictWriter(file, fieldnames=list(data[0].keys()), delimiter=';')
        writer.writeheader()
        for row in data:
            writer.writerow(row)