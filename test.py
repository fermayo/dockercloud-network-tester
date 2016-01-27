import os
import time
import signal
import tutum
import requests
import sys


def check_connectivity():
    my_service = tutum.Utils.fetch_by_resource_uri(os.getenv("TUTUM_SERVICE_API_URI"))
    containers = tutum.Container.list(service=my_service.resource_uri, state="Running")
    print "%s: Trying to contact: %s" % (time.asctime(), " ".join([c.private_ip for c in containers]))
    for container in containers:
        try:
            r = requests.get("http://%s:8000" % container.private_ip, timeout=2)
            r.raise_for_status()
            print "%s: %s on %s is reachable" % (time.asctime(), container.name, container.node)
        except requests.exceptions.RequestException as e:
            print "%s: %s on %s is NOT reachable: %s" % (time.asctime(), container.name, container.node, e)
    sys.stdout.flush()


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, lambda x, y: sys.exit())
    while True:
        check_connectivity()
        time.sleep(5)
