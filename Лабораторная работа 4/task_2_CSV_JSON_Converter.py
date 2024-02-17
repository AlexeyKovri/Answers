# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
      # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r") as input_file:
        reader = csv.DictReader(input_file, delimiter=",", quotechar="\n")

        # TODO Сериализовать в файл с отступами равными 4

        with open(OUTPUT_FILENAME, "w") as output_file:
            list_ = []
            for row in reader:
                list_.append(row)
            json.dump(list_, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
