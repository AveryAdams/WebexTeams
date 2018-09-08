class Webex_Teams:
    def __init__(self, auth_token: str):
        import requests
        import json
        self.requests = requests
        self.json = json
        self.api_base_url = "https://api.ciscospark.com/v1/%s"
        self.auth_token = auth_token
        self.headers = {"Authorization": "Bearer " + auth_token}
        self.me = self.api_call().json()
    
    def api_call(self, request_type: str = "get", path: str = "people/me",
                 data: str = "",
                 *args, **kwargs):
        if request_type == "get":
            call = self.requests.get
        if request_type == "delete":
            call = self.requests.delete
        if request_type == "post":
            call = self.requests.post
        if request_type == "patch":
            call = self.requests.patch
        if request_type == "put":
            call = self.requests.put
        
        return (
            call(self.api_base_url % path, headers = self.headers, data = data))
    
    def send_test_to_sparky(self,
                            text: str = "This is a test message to Sparky... x`Sent via Avery's Python Script"):
        self.api_call(
                request_type = "post",
                path = "messages", data = {
                    "toPersonId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS83MjJiYjI3MS1kN2NhLTRiY2UtYTllMy00NzFlNDQxMmZhNzc",
                    "text"      : text
                })
    
    def get_my_rooms(self):
        self.my_rooms = self.api_call(path = "rooms").json()
        return self.my_rooms.get("items")
    
    def search_my_rooms(self, *args, **kwargs):
        rooms = []
        for index, room in enumerate(self.get_my_rooms()):
            for k, v in kwargs.items():
                if room.get(k) != v:
                    break
                rooms.append(room)
        return rooms
    
    def delete_my_messages_in_room_id(self, room_id: str, *args, **kwargs):
        response = self.api_call(
            path = "messages?max=999999999&roomId=" + room_id)
        for message in self.json.loads(response.text).get("items"):
            self.api_call(request_type = "delete",
                          path = "messages/" + str(message.get("id")))
    
    def delete_my_messages(self, room_obj_list: list):
        for room in room_obj_list:
            self.delete_my_messages_in_room_id(room.get("id"))