# SU Tech Backend Scripts

This repository contains Python scripts created for backend projects in the AUC SU Technology and Innovation team (2024-2025). Each script serves a specific function to streamline tasks and improve backend operations.

## Table of Contents

- [Scripts](#scripts)
- [Usage](#usage)
- [Contributing](#contributing)

## Scripts

### SU Packs Python Scripts

- **filter_keyword_orders.py**  
  Filters emails of users who ordered items containing a specific keyword (e.g., "case") and lists the matching items in a CSV file.
- **clean_orders_csv.py**  
  Removes duplicate customer entries from an order CSV file based on unique identifiers (email, name, phone number), saves the cleaned data into a new CSV file, and ensures that the database is updated by removing corresponding duplicate records.


### Usage

To use any of these scripts, clone the repository and run the desired script using Python:

```bash
git clone https://github.com/yomnahisham/SU-Tech-Backend-Scripts.git
cd SU-Tech-Backend-Scripts
python3 path/to/script_name.py
```

## Contributing
I welcome contributions! If you’d like to add a new script or improve an existing one, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.


