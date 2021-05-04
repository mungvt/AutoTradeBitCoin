from datetime import datetime
import luigi
import crawl, bq_code, logic


class BaseTask(luigi.Task):
    """
    Output Create a Abstract Class
    """
    date = luigi.DateSecondParameter(default=datetime.now())

    def output(self):
        return logic.create_target(self)

    def execute(self):
        pass

    def run(self):
        cls_name = self.__class__.__name__
        # logic.write_log("Start {}. [{}]".format(cls_name, self.date))
        print("Start {}. [{}]".format(cls_name, self.date))
        try:
            self.execute()
        except Exception as e:
            # logic.write_log("Exception.[{}]".format(str(e)))
            print("Exception.[{}]".format(str(e)))
            raise
        logic.touch_target(self, cls_name)
        # logic.write_log("End {}.".format(cls_name))
        print("End {}.".format(cls_name))
        return


class CrawlData(BaseTask):
    def execute(self):
        crawl.crawl_data()


class CreateAllTables(BaseTask):
    def requires(self):
        return CrawlData()

    def execute(self):
        bq_code.create_all_tables()


class ImportData(BaseTask):
    def requires(self):
        yield CrawlData()
        yield CreateAllTables()

    def execute(self):
        bq_code.load_btc_data_into_bq()


class AllTasks(luigi.WrapperTask):
    """
    Output A WrapperTask
    """
    def requires(self):
        return ImportData()
