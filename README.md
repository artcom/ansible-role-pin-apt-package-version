# Pin apt package version
Ansible role to pin the version of an apt package using apt preferences.

## Role Variables
Available variables are listed below, along with default values `(see defaults/main.yml)`:
```yaml
package_name: null
package_version: null
```
This will create the file `/etc/apt/preferences.d/<package_name>.pref` with content:
```
Explanation: Pin added by Ansible role "pin-apt-package-version"
Package: <package_name>
Pin: version <package_version>
Pin-Priority: 600
```
`package_version` should be set according to the [apt_preferences man page](http://manpages.ubuntu.com/manpages/bionic/man5/apt_preferences.5.html) and can use wildcards.

## Test
### Requirements
- python >= 3.7
- docker

### Run
```bash
pip install -r requirements.txt
molecule test
```
