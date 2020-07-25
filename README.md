gabops.hashicorp_repo
=====================
![Molecule CI](https://github.com/gabops/ansible-role-hashicorp-repo/workflows/Molecule%20CI/badge.svg?branch=master)

Installs and configures Hashicorp repository.

Requirements
------------

None.

Role Variables
--------------

| Variable | Default value | Description |
| :--- | :--- | :--- |
| hashicorp_repo_stable_state | present | Controls the state of the repository. Possible values are 'present' or 'absent'. |
| hashicorp_repo_stable_enabled | true | Controls whether or not the repo is enabled. Only used if `hashicorp_repo_stable_state` is set to 'present'. |
| hashicorp_repo_test_state | absent | Controls the state of the test repository. Possible values are 'present' or 'absent'. Note this option is only used on RedHat family os. |
| hashicorp_repo_test_enabled | false | Controls whether or not the test repo is enabled. Only used if `hashicorp_repo_test_state` is set to 'present'. Note this option is only used on RedHat family os. |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  vars:
    hashicorp_repo_stable_enabled: false
  roles:
     - role: gabops.hashicorp_repo
```

License
-------

[MIT]((./LICENSE))

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops))
