# Hassio

## Installation

```bash
#First
sudo su -

#Then
curl -sL https://raw.githubusercontent.com/home-assistant/hassio-build/master/install/hassio_install | bash -s -- -m intel-nuc
```

## Stop

```bash
systemctl stop hassio-apparmor.service && \
systemctl stop hassio-supervisor.service
```

## Start (not needed first time)

```bash
systemctl start hassio-apparmor.service && \
systemctl start hassio-supervisor.service
```
