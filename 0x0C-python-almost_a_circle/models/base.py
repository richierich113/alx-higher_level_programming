#!/usr/bin/python3
"""base module for all other classes in this project
"""


class Base:
    """base class for use with other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor of  the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            empty_list = "[]"
            return empty_list

        if (type(list_dictionaries) != list or not
                all(type(k) == dict for k in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        name_of_file = cls.__name__ + ".json"

        with open(name_of_file, "w") as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                dictionary_lsts = [objts.to_dictionary() for objts in list_objs]

                myFile.write(Base.to_json_string(dictionary_lsts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representations"""
        if json_string is None or len(json_string == 0):
            emptylist_of_json_strings = []
            return emptylist_of_json_strings
        else:
            if type(json_string) != str:
                raise TypeError("json_string must be a string")

            list_of_json_strings = json.loads(json_string)
            return list_of_json_strings
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)

        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

     @classmethod
    def load_from_file(cls):
        """returns a list of all instances in class's file
        """
        name_of_file = cls.__name__  + '.json'

        try:
            with open(name_of_file, 'r', encoding='utf-8') as myFile:
                text_str = myFile.read()

        except Exception as e:
            return []

        instance_list = []
        dictionary_list = cls.from_json_string(text_str)

        for dictionary in dictionary_list:
            instance_list.append(cls.create(**dictionary))
        return instance_list


if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())
