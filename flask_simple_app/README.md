# Simple Flask App

This is a starter template for simple flask application with self signed SSL certificates and deployment with docker.
## Linux:
### System dependencies:
* openssl
* docker
* python3.7 or higher
### Run instructions:
Once you've installed all system dependencies, simply type "make" from the command line. When it's done building, navigate to "https://0.0.0.0:7000" to see the landing page.

### Manual setup instructions for development:
1. Create and activate virtual environment: 
    * `~$ cd <project_path>`
    * `~/flask_simple_app$ python -m venv venv`
    * `~/flask_simple_app$ source venv/bin/activate`

2. Install requirements:
    * `~/flask_simple_app$ pip install -r requirements.txt`

3. Create `.env` file if you want to change config values:
    * `~/flask_simple_app$ touch .env`
    
4. Run web service:
    * `~/flask_simple_app$ python app.py`

## Docker:
1. Create `.env` file if you want to change config values:
   * `~/flask_simple_app$ touch .env `
   
2. Build image:
   * `~/flask_simple_app$ docker build -t <yourtag> .`

3. Run:
   * `~/flask_simple_app$ docker run --name flask_simple_app -d -p <host_post>:<port_in_containter> <image>`

4. Access container:
   * `~/flask_simple_app$ docker exec -it <container_id> bash`
   
5. Follow container logs:
   * `~/flask_simple_app$ docker logs --tail 200 -f <container_id>`

By default you can find logs for container at the `/var/lib/docker/<container_id>`. You can switch to root 

`sudo su -` 

to access this folder.