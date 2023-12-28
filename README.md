# Coding Chalanges
A collection of coding problem solutions from different coding platforms or coding bank.

### SSH connection
```
# generate SSH key with your email address
ssh-keygen -t ed25519 -C "your_email@example.com"
```
```
# adding SSH key in local machine
ssh-add /c/Users/YOU/.ssh/id_ed25519
```
```
# start the ssh-agent in the background
$ eval "$(ssh-agent -s)"
> Agent pid 59566
```
```
# Find and take a note of your public key fingerprint.
$ ssh-add -l -E sha256
> 2048 SHA256:274ffWxgaxq/tSINAykStUL7XWyRNcRTlcST1Ei7gBQ /Users/USERNAME/.ssh/id_rsa (RSA)
```

## Docker
- `docker ps`, list all running containers
- `docker-compose up --build`, rebuild and start up the docker services
- `docker exec -it <containerID> sh`, interact the container of specific container ID with shell
- `docker run -it <imageID> sh`, start a new container in foreground by image ID with shell

## Testing
- `$ pip install -U pytest`, install pytest testing framework
- `pytest --version`, check current pytest version
- `$ pytest <filename>`, test the assertion statements in the file
- `assert s1 == s2`, assertion statement example in python code, s1 and s2 are 2 objects

