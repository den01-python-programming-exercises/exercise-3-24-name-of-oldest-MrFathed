def main():
    #write your code below this line
    oldest_age = 0
    oldest_name = ''

    while True:
        line = input()

        if line == '':
            break

        data = line.split(',')
        name = data[0]
        age = int(data[1])

        if age > oldest_age:
            oldest_age = age
            oldest_name = name

    print("Name of the oldest: " + oldest_name)

if __name__ == '__main__':
    main()
