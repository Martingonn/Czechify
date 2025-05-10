def replace_selected_digraphs(input_file, output_file=None):
    # Define possible replacements
    all_replacements = {
        'sz': 'š',
        'Sz': 'Š',
        'cz': 'č',
        'Cz': 'Č',
        'ch': 'h',
        'Ch': 'H',
        'rz': 'ż',
        'Rz': 'Ż',
        'ó': 'u',
        'Ó': 'U'
    }
    
    # Ask user which replacements to perform
    selected_replacements = {}
    print("Select which digraphs to replace:")
    print("Type 'Y' to replace, 'N' to skip, or 'ALL' to replace all remaining digraphs automatically.")

    for digraph, replacement in all_replacements.items():
        while True:
            choice = input(f"Replace '{digraph}' with '{replacement}'? (Y/N/ALL): ").strip().upper()
            if choice == 'Y':
                selected_replacements[digraph] = replacement
                break
            elif choice == 'N':
                break
            elif choice == 'ALL':
                # Add current and all remaining digraphs to replacements
                selected_replacements[digraph] = replacement
                # Add all remaining digraphs without asking further
                for d, r in all_replacements.items():
                    if d not in selected_replacements:
                        selected_replacements[d] = r
                break
            else:
                print("Invalid input. Please enter Y, N, or ALL.")
        if choice == 'ALL':
            break

    if not selected_replacements:
        print("No replacements selected. Exiting.")
        return

    # Read the contents of the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Perform selected replacements
    for old, new in selected_replacements.items():
        text = text.replace(old, new)
    
    # Determine where to write the result
    if not output_file:  # Handles None or empty string
        output_file = input_file  # Overwrite the original file
    
    # Write the modified text back to the file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print("Replacement complete!")

# Example usage:
input_file = input("Input file path: ")
output_file = input("Input output file path (leave empty for overwrite): ")
replace_selected_digraphs(input_file, output_file)
