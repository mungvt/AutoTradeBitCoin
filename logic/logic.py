import luigi
import os
import re
import configparser
# from luigi.contrib.mysqldb import MySqlTarget
# from luigi.contrib.bigquery import BigqueryTarget

config = configparser.ConfigParser()
config.read('config/config.ini')
DRY_RUN = config['DEFAULT']
PROJECT_ID = config['DEFAULT']['PROJECT_ID']


def is_dryrun():
    """
    Return mode
    :rtype bool
    :return: true or false
    """
    return DRY_RUN


def create_dir(_path):
    """
    Create a folder
    :param string _path: a path to the folder
    :return:
    """
    try:
        direct_path = os.getcwd() + _path
        if not os.path.exists(direct_path):
            os.mkdir(direct_path)
    except OSError:
        exit(1)


def convert_name(class_name):
    """
    Convert from class name to table name
    :param string class_name: a class name
    :rtype string
    :return: a table name or None
    """
    element_name = re.findall('[A-Z][^A-Z]*', class_name)

    if element_name[0] == 'Create':
        tbl_name = ''
        for i in element_name[1:]:
            tbl_name += i.lower() + '_'
        tbl_name = tbl_name[0:len(tbl_name) - 1]
        return tbl_name
    else:
        return None


def create_target(target):
    """
    Create a LocalTarget in DRYRUN mode
    Create a MySqlTarget in normal mode
    :param object target: a instance of the class
    :rtype object
    :return: a luigi Target
    """
    class_name = target.__class__.__name__
    tbl_name = convert_name(class_name)
    update_id = "{}_{}".format(class_name, target.date)
    if is_dryrun():
        return luigi.LocalTarget("dryrun/{}.txt".format(class_name))
    # else:
    #     return BigqueryTarget(
    #         project_id=PROJECT_ID,
    #         dataset_id=,
    #         table_id=,
    #         client=None,
    #         location=None
    #     )


def touch_target(target, cls_name):
    """
    Write into the file in DRYRUN mode
    Touch into the database in normal mode
    :param string cls_name: name of the class
    :param object target: a instance of the class
    :return:
    """
    if is_dryrun():
        with target.output().open('w') as f:
            f.write(
                "{} {}".format(
                    str(target.date),
                    cls_name)
            )
    # else:
    #     target.output().touch()


if __name__ == '__main__':
    print(DRY_RUN)
    print(type(DRY_RUN))
