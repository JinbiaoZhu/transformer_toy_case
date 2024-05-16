def read_from_file(filename):
    with open(filename, 'r') as file:
        with open("./src_string.txt", "w") as srcfp:
            with open("./trg_string.txt", "w") as trgfp:
                for line in file:
                    original, reversed_str = line.strip().split()
                    srcfp.write(original + '\n')
                    trgfp.write(reversed_str + '\n')
            trgfp.close()
        srcfp.close()
    file.close()

read_from_file("./strings.txt")
