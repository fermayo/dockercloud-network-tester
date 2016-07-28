# dockercloud-network-tester

Tests connectivity to other containers through the overlay network

[![Deploy to Docker Cloud](https://files.cloud.docker.com/images/deploy-to-dockercloud.svg)](https://cloud.docker.com/stack/deploy/)


# Sample Output

    [network-tester-3]2016-07-20T16:50:28.458088897Z d24ca418->0facb879:     0.21 ms | d24ca418->264d48bc:     1.88 ms | d24ca418->6f989aef:    12.25 ms | d24ca418->f17488a6:     2.28 ms 
    [network-tester-2]2016-07-20T16:50:31.350371980Z e9155705->0facb879:     2.58 ms | e9155705->264d48bc:     0.20 ms | e9155705->6f989aef:     5.55 ms | e9155705->f17488a6:     2.52 ms 
    [network-tester-1]2016-07-20T16:50:33.207478527Z 4ec75006->0facb879:     3.76 ms | 4ec75006->264d48bc:     8.77 ms | 4ec75006->6f989aef:     0.52 ms | 4ec75006->f17488a6:     3.94 ms 
    [network-tester-4]2016-07-20T16:50:33.455264146Z 6195245d->0facb879:     2.90 ms | 6195245d->264d48bc:     2.49 ms | 6195245d->6f989aef:     5.60 ms | 6195245d->f17488a6:     0.24 ms 
    [network-tester-3]2016-07-20T16:50:33.658858667Z d24ca418->0facb879:     0.20 ms | d24ca418->264d48bc:     8.10 ms | d24ca418->6f989aef:     5.53 ms | d24ca418->f17488a6:     2.38 ms 
    [network-tester-2]2016-07-20T16:50:36.557740521Z e9155705->0facb879:     2.74 ms | e9155705->264d48bc:     0.20 ms | e9155705->6f989aef:     4.31 ms | e9155705->f17488a6:     1.69 ms 
    [network-tester-1]2016-07-20T16:50:38.465712062Z 4ec75006->0facb879:     3.57 ms | 4ec75006->264d48bc:     8.25 ms | 4ec75006->6f989aef:     0.84 ms | 4ec75006->f17488a6:     4.20 ms 
    [network-tester-4]2016-07-20T16:50:38.676385101Z 6195245d->0facb879:     4.86 ms | 6195245d->264d48bc:     2.44 ms | 6195245d->6f989aef:     6.98 ms | 6195245d->f17488a6:     0.20 ms 
    [network-tester-3]2016-07-20T16:50:38.893413767Z d24ca418->0facb879:     0.22 ms | d24ca418->264d48bc:     5.48 ms | d24ca418->6f989aef:     3.24 ms | d24ca418->f17488a6:     2.57 ms 
    [network-tester-2]2016-07-20T16:50:41.783308575Z e9155705->0facb879:    16.02 ms | e9155705->264d48bc:     0.27 ms | e9155705->6f989aef:     5.33 ms | e9155705->f17488a6:     2.26 ms 
    [network-tester-1]2016-07-20T16:50:43.690646265Z 4ec75006->0facb879:     5.65 ms | 4ec75006->264d48bc:    13.09 ms | 4ec75006->6f989aef:     0.70 ms | 4ec75006->f17488a6:     7.60 ms 
    [network-tester-4]2016-07-20T16:50:43.899900045Z 6195245d->0facb879:     1.82 ms | 6195245d->264d48bc:     2.15 ms | 6195245d->6f989aef:     4.10 ms | 6195245d->f17488a6:     0.20 ms 
    [network-tester-3]2016-07-20T16:50:44.117530184Z d24ca418->0facb879:     0.20 ms | d24ca418->264d48bc:     4.31 ms | d24ca418->6f989aef:     7.27 ms | d24ca418->f17488a6:     1.90 ms 
    [network-tester-2]2016-07-20T16:50:47.011318295Z e9155705->0facb879:    14.78 ms | e9155705->264d48bc:     0.20 ms | e9155705->6f989aef:     5.22 ms | e9155705->f17488a6:     2.34 ms 
    [network-tester-1]2016-07-20T16:50:48.945198928Z 4ec75006->0facb879:     5.19 ms | 4ec75006->264d48bc:     7.65 ms | 4ec75006->6f989aef:     0.43 ms | 4ec75006->f17488a6:    12.99 ms


# Settings

* `POLLING_PERIOD` (default `5`): Wait this number of seconds between checks
* `PING_THRESHOLD_MS` (default `0`): Log only pings with a RTT longer than this number of milliseconds. Pings that fail are always logged