# Marvel API Python Challenge

This project demonstrates how to interact with the Marvel API to fetch character data.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Marvel API keys from [Marvel Developer Portal](https://developer.marvel.com/)

3. Replace the hardcoded keys in `marvel_client.py`:
   - Find lines 19-20 in the `_get_keys()` function
   - Replace `"your_public_key_here"` with your actual public key
   - Replace `"your_private_key_here"` with your actual private key

## Usage

### Basic test (prints 3 character names):
```bash
python3 marvel_client.py
```

### Export characters to CSV:
```python
from marvel_client import iter_all_characters
import csv

# Export to CSV
with open('characters.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'name', 'description'])
    writer.writeheader()
    
    for character in iter_all_characters(max_items=100):
        writer.writerow({
            'id': character.get('id'),
            'name': character.get('name'),
            'description': (character.get('description') or '').replace('\n', ' ').strip()
        })
```

## Files

- `marvel_client.py` - Main script with Marvel API functions
- `marvel_characters.csv` - Sample exported data (300 characters)
- `requirements.txt` - Python dependencies

## API Functions

- `get_characters()` - Fetch characters with pagination and filtering
- `iter_all_characters()` - Generator to iterate through all characters
- `get_character_comics()` - Fetch comics for a specific character