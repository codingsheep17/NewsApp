#news app using Gnews Api
import requests
import sys

class NewsApp:
    def __init__(self):
        self.ip_api()

    def ip_api(self):
        self.ip_api_url = "http://ip-api.com/json/"
        self.response = requests.get(self.ip_api_url).json()
        self.country_code = self.response["countryCode"].lower()  # e.g. 'pk'
        self.country_name = self.response["country"]
        self.api_working()
        
    def api_working(self):
        try:
            self.api_key = "2e3e4d7b1ede374bc383ccf2064acd22"
            self.country = "us"
            self.api_url = f"https://gnews.io/api/v4/top-headlines?country={self.country}&apikey={self.api_key}"
            self.data_fetch = requests.get(self.api_url)
            self.data = self.data_fetch.json()
            self.user_menu()
        except Exception:
            print("""---An Error Occured While Fetching Data---
1: Try Again, Check Your Internet Connection
2: Try Again By Restarting the App
3: Check If the Server is Down or Crashed.""")
    
    def top_headlines(self):
        self.index_no = 0
        for i in range(1,5):
            self.title = self.data["articles"][self.index_no]["title"]
            self.source = self.data["articles"][self.index_no]["source"]["name"]
            self.url = self.data["articles"][self.index_no]["url"]
            print("******")
            print(f"Title --> {self.title}")
            print(f"Source --> {self.source}")
            print(f"Url --> {self.url}")
            print("******")
            self.index_no += 1

    def news_categories(self):
        try:     
            print(f"""--- Choose a News Category ---
1. 🧠 Technology
2. 💼 Business
3. ⚽ Sports
4. 🎬 Entertainment
5. 🏛️ Politics
6. 🌍 World""")
            self.news_category = int(input("Enter (1-6) --> "))
            self.cateogries = {
                1: "technology",
                2: "business",
                3: "sports",
                4: "entertainment",
                5: "politics", 
                6: "world"
            }

            if self.news_category in self.cateogries:
                self.cateogry = self.cateogries[self.news_category]
                self.api_url = f"https://gnews.io/api/v4/top-headlines?category={self.cateogry}&country={self.country_code}&apikey={self.api_key}"
                self.data_fetch = requests.get(self.api_url)
                self.data = self.data_fetch.json()
                self.top_headlines()
            else:
                print("❌ Invalid input. Choose a number between 1 and 6.")
        except ValueError:
            print("❌ Please enter a number only (1-6).")

        
    def change_country(self):
        try:
            self.country_option = input("--- Enter the Country Code (e.g. us, gb, pk) --> ").lower()
            if len(self.country_option) == 2:
                self.country = self.country_option
                self.country_name = self.country.upper()  # optional
                self.api_url = f"https://gnews.io/api/v4/top-headlines?country={self.country}&apikey={self.api_key}"
                self.data_fetch = requests.get(self.api_url)
                self.data = self.data_fetch.json()
                print(f"✅ Country changed to {self.country.upper()}.")
                self.top_headlines()
            else:
                print("❌ Please enter a valid 2-letter country code.")
        except Exception as e:
            print(f"❌ Error while changing country: {e}")


    def user_menu(self):
        while True:
            self.user_menu_input = 0
            try:
                print(f"""
1: Top Headlines {self.country_name}
2: News Categories
3: Filter by Country
4: Exit --> """)
                self.user_menu_input = int(input("Enter Your Choice --> "))
                if self.user_menu_input == 1:
                    self.top_headlines()
                elif self.user_menu_input == 2:
                    self.news_categories()
                elif self.user_menu_input == 3:
                    self.change_country()
                elif self.user_menu_input == 4:
                    print("Thanks for using NewsApp")
                    sys.exit()
            except ValueError:
                print("Kindly Enter Only Option Ranging From (1-4)")

newsapp = NewsApp()