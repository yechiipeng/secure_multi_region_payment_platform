#Security Observation — Internal Service Port (8000)
1. Initial Concern

The application container listens on port 8000, could this introduce an unnecessary attack surface?


2. Context Analysis

Port 8000 is a non-privileged port (>1024).

It is commonly used for development servers (e.g., FastAPI).

The container binds to 0.0.0.0 internally.

Current deployment stage: local / containerized dev.

Not publicly exposed via cloud security group.

3. Threat Scenario Considered

If port 8000 were exposed publicly (e.g., security group allows 0.0.0.0/0), an attacker could directly interact with the API without TLS termination or upstream filtering.


4. Risk Assessment
|Condition|	Present?|	Notes|
|Public exposure|	No|	Not exposed outside container|
|TLS enforced|	Planned at ingress|	Will terminate at load balancer|
|Authentication|	Not yet implemented|	API currently unauthenticated|
|Firewall restriction|	Yes (planned in Terraform)|	Only 443 will be public|

Conclusion:

Risk level: Low in current state (development only), becomes High if misconfigured in production.


5. Decision

Port 8000 retained for internal container communication.

External exposure restricted to HTTPS (443) via ingress/load balancer.

Security groups will deny inbound 8000 from public networks.
