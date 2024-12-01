# This project is part of a High-interaction honeypot.

DISCLAIMER: !!! ONLY FOR EDUCATIONAL PURPOSES !!!

The goal of this project is to simulate a network containing multiple honeypots to study and analyze potential cyberattacks. The implementation of these honeypots is designed to capture and log attacker activities in real-time, which will be useful for understanding attack methods and enhancing security measures. Please note that this project is intended solely for educational purposes and should not be used for malicious activities or unauthorized testing.

----------------------------------------------------------------------------------------------------------------------------------------------------

For simulating virtual machines download VHD images (unfortunately it is big :( stupid azure export )

make network with 4 VMs:

1. cowrie : https://md-b0pm20kcsc4n.z12.blob.storage.azure.net/nwhvzx22rszl/abcd?sv=2018-03-28&sr=b&si=9a825b94-2ee3-4a47-ad54-a3d1833d1862&sig=SeJEb56d28IUtT1RJ2iQftKdSIMBUZzYlz4XcXnJBCE%3D
    - ssh to real connection on 33333 port,
    - username: bit
    - password: bit123456 or bit1234567890!
    - for cowrie logs needed to switch users to user "cowrie"
2. t-pot : (pribudne po prezentacii)
    - ssh to real connection on 64295 port
    - dashboard on port 64297 (username: bit, password: bit123456)
    - username: bit
    - password: bit123456 or bit1234567890!
2. mongoDB : https://md-hdd-wtjbw1zrrsjx.z44.blob.storage.azure.net/s00pq43fqv0s/abcd?sv=2018-03-28&sr=b&si=8b3b16c0-babd-4798-a359-f4992518d5d8&sig=24Qwt5MfGzOH6QppvEEIRryDVslY%2B%2FiaLflDI1EfXok%3D
    - username: bit
    - password: bit123456 or bit1234567890!

4. honeythings : https://md-ssd-bncbcpzn1g30.z7.blob.storage.azure.net/pm2w4drsnw2k/abcd?sv=2018-03-28&sr=b&si=745b4650-71cf-4a13-a3a1-106d3319fb7b&sig=og4LuzmCU5ajZl6jnO1i%2FS0RoSpMlqAy0sAQAXYdyd0%3D 
    - username: bit
    - password: Bit1234567890

Have fun :)