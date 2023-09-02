import sys
import glob

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            #print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def crate_name():
        #check all arguments is any of them is like -o=OUTPUT_FILE_NAME
    for arg in sys.argv[1:]:
        if arg.startswith("-o="):
            output_file_name = arg[3:]
            sys.argv.remove(arg)
            break
        else:
            output_file_name = "output.yaml"

    #check if the output file name ends with .yaml
    if not output_file_name.endswith(".yaml"):
        output_file_name=output_file_name+".yaml"

    return output_file_name

def check_if_verbose():
    for arg in sys.argv[1:]:
        if arg.startswith("-v"):
            sys.argv.remove(arg)
            return True
    return False

def print_help():
    print("Usage: python main.py [OPTIONS] [FILES]")
    print("Merge text files into an output YAML file.")
    print("\nOptions:")
    print("-o=OUTPUT_FILE_NAME  Specify the output YAML file name (default: output.yaml)")
    print("-v                  Enable verbose mode")
    print("-h, --help           Display this help message")
    sys.exit(0)

if __name__ == "__main__":

    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()

    if len(sys.argv) == 0:
        print("At least one argument is expected")
        sys.exit(1)

    is_verbose=check_if_verbose()
    output_file_name=crate_name()
    print(f"Output file name: ", output_file_name)

    #loop trought ars to math files with * and add them to list
    for arg in sys.argv[1:]:
        if arg.find("*") != -1:
            #use glob to math all the files in directory
            for file_path in glob.glob(arg+"*.yaml"):
                if is_verbose:
                    print(f"Found file: {file_path}")
                sys.argv.append(file_path)
            sys.argv.remove(arg)

    #check if output file exists and delete it
    try:
        with open(output_file_name, 'r+') as file:
            print(f"Output file {output_file_name} already exists.")
            exit(1)
    except FileNotFoundError:
        pass

    #create outputfile:
    with open(output_file_name, 'w') as output_file:
        output_file.write("---\n")

    for file_path in sys.argv[1:]:
        if is_verbose:
            print(f"Merging file: {file_path}")
        read_text_file(file_path)
        #append processed file to the output file
        with open(file_path, 'r') as file:
            content = file.read()
            with open(output_file_name, 'a') as output_file:
                output_file.write(content)
                output_file.write("---\n")
        