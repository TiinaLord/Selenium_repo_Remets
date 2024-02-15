FROM python:3.10.12-alpine
WORKDIR /home/user/Selenium_repo_Remets/
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest", "tests/test_find_elements.py", "tests/test_new_oop", "tests/test_scenario",  "--browser=chrome", "--url=http://192.168.0.111:8081", "--log_level=DEBUG", "--executor=192.168.0.111", "--platform=Linux", "--vnc", "--logs"]

