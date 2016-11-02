import pymongo
import csv


class Collect(object):
    def __init__(self, address, port, db, user, password):
        """

        :param address:
        :param port:
        :param db:
        :param user:
        :param password:
        """
        db_connect = pymongo.MongoClient(address, port)
        database = db_connect[db]
        database.authenticate(user, password)
        collections = database.collection_names(include_system_collections=False)
        self.database = database
        self.collections = collections

    def collect_link_course(self):
        for i in self.collections:
            if i == 'courses':
                with open("course_search.csv", "w") as f:
                    cursor = self.database[i].find({}, {"name": 1, "alias_name": 1, "user_id": 1})
                    for document in cursor:
                        link = "https:/edumall.vn/course" + document["alias_name"]
                        # document["user_id"] = str(document.get("user_id"))
                        document["_id"] = str(document["_id"])
                        a = csv.writer(f, delimiter=',')
                        data = [document["_id"], document["name"], link]
                        a.writerow(data)
            # if i == 'user':
            #     with open("teacher_search.csv", "w") as f:
            #         cursor = self.database[i].find({})
            #         for document in cursor:


if __name__ == '__main__':
    collect_course = Collect('sgdb1.pedia.vn', 27017, 'jackfruit', 'pedia', 'pedia.jackfruit@topica')
    # collect_teacher = Collect('sgepimetheus4.edumall.vn', 27017, 'tartarus', 'tartarus', 'tartarus.edumall@topica')
    collect_course.collect_link_course()
