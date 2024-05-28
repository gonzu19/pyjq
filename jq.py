import json
import termcolor as tc
import sys



def read_json(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def pretty_print_json(info: dict) -> None:
    print(tc.colored(text="{",color='magenta'))
    for key in info.keys():
        print(tc.colored(text=f'{key}:',color='green'))
        print(tc.colored(text=f'{info[key]}\n',color='yellow'))
    print(tc.colored(text="}",color='magenta'))

def parsing_json(json_data: dict,filtering: str) -> any:
    if filtering[0] != '.':
        return 'Invalid filtering'
    
    tokens = filtering[1:].split('.')
    if '[]' not in tokens:
        for token in tokens:
            if token in json_data.keys():
                json_data = json_data[token]
            else:
                return 'Invalid filtering'
        return json_data
    else:
        result = []
        look = False
        recursive = False
        for index,token in enumerate(tokens):
            if token == '[]':
                look = True
            else:
                if recursive:
                    result = [parsing_json(json_data=data,filtering=token) for data in result]
                elif look:
                    for key in json_data.keys():
                        aux = json_data[key]
                        result.append(aux[token])
                        recursive = True
                else:
                    json_data = json_data[token]
        return result

                    
def main() -> None:
    arguments = sys.argv
    # Read input from another command's output
    lines = sys.stdin.readlines()
    try:
        data = json.loads(''.join(lines))
    except Exception as e:
        print(tc.colored(text=f'Error: {e}',color='red'))
        sys.exit(1)
    if lines:
        if len(arguments) > 2:
            print(tc.colored(text=f'There can only be 1 argument which is the filtering',color='red'))
        elif len(arguments) == 1:
            pretty_print_json(data)
            #print(tc.colored(text=f'{data}',color='green'))
        elif len(arguments) == 2:
            print(tc.colored(text=parsing_json(data, f'{arguments[1]}'),color='yellow'))


if __name__ == '__main__': 
    main()

# !TODO allow the command to be used with stdin/ we will need a function to convert strings into json
# Formating of the outputs
# do this exercise in c


# usar for y enumerate para ver si es el último token y añadir a la lista de devolucion solo si es el ultimo