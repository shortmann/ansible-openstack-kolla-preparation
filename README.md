ansible-openstack-kolla-preparation
===================================

This role will prepare a centos 7 machine to enable the installation of OpenStack kolla.
https://docs.openstack.org/kolla-ansible/latest/user/quickstart.html


Role Variables
--------------

* `kolla_user`: molecule
* `kolla_group`: molecule
* `kolla_base_distro`: centos
* `kolla_install_type`: source
* `kolla_openstack_release`: rocky
* `kolla_network_interface`: eth0
* `kolla_neutron_external_interface`: eth1


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - { role: ansible-openstack-kolla-preparation }


Tests
-----

You can test the role with molecule
```sh
molecule test
```


License
-------

MIT

Author Information
------------------

Kai Kahllund <kai.kahllund@akra.de>
