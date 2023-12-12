def print_full_name(first, last):
    # Write your code here
    if (len(first) <= 10 and len(last) <= 10):
        name = " ".join([first, last])
    else:
        print("Length of names must not be greater than 10")  
    welcome = "Hello " + name + "! You just delved into python."
    print(welcome)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)