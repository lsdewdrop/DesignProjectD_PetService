class ReportType():
    def __init__(self):
        self.id=None
        self.type=None

    @classmethod
    def create_from_request(cls, request_data):
        type = ReportType()
        type.type = request_data['type']
        if 'id' in request_data:
            type.id = request_data['id']


        return type

    @classmethod
    def makeDicByReportType(cls, rt):
        dic = {'id': rt.id, 'type': rt.type}
        return dic

    @classmethod
    def create_from_dbdata(cls, dbdata):
        type = ReportType()
        type.id = dbdata[0]
        type.type = dbdata[1]

        return type

class Report():
    def __init__(self):
        self.id=None
        self.title=None
        self.tid = None
        self.uid = None
        self.time = None
        self.content = None

    @classmethod
    def create_from_request(cls, request_data):
        report = Report()

        if 'id' in request_data:
            report.id = request_data['id']
        if 'title' in request_data:
            report.id = request_data['title']
        if 'tid' in request_data:
            report.id = request_data['tid']
        if 'uid' in request_data:
            report.id = request_data['uid']
        if 'time' in request_data:
            report.id = request_data['time']
        if 'content' in request_data:
            report.id = request_data['content']

        return report

    @classmethod
    def makeDicByReport(cls, r):
        dic = {'id': r.id, 'title': r.title, 'tid':r.tid, 'uid':r.uid,'time':r.time,'content':r.content}
        return dic

    @classmethod
    def create_from_dbdata(cls, dbdata):
        report = Report()
        report.id = dbdata[0]
        report.title = dbdata[1]
        report.tid = dbdata[2]
        report.uid = dbdata[3]
        report.time = dbdata[4]
        report.content = dbdata[5]

        return report