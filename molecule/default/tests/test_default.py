import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_services_running_and_enabled(host):
    assert host.service('prometheus-resque-exporter').is_enabled
    assert host.service('prometheus-resque-exporter').is_running


def test_node_exporter_metrics(host):
    out = host.check_output('curl http://localhost:9447/metrics')
    assert 'resque_up' in out
