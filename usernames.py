import pandas as pd
import random
import string
import numpy as np

# Constants
NUM_USERS_PER_FILE = 200
NUM_FILES_TO_GENERATE = 10
PLATFORM_VALUE = "X"
SEND_AMOUNT_VALUE = 0.0001
DESCRIPTIVE_TEXT = "Please follow the format below to enter custom receivers and send amounts. You will select an available token on the sending page."
HEADER_ROW = ['Receivers', 'Platform', 'Send Amount']

# Sample name pool for realistic usernames
name_pool = [
    'jepht', 'uche', 'daniel', 'bliss', 'chika', 'tomi', 'emeka',
    'grace', 'ayobami', 'sade', 'bayo', 'kelvin', 'amara', 'kenny',
    'ife', 'chioma', 'lola', 'tope', 'zainab', 'kalu', 'temi', 'mike'
]

def generate_realistic_username():
    """Generates a more human-like username."""
    base = random.choice(name_pool)
    use_underscore = random.choice([True, False])
    use_number = random.choice([True, False])

    username = base
    if use_underscore:
        username += '_'
    if use_number:
        username += str(random.randint(1, 999))

    return '@' + username

def generate_unique_usernames(num_users):
    """Generates a set of unique usernames with a real look."""
    usernames = set()
    while len(usernames) < num_users:
        usernames.add(generate_realistic_username())
    return list(usernames)

# Main loop to generate Excel files
for i in range(1, NUM_FILES_TO_GENERATE + 1):
    usernames = generate_unique_usernames(NUM_USERS_PER_FILE)

    # Create rows: first the description row, then header, then usernames
    all_rows = [[DESCRIPTIVE_TEXT] + [np.nan] * (len(HEADER_ROW) - 1)]
    all_rows.append(HEADER_ROW)

    for username in usernames:
        all_rows.append([username, PLATFORM_VALUE, SEND_AMOUNT_VALUE])

    df_output = pd.DataFrame(all_rows)

    filename = f"user_batch_{i}.xlsx"

    try:
        df_output.to_excel(filename, index=False, header=False)
        print(f"✅ File saved: {filename}")
    except Exception as e:
        print(f"❌ Error saving file {filename}: {e}")

print("\n🎉 Done! All files generated with improved usernames and clean filenames.")
