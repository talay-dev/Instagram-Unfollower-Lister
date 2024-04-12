import instaloader
import os


class Instagram:
    def __init__(self) -> None:
        self.username = ""
        self.L = instaloader.Instaloader()
        
    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        
    def welcome(self):
        print("Welcome to Instagram Downloader")
        print("Please before you start, enter your account from firefox and then run cookie.py file")
        print("Then you can start downloading")
        #list session files in the current directory
        self.username = input("Enter your username which you login: ")
        
        try:
            self.L.load_session_from_file(self.username)
        except FileNotFoundError:
            print("Session file not found, please run cookie.py file")
            exit()
            
        self.clear()
        
        print("Logged in successfully")
        
        self.menu()
        
    def menu(self):
        print("\n" * 2)
        print("*" * 50)
        print("1. Download Profile Picture Only")
        print("2. Download All Posts")
        print("3. Download All Stories")
        print("5. List Unfollowers")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.download_profile_picture()
        elif choice == 2:
            self.download_all_posts()
        elif choice == 3:
            self.download_all_stories()
        elif choice == 5:
            self.list_unfollowers()
        elif choice == 6:
            print("Exiting...")
            exit()
        else:
            print("Invalid choice")
            self.menu()
            
    def download_profile_picture(self):
        self.clear()
        target_username = input("Enter the username of the target: ")

        try:
            self.L.download_profile(target_username, profile_pic_only=True)
            print("Profile picture downloaded successfully")
            
            if os.name != "nt":
                for file in os.listdir(target_username):
                    if file.endswith(".jpg"):
                        os.rename(target_username + "/" + file, target_username + ".jpg")
                        #open the image
                        os.system("open " + target_username + ".jpg")
                        
            
        except Exception as e:
            print("Error: ", e)
        self.menu()
        
    def download_all_posts(self):
        self.clear()
        target_username = input("Enter the username of the target: ")

        try:
            self.L.download_profile(target_username)
            print("All posts downloaded successfully")
        except Exception as e:
            print("Error: ", e)
        self.menu()
        
    def download_all_stories(self):
        self.clear()
        target_username = input("Enter the username of the target: ")

        try:
            self.L.download_profile(target_username, profile_pic=False, profile_pic_only=False, stories_only=True)
            print("All stories downloaded successfully")
        except Exception as e:
            print("Error: ", e)
        self.menu()
        
    def list_unfollowers(self):
        self.clear()
        target_username = input("Enter the username of the target: ")

        try:
            profile = instaloader.Profile.from_username(self.L.context, target_username)
            followers = set(profile.get_followers())
            followees = set(profile.get_followees())
            unfollowers = followees - followers
            print("Unfollowers: ")
            for unfollower in unfollowers:
                print(unfollower.username)
        except Exception as e:
            print("Error: ", e)
        self.menu()
        
if __name__ == "__main__":
    instagram = Instagram()
    instagram.welcome()
        