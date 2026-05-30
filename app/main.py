class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_of_objects = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        if person_dict.get("wife") is not None:
            person.wife = person_dict.get("wife")
        if person_dict.get("husband") is not None:
            person.husband = person_dict.get("husband")
        list_of_objects.append(person)
    for objects in list_of_objects:
        if hasattr(objects, "wife"):
            objects.wife = objects.people[objects.wife]
        if hasattr(objects, "husband"):
            objects.husband = objects.people[objects.husband]
    return list_of_objects
