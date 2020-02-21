# Pin apt package version
Ansible role to pin the version of an apt package using apt-mark hold.

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
pin_apt_packages_version_packages: []
```

## Test
### Requirements
- python >= 3.7
- docker

### Run
```bash
pip install -r requirements.txt
molecule test
```
