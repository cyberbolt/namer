from typing import List
Names = List[str]

"""
Main entity to work with names
"""
class SimpleNamer:
    def __init__(self, data=None):
        self.__storage = list()
        if data:
            self.__storage += data

    """
    Adds a name to local storage
    """
    def addName(self, name: str) -> None:
        if (name and type(name) is str):
            self.__storage.append(name)

    """
    Gets last five names such as last input name returns first
    """
    def getNames(self) -> Names:
        return self.__storage[-5:][::-1]
