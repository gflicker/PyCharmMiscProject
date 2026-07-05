#Having as make keyword pair arguments as possible
#Building user profiles
def build_profile(first, last, **user_info):
    #Double asterisks tells python to build a dictionary called user_info
    """Build a profile object for user_info"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('John', 'Doe', location='New York', field = 'Maths')
print(user_profile)