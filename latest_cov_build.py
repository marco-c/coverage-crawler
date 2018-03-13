import tarfile
import sys
import json
import os
from urllib import urlretrieve, urlencode
from urllib2 import urlopen


def get_json(url, params=None):
    if params is not None:
        url += '?' + urlencode(params)

    r = urlopen(url).read().decode('utf-8')

    return json.loads(r)

last_task = get_json('https://index.taskcluster.net/v1/task/gecko.v2.mozilla-central.latest.firefox.linux64-ccov-opt')
taskId = last_task['taskId']
name = os.path.join('ccov-artifacts', taskId + 'artifacts.public.build.target.tar.bz2')
urlretrieve('https://queue.taskcluster.net/v1/task/' + taskId + '/artifacts/public/build/target.tar.bz2', name)
tar = tarfile.open(name, 'r:bz2')
tar.extractall()
tar.close()
# target.tar.bz2 deleted
os.remove(name)
