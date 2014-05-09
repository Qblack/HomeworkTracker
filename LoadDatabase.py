__author__ = 'Q'
__author__ = 'Q'


from Database import DataBase
from ReadCourseInfo import *
import SetUpDataBase


def load_database():
    SetUpDataBase.reset_database()

    db = DataBase("summer2014courses.db")


    fh = open("bu362.txt","r+",encoding="utf-8")
    bu362 = convert_schedule_to_course(fh,"BU362","Building and Managing A Brand", db)
    fh.close()


    convert_schedule_to_course_bu395("BU395.txt","BU395","Operations Management II",db)


    convert_schedule_to_course_bu398("BU398.txt","BU398","Organizational Behaviour II",db)
    convert_schedule_to_course_bu415("BU415.txt","BU415","Intro Management of IS",db)

    convert_schedule_to_course_bu393("BU393.txt","BU393","Financial Management II",db)


