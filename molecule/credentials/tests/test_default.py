import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_host(host):
    cmd = host.run("pip download pip-install-test | sed -n 2p | grep artifactory")  # noqa 501
    assert cmd.succeeded
