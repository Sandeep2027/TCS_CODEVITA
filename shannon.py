def evaluate_gate(gate_type, input1, input2):
    if gate_type == 'AND':
        return input1 & input2
    elif gate_type == 'OR':
        return input1 | input2
    elif gate_type == 'NAND':
        return not (input1 & input2)
    elif gate_type == 'NOR':
        return not (input1 | input2)
    elif gate_type == 'XOR':
        return input1 ^ input2

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    N = int(data[0])  # Number of gates
    gates = {}
    
    for i in range(1, N + 1):
        line = data[i].strip()
        output_gate, rest = line.split('-')
        gate_type, inputs = rest.split('(')
        inputs = inputs[:-1].split(',')  # Remove the closing parenthesis and split
        gates[output_gate.strip()] = (gate_type.strip(), [input.strip() for input in inputs])
    
    T = int(data[N + 1])  # Length of the cycles
    inputs = {}
    
    for i in range(N + 2, N + 2 + T):
        line = data[i].strip().split()
        var = line[0]
        states = list(map(int, line[1:]))
        inputs[var] = states
    
    target_gate = data[N + 2 + T].strip()
    
    # Initialize outputs for each gate
    outputs = {gate: [0] * T for gate in gates}
    
    # Process each cycle
    for cycle in range(T):
        for gate, (gate_type, input_vars) in gates.items():
            if cycle == 0:
                # Initial output is always 0
                outputs[gate][cycle] = 0
            else:
                # Get the inputs for the gate from the previous cycle
                input_values = [outputs[input_var][cycle - 1] for input_var in input_vars]
                if len(input_values) == 2:
                    input1 = input_values[0]
                    input2 = input_values[1]
                    if gate_type == 'AND':
                        outputs[gate][cycle] = evaluate_gate('AND', input1, input2)
                    elif gate_type == 'OR':
                        outputs[gate][cycle] = evaluate_gate('OR', input1, input2)
                    elif gate_type == 'NAND':
                        outputs[gate][cycle] = int(evaluate_gate('NAND', input1, input2))
                    elif gate_type == 'NOR':
                        outputs[gate][cycle] = int(evaluate_gate('NOR', input1, input2))
                    elif gate_type == 'XOR':
                        outputs[gate][cycle] = evaluate_gate('XOR', input1, input2)

    # Output the result for the target gate
    result = ''.join(map(str, outputs[target_gate]))
    print(result)

if __name__ == "__main__":
    main()