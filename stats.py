
def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    counts = {}
    for char in text:
        # Convert character to lowercase
        lowered_char = char.lower()
        
        # Update the count in the dictionary
        if lowered_char in counts:
            counts[lowered_char] += 1
        else:
            counts[lowered_char] = 1
            
    return counts

def sort_on_num_down(item):
    """Helper function to return the 'num' key for sorting."""
    return item["num"]

def get_chars_sorted_list(char_counts_dict):
    """
    Converts a character count dictionary into a sorted list of dictionaries.

    Args:
        char_counts_dict (dict): A dictionary of character counts.

    Returns:
        list: A list of dictionaries, sorted by count in descending order.
    """
    sorted_list = []
    for char, count in char_counts_dict.items():
        sorted_list.append({"char": char, "num": count})
    
    # Sort the list from greatest to least (descending) using the helper function
    sorted_list.sort(reverse=True, key=sort_on_num_down)
    
    return sorted_list