from traitlets import Type, Instance
from .baseapp import NbGrader
from ..plugins import ExportPlugin, CsvExportPlugin
from ..api import Gradebook

aliases = {
    'log-level' : 'Application.log_level',
    'db': 'NbGrader.db_url',
    'to' : 'ExportPlugin.to',
    'exporter': 'ExportApp.plugin_class'
}
flags = {}


class ExportApp(NbGrader):

    name = u'nbgrader-export'
    description = u'Export information from the database to another format.'

    aliases = aliases
    flags = flags

    examples = """

        The default is to export to a file called "grades.csv", i.e.:

            nbgrader export

        You can customize the filename with the --to flag:

            nbgrader export --to mygrades.csv

        To change the export type, you will need a class that inherits from
        nbgrader.plugins.ExportPlugin. If your exporter is named
        `MyCustomExporter` and is saved in the file `myexporter.py`, then:

            nbgrader export --exporter=myexporter.MyCustomExporter

        """

    plugin_class = Type(
        CsvExportPlugin,
        klass=ExportPlugin,
        help="The plugin class for exporting the grades."
    ).tag(config=True)

    plugin_inst = Instance(ExportPlugin).tag(config=False)

    def init_plugin(self):
        self.log.info("Using exporter: %s", self.plugin_class.__name__)
        self.plugin_inst = self.plugin_class(parent=self)

    def _classes_default(self):
        classes = super(ExportApp, self)._classes_default()
        classes.append(ExportApp)
        classes.append(self.plugin_class)
        return classes

    def start(self):
        super(ExportApp, self).start()
        self.init_plugin()
        gradebook = Gradebook(self.db_url)
        try:
            self.plugin_inst.export(gradebook)
        finally:
            gradebook.db.close()
