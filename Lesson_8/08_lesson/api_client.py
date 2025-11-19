import requests

from config import BASE_URL, API_TOKEN

class YougileAPI:
    def __init__(self):
        self.base_url = f"{BASE_URL}/api-v2/projects"
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, name):
        data = {"title": name}
        return requests.post(self.base_url, json=data, headers=self.headers)

    def update_project(self, project_id, new_name):
        data = {"title": new_name}
        return requests.put(f"{self.base_url}/{project_id}", json=data, headers=self.headers)
 
 
    def get_project(self, project_id):
        return requests.get(f"{self.base_url}/{project_id}", headers=self.headers)
