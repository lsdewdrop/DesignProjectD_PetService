class Post():
    def __init__(self):
        self.no = None
        self.tilte = None
        self.auth_id = None
        self.content = None
        self.time = None
        self.register_id = None
        self.pet = None


    @classmethod
    def create_from_request(cls, request_data):
        post = Post()
        post.title = request_data['title']
        if 'auth_id' in request_data:
            post.kinds_kinds = request_data['auth_id']
        if 'content' in request_data:
            post.content=request_data['content']
        if 'time' in request_data:
            post.time = request_data['time']
        if 'register_id' in request_data:
            post.register_id = int(request_data['register_id'])
        if 'pet' in request_data:
            post.pet = int(request_data['pet'])


        return post