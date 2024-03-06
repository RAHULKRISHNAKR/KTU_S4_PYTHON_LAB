def isvalid(email):
    if "@" not in email:
        return False

    parts = email.split("@")
    if len(parts) != 2:
        return False

    if "." not in parts[1]:
        return False

    if parts[1].count(".") != 1:
        return False

    if (parts[0]=='_' or parts[0]=='.' or parts[0]== '-'):
        return False
    for part in parts:
        if not part:
            return False
        for char in part:
            if not (char.isalnum() or char in "_.-"):
                return False

    return True

def main():
    email = input("enter email: ")
    print(isvalid(email))

main()
