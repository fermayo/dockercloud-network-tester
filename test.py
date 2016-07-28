from gevent import monkey; monkey.patch_all()
import os
import time
import signal
import dockercloud
import sys
import pyping
import re
import gevent
import psutil

node_short_uuid = re.compile(r"\/(\w+)-")
polling_period = int(os.getenv("POLLING_PERIOD", 5))
my_container_short_uuid = node_short_uuid.search(os.getenv("DOCKERCLOUD_CONTAINER_API_URI")).group(1)
psutil.PROCFS_PATH = "/host/proc"


def check_connectivity(my_service):
    containers = dockercloud.Container.list(service=my_service.resource_uri, state="Running")
    jobs = [gevent.spawn(ping_container, container) for container in containers]
    gevent.joinall(jobs, timeout=2100)
    results = filter(None, [job.value for job in jobs])
    if results:
        print "[CPU: %s%% MEM: %s%%] %s" % (psutil.cpu_percent(), psutil.virtual_memory().percent,
                                            " | ".join(sorted(results)))
        sys.stdout.flush()


def ping_container(container):
    r = pyping.ping(container.name, count=3, timeout=2000, quiet_output=True)
    rtt = float(r.avg_rtt) if r.avg_rtt else None
    if not rtt or rtt >= int(os.getenv("PING_THRESHOLD_MS", 0)):
        return "%s->%s: %s" % (my_container_short_uuid, node_short_uuid.search(container.node).group(1),
                               "%8.2f ms" % rtt if rtt else "%11s" % "!!!")
    else:
        return


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, lambda x, y: sys.exit())
    if not os.path.isdir(psutil.PROCFS_PATH):
        print "You must mount the host's /proc folder to /host/proc inside this container"
        exit(1)

    print "%s: Starting periodic pings with a polling period of %s seconds" % (time.asctime(), polling_period)
    my_service = dockercloud.Utils.fetch_by_resource_uri(os.getenv("DOCKERCLOUD_SERVICE_API_URI"))
    while True:
        check_connectivity(my_service)
        time.sleep(polling_period)
