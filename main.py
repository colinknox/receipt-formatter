def add_tax(receipt):
    return f"{receipt}\nTax: $0.00"


def add_header(receipt):
    return f"=== RECEIPT ===\n{receipt}"


def add_footer(receipt):
    return f"{receipt}\n=== THANK YOU ==="


def format_receipt(receipt):
    return add_footer(add_header(add_tax(receipt)))