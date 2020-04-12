# 0x13-firewall

## Tasks

### 0. Firewall ABC
Pick one answer for every question.

What is a firewall?
1. A hardware security system
2. A hardware or software security system
3. A software security system

What are the 2 types of firewall:
1. Soft and hard firewall
2. Incoming and outgoing firewall
3. Network and host-based firewall

What is the main function of a firewall?
1. To filter incoming and outgoing network traffic
2. To filter incoming and outgoing TCP traffic
3. To filter outgoing traffic

### 1. Block all incoming traffic but
Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:

* The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
* Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
  	    22 (SSH)
  	    443 (HTTPS SSL)
	    80 (HTTP)
* Share the ufw commands that you used in your answer file
