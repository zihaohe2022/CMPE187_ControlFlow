import sys
import os

def add_line_numbers(input_file):
    if not os.path.isfile(input_file):
        print("File does not exist.")
        return

    name, ext = os.path.splitext(input_file)
    output_file = f"{name}_withLineNumber{ext}"

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:

        for index, line in enumerate(infile, start=1):
            outfile.write(f"{index}    {line}")

    print(f"New file created: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        filename = input("Please enter the file name: ").strip()

    add_line_numbers(filename)