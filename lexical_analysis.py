def lexical_analysis(program, nb_registers):
    for line_number, line in enumerate(program):
        if line.split()[0] == "copy":
            # Check if there are 3 arguments
            if len(line.split()) != 3:
                print(
                    f"Syntax error in line {line_number+1}: {line}: 'copy' instruction requires 2 arguments"
                )
                return False
            # Unpack arguments
            _, i, j = line.split()
            # Check if arguments are registers
            if not i.startswith("r") or not j.startswith("r"):
                print(
                    f"Syntax error in line {line_number+1}: {line}: Register must start with 'r'"
                )
                return False
            # Check if registers are in range
            if int(i[1:]) > nb_registers or int(j[1:]) > nb_registers:
                print(
                    f"Error in line {line_number+1}: Only {nb_registers} registers are available"
                )
                return False
        elif line.split()[0] == "inc" or line.split()[0] == "dec":
            # Not enough arguments
            if len(line.split()) != 2:
                print(
                    f"Syntax error in line {line_number+1}: {line}: 'inc' or 'dec' instruction requires 1 argument"
                )
                return False
            _, i = line.split()
            # Check if argument is a register
            if not i.startswith("r"):
                print(
                    f"Syntax error in line {line_number+1}: {line}: Register must start with 'r'"
                )
                return False
        elif line.split()[0] == "jump":
            # Not enough arguments
            if len(line.split()) != 3:
                print(
                    f"Syntax error in line {line_number+1}: {line}: 'jump' instruction requires 2 arguments"
                )
                return False
            _, i, ligne = line.split()
            # Check if first argument is a register
            if not i.startswith("r"):
                return False
            # Check if second argument is a correct line number
            if not ligne.isdigit() or int(ligne) > len(program) or int(ligne) <= 0:
                print(
                    f"Syntax error in line {line_number+1}: {line}: Second argument must be a correct line number"
                )
                return False
        elif line.split()[0] == "stop":
            pass
        else:
            print(f"Syntax error in line {line_number+1}: {line}: Unknown instruction")
    return True
