def main():
    name_list = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in name_list:
        print(write_letter(name, "Princess Peach"))
def write_letter(recipient, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {recipient},
    
       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """
main()