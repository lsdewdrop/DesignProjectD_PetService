class Post():
    def __init__(self):
        self.no = None
        self.title = None
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
            post.auth_id = request_data['auth_id']
        if 'content' in request_data:
            post.content=request_data['content']
        if 'time' in request_data:
            post.time = request_data['time']
        if 'register_id' in request_data:
            post.register_id = int(request_data['register_id'])

        if 'pet' in request_data:
            post.pet = int(request_data['pet'])


        return post

    @classmethod
    def makeDicByPost(cls, post):
        dic = {'no': post.no, 'title': post.title, 'auth_id': post.auth_id, 'content': post.content,
               'time': post.time, 'register_id': post.register_id, 'pet': post.pet}
        return dic

    @classmethod
    def create_from_dbdata(cls, dbdata):
        post=Post()
        post.no=dbdata[0]
        post.title = dbdata[1]
        post.auth_id = dbdata[2]
        post.content = dbdata[3]
        post.time = dbdata[4]
        post.register_id = dbdata[5]
        post.pet = dbdata[6]

        return post