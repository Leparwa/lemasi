import json
class Post():
    def __init__(self,  title,  description, post, author, image):
        self.description = description
        self.price = post
        self.title = title
        self.author = author
        self.image = image

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)