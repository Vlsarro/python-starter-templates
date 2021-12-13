# Simple Flask app (Python 3.7)

## Linux:
1. Create and activate virtual environment: 
    * ``` ~$ cd <project_path>```
    * ```~/flask_simple_app$ python -m venv venv```
    * ```~/flask_simple_app$ source venv/bin/activate```

2. Install requirements:
    * ```~/flask_simple_app$ pip install -r requirements.txt```

3. Create ```.env``` file if you want to change config values:
    * ```~/flask_simple_app$ touch .env```
    
4. Run web service:
    * ```~/flask_simple_app$ python app.py```

## Docker:
1. Create ```.env``` file if you want to change config values:
   * ```~/flask_simple_app$ touch .env ```
   
2. Build image:
   * ```~/flask_simple_app$ docker build -t <yourtag> .```

3. Run:
   * ```~/flask_simple_app$ docker run -d -p <host_post>:<port_in_containter> <image>```

4. Access container:
   * ```docker exec -it <container_id> bash```