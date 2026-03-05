from locust import HttpUser, task, between

class WordPressUser(HttpUser):
    wait_time = between(1, 3)

    @task(5)
    def home(self):
        self.client.get("/")

    @task(3)
    def blog_posts(self):
        self.client.get("/blog/")

    @task(2)
    def search(self):
        self.client.get("/?s=test")

    @task(1)
    def login_page(self):
        self.client.get("/wp-login.php")

    @task(2)
    def rest_api(self):
        self.client.get("/wp-json/wp/v2/posts")
