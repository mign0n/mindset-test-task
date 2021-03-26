# Forecasting customer churn

## Intro  
This is a web service that allows you to predict the probability of outflow of
insurance company customers.  
Every year, the company extends the CASCO policies of its individual customers.
To optimize the work with customer lists, you need to predict the probability
with which each of the customers contract will be prolonged and what factors will
affect it. Depending on this, priorities are set for call center operators who
process the list (make calls to customers), and decisions are made about additional
motivation for customers to prolong.  
The service is based on a pre-trained [CatBoost](https://catboost.ai/) classifier model.

## Steps to run server on Linux  
1. Open a terminal, create a directory and navigate to it.  
```shell
~$ mkdir mindset && cd mindset
```
2. Clone the repository and navigate to `mindset-test-task` directory.  
```shell
~/mindset$ git clone https://github.com/mign0n/mindset-test-task.git
```
```shell
~/mindset$ cd mindset-test-task
```
3. Create virtual environment and activate it.  
```shell
~/mindset/mindset-test-task$ python -m venv env
```
```shell
~/mindset/mindset-test-task$ source env/bin/activate
```
4. Install requirements.  
```shell
(env) ~/mindset/mindset-test-task$ pip install -r requirements.txt
```
5. Run server.
```shell
(env) ~/mindset/mindset-test-task$ ./run.sh
```
6. Go to http://127.0.0.1:5000

## Steps to run server in Docker container
1. Open a terminal, create a directory and navigate to it.  
```shell
~$ mkdir mindset && cd mindset
```
2. Clone the repository and navigate to `mindset-test-task` directory.  
```shell
~/mindset$ git clone https://github.com/mign0n/mindset-test-task.git
```
```shell
~/mindset$ cd mindset-test-task
```
3. Run script `run-docker`.
```shell
~/mindset/mindset-test-task$ bash ./run-docker.sh
```
4. Go to http://127.0.0.1:5000
