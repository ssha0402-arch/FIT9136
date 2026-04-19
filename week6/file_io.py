def read_image(file_name):
    table = []

    with open(file_name, "r") as file_:
        for line in file_:
            if len(table) == 28:
                break

            row = []
            for ch in line.strip()[:28]:
                if ch == "1":
                    row.append(1)
                else:
                    row.append(0)

            while len(row) < 28:
                row.append(0)

            table.append(row)

    while len(table) < 28:
        table.append([0] * 28)

    return table
     

def write_image(file_name, table):
    # Open the file for writing
    with open(file_name, "w") as file_:
        # Iterate over each row in the table
        for row in table:
            # Convert each pixel to string and build the line
            line = ""
            for pixel in row:
                line = line + str(pixel)

            # Write the line followed by a newline character
            file_.write(line + "\n")

    return 0

if __name__ == "__main__":
    image_1 = read_image("week6/faulty_image_1.txt")
    image_2 = read_image("week6/faulty_image_2.txt")

    write_image("new_image_1.txt", image_1)
    write_image("new_image_2.txt", image_2)
