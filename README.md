# Django basicsite Project

## Getting Started with Project setup


### Creating Virtual Environment:
```bash
# Create a virual environment. 
# Go to following link if you do not know how to do it 
# <script src="https://gist.github.com/simonw/4835a22c79a8d3c29dd155c716b19e16.js"></script>
```
### One Liner Script:
```bash

curl https://raw.githubusercontent.com/faisy0001/basicsite/master/install.sh | bash

# Now,go to http://localhost:8000/accounts ,you will see a login\signup page.

```

## Useful make commands:
```bash
# start services
make up

# start services in detached mode
make up-d

# restart the service containers
make restart

# see web logs 
make logs

# attach to python shell
make shell

# generate migrations
make migrations

# apply migrations
make migrate

# stop services
make stop

# remove service containers
make down
```
