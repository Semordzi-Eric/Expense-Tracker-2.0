import re
from datetime import datetime, timedelta
from utils.categorizer import auto_categorize

def get_recent_day_date(day_string: str) -> str:
    day_string = day_string.strip().lower()
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if day_string in days:
        target_day = days.index(day_string)
        current_day = datetime.now().weekday()
        diff = current_day - target_day
        if diff < 0:
            diff += 7 # It was last week
        dt = datetime.now() - timedelta(days=diff)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    elif day_string == "yesterday":
        return (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    elif day_string == "today":
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return ""

def parse_bulk_quick_add(user_input: str) -> list[dict]:
    """
    Parses multi-line input handling single amounts, comma-separated amounts,
    and contextual days (e.g. "Friday").
    """
    transactions = []
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lines = [line.strip() for line in user_input.split('\n') if line.strip()]
    
    for line in lines:
        parsed_date = get_recent_day_date(line)
        if parsed_date:
            current_date = parsed_date
            continue
            
        # Find all numbers in the line that could be amounts.
        matches = list(re.finditer(r'\b\d+(?:\.\d+)?(?:\s*,\s*\d+(?:\.\d+)?)*\b', line))
        if not matches:
            continue
            
        # Prefer the match that has commas, otherwise take the first match
        amount_match = None
        for m in matches:
            if ',' in m.group(0):
                amount_match = m
                break
        if not amount_match:
            amount_match = matches[0]
            
        amounts_str = amount_match.group(0)
        # remove spaces and split by comma
        amounts = [float(x.strip()) for x in amounts_str.split(',')]
        
        description = line[:amount_match.start()] + line[amount_match.end():]
        description = description.replace(',', '').strip()
        
        if not description:
            description = "Quick Add Entry"
            
        category = auto_categorize(description)
        
        for amt in amounts:
            transactions.append({
                "amount": amt,
                "category": category,
                "description": description,
                "date": current_date,
                "payment_method": "cash",
                "subcategory": "",
                "tags": ""
            })
            
    return transactions
