with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        for i, line in enumerate(input_file, 1):
            output_file.write(
                "{}) {}".format(i, line)
            )