# Author: Tarik Rajper
# Assignment: Project #4
# Date (Last Revised): 11/06/2018

import matplotlib.pyplot as plt

# Prompts user to enter a file name
def prompt_user():
    while True:
        prompt = input('Enter File Name: ')
        try:
            file_name = open(prompt, 'r').readlines()
        except FileNotFoundError:
            print('File Not Found or Wrong File')
        else:
            break
    return file_name

# Reads data from file and inputs all floats into a list
def read_data(data):
    my_data = []

    for i in range(len(data)):
        i = float(i)

        if isinstance(i, float):
            my_data.append(i)
        else:
            raise TypeError('Invalid Data Type')
       
    return my_data

# multiplies all values in the list by 100 and writes and saves it to a file
def write_save_data(data):
    my_file = open("P4out.txt", 'w')
    for i in range(len(data)):
        i = i * 100.0
        my_file.write(str(i) + ' ')
    my_file.close()
    return my_file

# Plots data onto a graph
def plot_data(data):
    years = []
    for i in range(1840, 2020):
        years.append(i)
    plt.xlabel('Years')
    plt.ylabel('Temperature Anomaly (Celsius)')
    plt.bar(years, data, color="blue")
    plt.show()

# Runs program
def main():
    prompt = prompt_user()
    read = read_data(prompt)
    save_data = write_save_data(read)
    print(read)
    print(save_data)
    plot_data(read)
    

if __name__ == '__main__':
    main()
