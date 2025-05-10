def replace_sz_with_s_caron(input_file, output_file=None):
    # Read the contents of the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Replace all occurrences of "sz" with "š"
    new_text = text.replace('sz', 'š')
    
    # Determine where to write the result
    if output_file is None:
        output_file = input_file  # Overwrite the original file
    
    # Write the modified text back to the file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_text)

# Example usage:
# replace_sz_with_s_caron('input.txt')  # Overwrites input.txt
# replace_sz_with_s_caron('input.txt', 'output.txt')  # Writes to output.txt
