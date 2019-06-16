[{"id":"18758c26.2c91c4","type":"ui_switch","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Enable","topic":"hydro/beer_enable","group":"Brewing control","order":1,"onvalue":"true","offvalue":"false","x":100,"y":160,"wires":[["4c68f5aa.da329c"]]},{"id":"4c68f5aa.da329c","type":"mqtt out","z":"cad785e7.7ca968","name":"","topic":"","qos":"","retain":"","broker":"66c8bac8.b99464","x":310,"y":160,"wires":[]},{"id":"119a8fe7.47ddf","type":"mqtt in","z":"cad785e7.7ca968","name":"","topic":"hydro/beer_temp","qos":"0","datatype":"utf8","broker":"66c8bac8.b99464","x":460,"y":160,"wires":[["4cbb77a1.6f67a8","4a370b23.6b2714"]]},{"id":"4cbb77a1.6f67a8","type":"ui_chart","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Temperature","group":"Brewing Feedback","order":"5","interpolate":"linear","nodata":"No Data","removeOlder":"12","removeOlderUnit":"3600","x":690,"y":80,"wires":[[],[]]},{"id":"60bf4303.25ad8c","type":"ui_numeric","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Setpoint","topic":"hydro/beer_setp","group":"Brewing control","order":"2","format":"{{value}}","min":"15","max":"25","x":100,"y":80,"wires":[["4c68f5aa.da329c"]]},{"id":"9a8214bf.b5a368","type":"mqtt in","z":"cad785e7.7ca968","name":"","topic":"hydro/beer_time","qos":"0","datatype":"utf8","broker":"66c8bac8.b99464","x":280,"y":240,"wires":[["4db8dd19.75b974"]]},{"id":"4db8dd19.75b974","type":"ui_text","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Time","group":"Brewing Feedback","order":"1","format":"{{msg.payload}}","x":510,"y":240,"wires":[]},{"id":"1af213f7.cf93fc","type":"ui_text","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Irrigations","group":"Irrigation ","order":"5","format":"{{msg.payload}}","x":540,"y":600,"wires":[]},{"id":"40006101.c9ea3","type":"mqtt in","z":"cad785e7.7ca968","name":"","topic":"hydro/irrigation_cnt","qos":"0","datatype":"utf8","broker":"66c8bac8.b99464","x":270,"y":600,"wires":[["1af213f7.cf93fc"]]},{"id":"e056dcbb.26757","type":"mqtt in","z":"cad785e7.7ca968","name":"","topic":"hydro/hours_no_water","qos":"0","datatype":"utf8","broker":"66c8bac8.b99464","x":260,"y":540,"wires":[["c3073153.1a8e7"]]},{"id":"c3073153.1a8e7","type":"ui_text","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"hours no water","group":"Irrigation ","order":"4","format":"{{msg.payload}}","x":560,"y":540,"wires":[]},{"id":"e9369853.22a4a8","type":"ui_text","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"last irrigation","group":"Irrigation ","order":"3","format":"{{msg.payload}}","x":550,"y":500,"wires":[]},{"id":"ef0cde13.efd13","type":"mqtt in","z":"cad785e7.7ca968","name":"","topic":"hydro/last_irrigation","qos":"0","datatype":"utf8","broker":"66c8bac8.b99464","x":270,"y":500,"wires":[["e9369853.22a4a8"]]},{"id":"88c07628.646e78","type":"ui_switch","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Auto","topic":"hydro/irrigation_auto","group":"Irrigation ","order":1,"onvalue":"true","offvalue":"false","x":310,"y":420,"wires":[["9c5f6b53.0bc9f8"]]},{"id":"9c5f6b53.0bc9f8","type":"mqtt out","z":"cad785e7.7ca968","name":"enable","topic":"","qos":"","retain":"","broker":"66c8bac8.b99464","x":530,"y":420,"wires":[]},{"id":"9c0ab08d.17aa9","type":"ui_switch","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Manual","topic":"hydro/irrigation_manual","group":"Irrigation ","order":"2","onvalue":"true","offvalue":"false","x":300,"y":460,"wires":[["e11e2694.f60838"]]},{"id":"e11e2694.f60838","type":"mqtt out","z":"cad785e7.7ca968","name":"enable","topic":"","qos":"","retain":"","broker":"66c8bac8.b99464","x":530,"y":460,"wires":[]},{"id":"7ec1b397.73f0dc","type":"mqtt in","z":"cad785e7.7ca968","name":"","topic":"hydro/beer_heating","qos":"0","datatype":"utf8","broker":"66c8bac8.b99464","x":290,"y":300,"wires":[["f80f83a.c80b98","64bdd812.4d6cf8"]]},{"id":"f80f83a.c80b98","type":"ui_text","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Heater","group":"Brewing Feedback","order":"2","format":"{{msg.payload}}","x":510,"y":300,"wires":[]},{"id":"4a370b23.6b2714","type":"ui_text","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Temperature","group":"Brewing Feedback","order":"3","format":"{{msg.payload}}","x":530,"y":340,"wires":[]},{"id":"f5f73b95.7adea8","type":"ui_chart","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Heater","group":"Brewing Feedback","order":"7","interpolate":"step-after","nodata":"No Data","removeOlder":"12","removeOlderUnit":"3600","x":670,"y":380,"wires":[[],[]]},{"id":"64bdd812.4d6cf8","type":"function","z":"cad785e7.7ca968","name":"Bool2Num","func":"if (msg.payload === \"True\") {\n    msg.payload=1\n} else {\n    msg.payload=0\n}\nreturn msg","outputs":1,"noerr":0,"x":430,"y":380,"wires":[["f5f73b95.7adea8","4f15bc6e.3a7024"]]},{"id":"4f15bc6e.3a7024","type":"debug","z":"cad785e7.7ca968","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"false","x":690,"y":300,"wires":[]},{"id":"2cbc7248.fa3dee","type":"ui_text","z":"cad785e7.7ca968","tab":"78428f07.e9148","name":"Heater","group":"Brewing Feedback","order":"6","format":"{{msg.payload}}","x":670,"y":340,"wires":[]},{"id":"137d5e7d.f08732","type":"inject","z":"cad785e7.7ca968","name":"","topic":"","payload":"false","payloadType":"bool","repeat":"","crontab":"","once":true,"onceDelay":0.1,"x":70,"y":280,"wires":[["18758c26.2c91c4"]]},{"id":"85b21bf1.619068","type":"inject","z":"cad785e7.7ca968","name":"","topic":"","payload":"15","payloadType":"num","repeat":"","crontab":"","once":true,"onceDelay":0.1,"x":90,"y":40,"wires":[["60bf4303.25ad8c"]]},{"id":"78428f07.e9148","type":"ui_tab","z":"","name":"Home","icon":"dashboard","order":"1"},{"id":"66c8bac8.b99464","type":"mqtt-broker","z":"","name":"pimoz","broker":"192.168.1.4","port":"1883","clientid":"test-client","usetls":false,"compatmode":true,"keepalive":"60","cleansession":true,"birthTopic":"","birthQos":"0","birthPayload":"","closeTopic":"","closeQos":"0","closePayload":"","willTopic":"","willQos":"0","willPayload":""}]
