# import schedule
# import time

__author__ = "Jan Frömberg"
__copyright__ = "Copyright 2018, GeRDI Project"
__credits__ = ["Jan Frömberg"]
__license__ = "Apache"
__maintainer__ = "Jan Frömberg"
__email__ = "jan.froemberg@tu-dresden.de"


def job():
    print("poll the harvester api...")


# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)

# schedule.every().wednesday.at("13:15").do(job)


# while True:
#     schedule.run_pending()
#     time.sleep(1)


class Scheduler:
    """Custom Scheduler class to handle timed events."""
