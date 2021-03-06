from flask_script import Manager

manager = Manager(usage="Perform database operations")

@manager.command
def drop():
    "Drops database tables"
    raise NotImplementedError
    # if prompt_bool("Are you sure you want to lose all your data"):
    #     db.drop_all()


@manager.command
def create(default_data=True, sample_data=False):
    "Creates database tables from sqlalchemy models"
    raise NotImplementedError
    # db.create_all()
    # populate(default_data, sample_data)


@manager.command
def recreate(default_data=True, sample_data=False):
    "Recreates database tables (same as issuing 'drop' and then 'create')"
    raise NotImplementedError
    # drop()
    # create(default_data, sample_data)


@manager.command
def populate(default_data=False, sample_data=False):
    "Populate database with default data"
    raise NotImplementedError
    # from fixtures import dbfixture

    # if default_data:
    #     from fixtures.default_data import all
    #     default_data = dbfixture.data(*all)
    #     default_data.setup()

    # if sample_data:
    #     from fixtures.sample_data import all
    #     sample_data = dbfixture.data(*all)
    #     sample_data.setup()
