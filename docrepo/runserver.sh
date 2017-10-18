#!/usr/bin/env bash

IP=$1
PORT=$2

if [ "$IP" == "" ]
then
    IP="0.0.0.0"
fi

if [ "$PORT" == "" ]
then
    PORT="8000"
fi

./manage.py runserver $IP:$PORT