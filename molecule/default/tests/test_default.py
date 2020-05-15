import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_python3_version_pinned(host):
    versions = {
        "bionic": "3.6.7-1~18.04",
        "focal": "3.8.2-0ubuntu2",
        "xenial": "3.5.1-3",
        "buster": "3.7.3-1"
    }
    host_release = host.ansible(
        "setup"
    )["ansible_facts"]["ansible_distribution_release"]
    file_content = [
        'Explanation: Pin added by Ansible role "pin-apt-package-version"',
        'Package: python3',
        'Pin: version {}'.format(versions[host_release]),
        'Pin-Priority: 600',
        ''
    ]
    pref_file = host.file('/etc/apt/preferences.d/python3.pref')

    assert pref_file.exists
    assert pref_file.is_file
    assert pref_file.user == 'root'
    assert pref_file.group == 'root'
    assert oct(pref_file.mode) == '0o640'
    assert pref_file.content_string == '\n'.join(file_content)


def test_package_policy(host):
    versions = {
        "bionic": "3.6.7-1~18.04",
        "focal": "3.8.2-0ubuntu2",
        "xenial": "3.5.1-3",
        "buster": "3.7.3-1"
    }
    host_release = host.ansible(
        "setup"
    )["ansible_facts"]["ansible_distribution_release"]

    assert host.check_output(
        'apt-cache policy python3 | grep 600'
    ) == ' *** {} 600'.format(versions[host_release])
