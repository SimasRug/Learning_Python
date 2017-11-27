empty_str = ''
file_name = 'C:/Users/Rugeviciuss/Desktop/Python/Learning_Python/Chapter8/test.txt'
file_name_copy = 'C:/Users/Rugeviciuss/Desktop/Python/Learning_Python/Chapter8/test_copy.txt'
input_file = open(file_name,'r')
output_file = open(file_name_copy,'w')

line = input_file.readline()
output_file.write(line)

output_file.close()
