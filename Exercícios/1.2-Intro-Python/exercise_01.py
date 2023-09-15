def vertical_inverted_ladder(word):
    for i in range(len(word), 0, -1):
        print(word[:i])

if __name__ == "__main__":
    name = input("Digite um nome: ")
    vertical_inverted_ladder(name)
