import os
import json
import instaloader


def find_unfollowers(target_username, file):
    """
    Finds the users who are not following the target_username on Instagram.

    Args:
        target_username (str): The username of the target user.
        file (str): The file path to the JSON file containing the login credentials.

    Returns:
        None
    """
    # Get data
    with open(file) as f:
        data = json.load(f)

    # Login or load session
    L = instaloader.Instaloader()
    L.login(data["username"], data["password"])  # (login)
    print("Logged in successfully")

    # Obtain profile metadata
    profile = instaloader.Profile.from_username(L.context, target_username)
    print("Obtained profile metadata")

    followers = profile.get_followers()
    follows = profile.get_followees()

    print("Obtained followers and follows")
    followers = [follower.username for follower in followers]
    follows = [follow.username for follow in follows]
    unfs = []

    print("*" * 40)
    for i in follows:
        if i not in followers:
            unfs.append(i)
    for i in unfs:
        print(i)


def set_account_info():
    """
    Sets the Instagram account information.

    Returns:
        dict: The dictionary containing the account information.
    """
    if os.path.exists("info.json"):
        with open(file) as f:
            data = json.load(f)
        print(f"Current username: {data['username']}")
        change_info = input("Do you want to change the account information? (y/n): ")
        if change_info.lower() == "n":
            return data

    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    
    account_info = {"username": username, "password": password}
    
    save_info = input("Do you want to save the account information? (y/n): ")
    if save_info.lower() == "y":
        with open("account_info.json", "w") as f:
            json.dump(account_info, f)
        print("Account information saved successfully.")

    return account_info

def set_target_user():
    """
    Sets the target user on Instagram.

    Returns:
        str: The username of the target user.
    """
    target_username = input("Enter the username of the target user: ")
    return target_username


# Usage
account_info = set_account_info()
target_username = set_target_user()

find_unfollowers(target_username, file)
