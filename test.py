import os
import time
import signal
import dockercloud
import sys
import pyping
import re

node_short_uuid = re.compile(r"\/(\w+)-")
polling_period = int(os.getenv("POLLING_PERIOD", 5))
my_container_short_uuid = node_short_uuid.search(os.getenv("DOCKERCLOUD_CONTAINER_API_URI")).group(1)


def check_connectivity(my_service):
    containers = dockercloud.Container.list(service=my_service.resource_uri, state="Running")
    results = {}
    for container in containers:
        if container.resource_uri == os.getenv("DOCKERCLOUD_CONTAINER_API_URI"):
            continue
        r = pyping.ping(container.name, count=1, timeout=2000, quiet_output=True)
        results[node_short_uuid.search(container.node).group(1)] = r.avg_rtt
    print " | ".join(["%s->%s: %8.2f ms" % (my_container_short_uuid, k, float(v)) for k, v in results.iteritems()])
    sys.stdout.flush()


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, lambda x, y: sys.exit())
    print "%s: Starting periodic pings with a polling period of %s seconds" % (time.asctime(), polling_period)
    my_service = dockercloud.Utils.fetch_by_resource_uri(os.getenv("DOCKERCLOUD_SERVICE_API_URI"))
    while True:
        check_connectivity(my_service)
        time.sleep(polling_period)
