This project is maid for Ideco as a test task.
It is an asyncronous web service able to scan machines on 
the Internet. 
- To run application:
    - run python3 -m venv venv in project folder
    - run source venv/bin/activate
    - run swerver with python sswa/run_server.py
  
Tests are available wit python3 -m unittest test.py

- To make rpm packages:
   - Make sure you have rpm-build installed
   - run python3 setup.py bdist_rpm