from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_text = toml.loads(content)
    
        wanted_dict = parsed_text['tool']['poetry']
        name = wanted_dict['name']
        description = wanted_dict['description']
        dependencies = wanted_dict['dependencies']
        developmentd_demendencies = wanted_dict['dev-dependencies']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, developmentd_demendencies)
