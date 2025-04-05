# Digital Party Planner 🎉

This is a Python-based web application that helps plan your ideal party using bitwise operations!

## Features

- Choose from 15 different party items
- Generate a unique **Party Code** using bitwise AND operations
- Get a fun message based on the result
- Web interface using HTML form
- Deployed on two EC2 instances with a Load Balancer
- Version controlled with Git using branches: `main`, `development`, and `feature1`

## How to Run

1. Launch 2 Amazon Linux 2 EC2 instances
2. Install Apache, Python, and Git
3. Copy the `party_planner.py` script into `/var/www/cgi-bin/`
4. Make it executable:
   ```bash
   chmod +x /var/www/cgi-bin/party_planner.py
