import json
from pymongo import MongoClient
from bson.objectid import ObjectId
import time
import datetime
from config import Config
import codecs


class CourseMongoDB:
    COURSE_TYPE = [
        "_id",
        "alias_name",
        "audience",
        "average_rating",
        "benefit",
        "category_ids",
        "curriculums",
        "description",
        "name",
        "rating",
        "price",
        "requirement",
        "lang",
        #"description_editor",
    ]

class Courses():
    def __init__(self, conf):
        mongolab_uri = "mongodb://pedia:pedia.jackfruit%40topica@sgdb1.pedia.vn:27017,sgdb2.pedia.vn:27017/jackfruit"
        client = MongoClient(mongolab_uri)
        self.db = client.get_default_database()
        self.conf = conf

    def collect_course(self):
        timeago = int(conf.get("time")["minutes"])
        timedelay = datetime.datetime.now() - datetime.timedelta(minutes=timeago)
        documment = self.db.courses.find({"version": "public", "fake_enabled": True, "enabled": True})#{"created_at": {"$gte": timedelay}})
        course_path = self.conf.get("output")["courses"]
        f = codecs.open(course_path, "a+", "utf-8")
        i = 0
        for course in documment:
            dict_data = {}
            for keys in CourseMongoDB.COURSE_TYPE:
                if keys in course.keys():
                    if keys == "_id":
                        dict_data[keys] = str(course[keys])
                    elif keys == "curriculums":
                        curris = []
                        for curri in course[keys]:
                            curris.append(curri['title'])
                        dict_data[keys] = curris
                    elif keys == "description":
                        list_data = ""
                        for index in range(1, len(course[keys])):
                            list_data += course[keys][index] + ". "
                        dict_data[keys] = list_data
                    elif isinstance(course[keys], list):
                        list_data = ""
                        for ls in course[keys]:
                            try:
                                list_data += ls + ". "
                            except:
                                list_data += str(ls) + ". "
                        dict_data[keys] = list_data
                    else:
                        dict_data[keys] = course[keys]
                else:
                    dict_data[keys] = None
            f.write(json.dumps(dict_data, ensure_ascii=True) + "\n")
        f.close()

class User:
    #global_track tap trung vao behavior: open, cateogry: U2
    USER_TYPE = [
        'user_id',
        'gender',
        'age_range',
        'money',
        'event_type', # buy, view
        'course_id',
        'timestamp'
    ]

class UserAction:
    def __init__(self, conf):
        self.conf = conf
        mongolab_uri = "mongodb://spymaster:spymaster%40pedia.topica@sgdbsector40.edumall.vn:27017,sgdbsector41.edumall.vn:27017/spymaster"
        client = MongoClient(mongolab_uri)
        self.db_spymaster = client.get_default_database()
        course = Courses(conf)
        course.collect_course()
        self.db_pedia = course.db


    def get_pedia_userById(self, _id):
        return self.db_pedia.users.find_one({"_id": ObjectId(_id)},
                                            {"meta_data": 1, "money": 1})

    def get_pedia_course(self, alias_name):
        return self.db_pedia.courses.find_one({"alias_name": alias_name},
                                              {"_id": 1, "alias_name": 1})

    def get_pedia_userPayment(self, f):
        #khac hang da mua khoa hoc
        timeago = int(conf.get("time")["minutes"])
        timedelay = datetime.datetime.now() - datetime.timedelta(minutes=timeago)
        payments = self.db_pedia.payments.find({"status": "success",
                                                "created_at": {"$gte": timedelay}},
                                               {"user_id": 1,
                                                "course_id": 1,
                                                "created_at": 1})
        for payment in payments:
            try:
                users = {}
                user_id = str(payment['user_id'])
                #user_info = self.get_pedia_userById(user_id)
                users['user_id'] = user_id
                users['event_type'] = "buy"
                users['course_id'] = str(payment['course_id'])
                users['timestamp'] = int(time.mktime(payment['created_at'].timetuple()))

                f.write(json.dumps(users, ensure_ascii=True) + "\n")
            except:
                print payment

    def get_userGlobalTracking(self, f):
        timeago = int(conf.get("time")["minutes"])
        timedelay = datetime.datetime.now() - datetime.timedelta(minutes=timeago)

        global_tracks = self.db_spymaster.global_tracks.find({
                                              "behavior": "open",
                                              "category": "U2",
                                              "user": {"$ne": None},
                                              "created_at": {"$gte": timedelay},
                                              "target": {"$regex": "edumall.vn/courses/"}},
                                                        {"user": 1,
                                                         "target": 1,
                                                         "created_at": 1}
                                             )
        text_search_path = self.conf.get("output")["text_search"]
        fs = open(text_search_path, "a+")
        courses_dict = {}
        for track in global_tracks:
            try:
                users = {}
                user_id = str(track['user'])
                users['user_id'] = user_id
                users['event_type'] = "open"
                if len(track['target'].split("edumall.vn/courses/")) == 2:
                    alias_name = track['target'].split("edumall.vn/courses/")[1].split("/")[0]
                    if len(alias_name.split("search?q=")) == 2:
                        users['event_type'] = "search"
                        users['search'] = alias_name.split("search?q=")[1]
                        users['timestamp'] = int(time.mktime(track['created_at'].timetuple()))
                        fs.write(json.dumps(users, ensure_ascii=True) + "\n")
                        continue
                    elif len(track['target'].split("/detail")) > 1:
                        if alias_name in courses_dict.keys():
                            users['course_id'] = courses_dict[alias_name]
                        else:
                            courses = self.get_pedia_course(alias_name)
                            if courses == None:
                                continue
                            users['course_id'] = str(courses['_id'])
                            courses_dict[alias_name] = str(courses['_id'])
                        users['timestamp'] = int(time.mktime(track['created_at'].timetuple()))
                        f.write(json.dumps(users, ensure_ascii=True) + "\n")
            except Exception as e:
                print e
                print track

        fs.close()


    def get_user(self):
        users_action_path = self.conf.get("output")["users_action"]
        users_buy_path = self.conf.get("output")["users_buy"]
        f = open(users_action_path, "a+")
        fpayment = open(users_buy_path, "a+")
        self.get_pedia_userPayment(fpayment)
        fpayment.close()
        self.get_userGlobalTracking(f)
        f.close()

if __name__ == '__main__':
    conf = Config()
    #mmsm = UserAction(conf)
    #mmsm.get_user()

    course = Courses(conf)
    course.collect_course()