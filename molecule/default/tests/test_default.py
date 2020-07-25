import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hashicorp_stable_repo(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
        c = host.run('apt-cache search nomad').rc
    else:
        c = host.run('yum --disablerepo="*" --enablerepo="hashicorp" \
        list available').rc

    assert c == 0


def test_hashicorp_test_repo(host):
    c = 0
    if host.system_info.distribution not in ['debian', 'ubuntu']:
        c = host.run('yum --disablerepo="*" --enablerepo="hashicorp-test" \
        list available').rc

    assert c == 0
