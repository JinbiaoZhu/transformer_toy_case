import random
import string


def generate_strings(n, l, src, trg):
    total_tokens = 0

    with open(src, 'w') as srcFP:
        with open(trg, 'w') as trgFP:
            for _ in range(n):
                length = random.randint(1, l)
                random_string = ''.join(random.choices(string.ascii_letters, k=length))
                srcFP.write(random_string + '\n')
                reversed_string = random_string[::-1]
                trgFP.write(reversed_string + '\n')
                total_tokens += len(random_string)

    print(f"Generated {n} strings with total {total_tokens} tokens and saved to {src} and {trg}")
    return total_tokens


if __name__ == "__main__":
    n = 10000  # 生成的字符串数量
    l = 128  # 字符串的最大长度
    src = "src_string.txt"
    trg = "trg_string.txt"

    total_tokens = generate_strings(n, l, src, trg)
