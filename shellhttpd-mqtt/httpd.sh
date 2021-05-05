#!/bin/sh
PORT="${PORT-8082}"
ACCESS=0
while true; do
	RESPONSE="HTTP/1.1 200 OK\r\n\r\nNumber of Access = ${ACCESS}\r\n"
	echo -en "$RESPONSE" | nc -l -p "${PORT}" > ./tmp.log || true
	if grep -q "GET / HTTP/1.1" ./tmp.log; then
		ACCESS=$((ACCESS+1))
		echo "Number of Access = $ACCESS"
		mosquitto_pub -h localhost -t "containers/requests" -m "ACCESS=$ACCESS"
		echo "----------------------"
	fi
done
