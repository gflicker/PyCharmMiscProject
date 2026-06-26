#Showing how a dictionary inside a dictionary works
users = {
    "Rosetta": {
        "first_name": "rose",
        "last_name": "Zulu",
        "email": "roseta@gmail.com",
        "cell": "0979198251"
    },
    "Givious": {
        "first_name": "givious",
        "last_name": "haluse",
        "email": "glixes@gmail.com",
        "cell": "0978639675"
    }
}
for username, data in users.items():
    print(f'Hello {username.title()}! Kindly verify your details:')
    for details in data.values():
        print(f'\t{details.title()}')