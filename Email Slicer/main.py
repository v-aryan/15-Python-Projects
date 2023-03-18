def email_slicer():
    print("Welcome to email slicer")
    print("")

    entered_email = input("Enter your email: ")

    (username,domain) = entered_email.split("@")
    (domain,extension) = domain.split(".")

    print("Username:",username)
    print("Domain:",domain)
    print("Extension:",extension)

email_slicer()