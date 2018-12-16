from fileOper import FileOper

path = "inputs/test1.txt"

input_file = FileOper(path)

print(input_file.get_bag_size())

print(input_file.get_random_list())
print(len(input_file.get_random_list()))

print(type(input_file.get_random_list()[0]))