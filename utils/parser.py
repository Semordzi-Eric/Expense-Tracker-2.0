import re
from datetime import datetime
from utils.categorizer import auto_categorize

def parse_quick_add(user_input: str) -> dict:
    """
    Parses a single-line input like "50 food" or "120 uber ride"
    Returns a dictionary with amount, category, description, and date.
    """
    user_input = user_input.strip()
    
    # Try to extract the first occurrence of a number (amount)
    amount_match = re.search(r'\b\d+(\.\d+)?\b', user_input)
    
    if not amount_match:
        raise ValueError("Could not find an amount in the input.")
        
    amount = float(amount_match.group(0))
    
    # Remove the amount from the text to get the description
    description = user_input[:amount_match.start()] + user_input[amount_match.end():]
    description = description.strip()
    
    # If there is no description, we can't really categorize
    if not description:
        description = "Quick Add Entry"
        
    # Categorize based on the description
    category = auto_categorize(description)
    
    return {
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "payment_method": "cash",
        "subcategory": "",
        "tags": ""
    }
