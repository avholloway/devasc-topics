#!/usr/bin/env python3

import json

class ExamBlueprint(object):
    """Builds and holds an Exam Blueprint"""

    def __init__(self, filename):
        self.blueprint = {}
        if not filename is None:
            self.__load_file(filename)
            self.__build_blueprint()

    def __load_file(self, filename):
        with open(filename, "r") as finput:
            self.file_contents = finput.read().splitlines()
        return self

    def __build_blueprint(self):
        for i in range(len(self.file_contents)):
            line = self.file_contents[i]
            if "%" in line:
                continue
            number, title = line.split(" ", 1)
            self.create_section(number, title)
            if number.endswith("0"):
                self.add_percentage(number, self.file_contents[i+1])
        return self

    def get_file_contents(self):
        return "\n".join(self.file_contents)

    def to_json(self, indent = None):
        return json.dumps(self.blueprint, indent = indent)

    def create_section(self, number, title):
        if number and title and not number in self.blueprint.keys():
            self.blueprint[number] = {"title":title}
        return self

    def add_percentage(self, number, percentage):
        if number and percentage:
            self.blueprint[number]["percentage"] = percentage
        return self

    def read_section(self, number):
        if number and number in self.blueprint.keys():
            return self.blueprint[number]
        else:
            return f"Section {number} Not Found"

    def update_section(self, number, title):
        if number and title and number in self.blueprint.keys():
            self.blueprint[number] = title
        return self

    def delete_section(self, number):
        if number and number in self.blueprint.keys():
            del self.blueprin[number]
        return self

def main():
    exam = ExamBlueprint("devasc-topics.txt")
    print(exam.to_json(indent = 4))

if __name__ == '__main__':
    main()
