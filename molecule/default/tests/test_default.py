import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_kolla_cli(host):
    """ Tests the kolla cli """
    venv = 'source $HOME/.venv/bin/activate'
    command = 'kolla-ansible'
    kolla = host.run('{venv} && {command}'.format(
        venv=venv,
        command=command
    ))

    assert kolla.rc == 0


# def test_kolla_bootstrap(host):
#     """ Tests the kolla bootstrap command (will not work with docker) """
#     venv = 'source $HOME/.venv/bin/activate'
#     command = 'kolla-ansible -i $HOME/kolla/all-in-one bootstrap-servers'
#     bootstrap = host.run('{venv} && {command}'.format(
#         venv=venv,
#         command=command
#     ))

#     assert bootstrap.rc == 0


# def test_kolla_prechecks(host):
#     """ Tests the kolla prechecks command (will not work with docker) """
#     venv = 'source $HOME/.venv/bin/activate'
#     command = 'kolla-ansible -i $HOME/kolla/all-in-one prechecks'
#     prechecks = host.run('{venv} && {command}'.format(
#         venv=venv,
#         command=command
#     ))

#     assert prechecks.rc == 0
