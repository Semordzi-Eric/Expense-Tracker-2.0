import re

# Default heuristic mapping for smart categorization
CATEGORY_MAP = {
    # Transport
    r'\b(uber|bolt|yango|stc|vip|trotro|taxi|transport|fuel|gas|petrol)\b': 'Transport',
    # Food
    r'\b(kfc|food|restaurant|lunch|dinner|breakfast|snack|mcdonalds|burger|pizza|waakye|jollof|kenkey|banku|eatery|drink|drinks|beverage)\b': 'Food',
    # Utilities
    r'\b(data|airtime|mtn|vodafone|telecel|at|airteltigo|ecg|water|electricity|bill|utility)\b': 'Utilities',
    # Groceries
    r'\b(market|supermarket|mall|melcom|shoprite|groceries|provisions)\b': 'Groceries',
    # Entertainment
    r'\b(netflix|spotify|apple|movie|club|party|entertainment|games)\b': 'Entertainment',
    # Health
    r'\b(pharmacy|hospital|clinic|drugs|medicine|health|doctor)\b': 'Health',
    # Shopping
    r'\b(clothes|shoes|bag|shein|amazon|jumia|shopping)\b': 'Shopping',
    # Personal
    r'\b(salon|barber|hair|spa|massage|personal)\b': 'Personal',
    # Transfer
    r'\b(transfer|sent|momo|pay|payment)\b': 'Transfer'
}

def auto_categorize(text: str) -> str:
    """
    Categorizes a transaction based on keywords in its description or text.
    Returns 'Other' if no match is found.
    """
    text = text.lower()
    for pattern, category in CATEGORY_MAP.items():
        if re.search(pattern, text):
            return category
    return "Other"
