#!/usr/bin/python3
"""Creating a class Student basing on file 10-student.py"""


class Student:
    """the classes"""
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """Initialised instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieving the dictionary representation of the class"""
        context = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        if attrs is None and type(attrs) != list:
            return context
        else:
            cont = {}
            for item in attrs:
                if type(item) != str:
                    return context
                if item in context.keys():
                    cont[item] = context[item]
            return cont

    def reload_from_json(self, json):
        """reload from json"""
        for item in json.keys():
            self.__dict__[item] = json[item]
