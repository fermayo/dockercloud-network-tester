from gevent import monkey; monkey.patch_all()
import os
import time
import signal
import dockercloud
import sys
import pyping
import re
import gevent

node_short_uuid = re.compile(r"\/(\w+)-")
polling_period = int(os.getenv("POLLING_PERIOD", 5))
my_container_short_uuid = node_short_uuid.search(os.getenv("DOCKERCLOUD_CONTAINER_API_URI")).group(1)


def check_connectivity(my_service):
    containers = dockercloud.Container.list(service=my_service.resource_uri, state="Running")
    jobs = [gevent.spawn(ping_container, container) for container in containers]
    gevent.joinall(jobs, timeout=2100)
    results = [job.value for job in jobs]
    print " | ".join(sorted(filter(None, results)))
    sys.stdout.flush()


def ping_container(container):
    r = pyping.ping(container.name, count=1, timeout=2000, quiet_output=True)
    return "%s->%s: %s" % (my_container_short_uuid, node_short_uuid.search(container.node).group(1),
                           "%8.2f ms" % float(r.avg_rtt) if r.avg_rtt else "%11s" % "!!!")


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, lambda x, y: sys.exit())
    print "%s: Starting periodic pings with a polling period of %s seconds" % (time.asctime(), polling_period)
    my_service = dockercloud.Utils.fetch_by_resource_uri(os.getenv("DOCKERCLOUD_SERVICE_API_URI"))
    while True:
        check_connectivity(my_service)
        time.sleep(polling_period)
