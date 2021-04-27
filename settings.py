from string import punctuation

DB_NAME = 'scheduler.db'
VALID_STATUSES = ['New', 'In Progress', 'Closed']
SYMBOLS = set(punctuation)

print(SYMBOLS)  # {'{', '"', ';', '}', '$', '%', '-', '/', "'", '=', '>', '[', '~', '`', '<', '.', '@', '?', ':', '(', '#', '^', ')', '+', '*', '!', '|', '&', ']', ',', '_', '\\'}
