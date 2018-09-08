import WebexTeams

def main():
    auth_token = "Put your token here"
    wx = WebexTeams.Webex_Teams(auth_token)
    wx.send_test_to_sparky("This message sent before running delete script")
    wx.delete_my_messages(wx.search_my_rooms(title = "Sparky"))
    wx.send_test_to_sparky("This message sent after running delete script")


main() if __name__ == "__main__" else None