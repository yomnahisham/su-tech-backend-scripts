import csv
import os

def filter_emails_with_items(input_file):
    # Generate the output file path by appending "_filtered" to the input file name
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_filtered{ext}"
    
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        
        # Write header for the new CSVs
        writer.writerow(["email", "ordered_items"])
        
        for row in reader:
            ordered_items = []
            
            # Check all item columns for "case"
            for key, value in row.items():
                if key.startswith("item_") and "case" in value.lower():
                    ordered_items.append(value)
            
            if ordered_items:
                # Write the email and the items they ordered
                writer.writerow([row["email"], ", ".join(ordered_items)])

    print(f"Filtered emails with ordered items saved to: {output_file}")

if __name__ == "__main__":
    input_csv = "test2.csv" # Specify your actual input file location here
    
    filter_emails_with_items(input_csv)
