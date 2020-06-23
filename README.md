Ansible role for artifactory-pip
==================================

Configures pip to use Artifactory repos

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-artifactory-pip/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-artifactory-pip/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-artifactory-pip/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-artifactory-pip/actions?query=workflow%3A%22Release%22)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `artifactory_base_url` | URL of Artifactory instance | string | "" | true |
| `artifactory_user` | User whose pip instance needs to be configured to use Artifactory | string | root | true |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-artifactory-pip
```

License
-------

[Apache License](LICENSE)
