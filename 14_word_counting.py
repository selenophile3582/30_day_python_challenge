sent = input("Enter your sentence :")
if sent.strip()=="":  # Using strip() to handle whitespace-only strings
    print("0 words ")
else :
    print(f"Your sentence contains {len(sent.split())} words.")