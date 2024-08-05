import sys

def generate_files(arg1, arg2):
    with open('output1.txt', 'w') as f1, open('output2.txt', 'w') as f2:
        f1.write(f'This is the content of the first file. Argument: {arg1}')
        f2.write(f'This is the content of the second file. Argument: {arg2}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_files.py <arg1> <arg2>")
        sys.exit(1)
    
    arg1, arg2 = sys.argv[1], sys.argv[2]
    generate_files(arg1, arg2)
