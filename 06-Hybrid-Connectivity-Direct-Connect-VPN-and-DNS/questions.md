# Questions - Hybrid Connectivity

## Question 1

A company must connect hundreds of workloads across multiple AWS accounts to its data center with low latency variation. Which architecture best meets this requirement?

A) A VPN for each VPC.
B) Direct Connect to a DXGW associated with a central Transit Gateway.
C) Peering between every VPC.
D) PrivateLink for all traffic.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

DX provides predictable connectivity, while DXGW and TGW support multi-account scale. The other options either do not scale appropriately or address a different purpose.
</details>

## Question 2

A financial institution requires a dedicated connection and controlled encryption between its on-premises environment and AWS. What should it choose?

A) Direct Connect alone.
B) Direct Connect with VPN over the connection, or MACsec where applicable.
C) An Internet Gateway.
D) VPC Peering.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

A dedicated DX connection does not automatically provide end-to-end encryption. A ignores the encryption requirement; C and D do not meet the connectivity requirements. VPN provides IPsec encryption; MACsec protects supported dedicated connection segments and is suitable only when that scope meets the requirement.
</details>

## Question 3

An ERP system uses DX as its primary connection and can tolerate degraded performance, but cannot accept a total connectivity outage. Which design is best?

A) A single DX connection.
B) Redundant DX connections or a backup VPN with BGP, route preferences and failover testing.
C) More EC2 instances.
D) An additional NAT gateway.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

The risk lies in the hybrid connection. The backup must be routable, tested and sized for the acceptable degraded mode. C and D do not address connectivity failure.
</details>

## Question 4

AWS workloads need to resolve `corp.local`, and on-premises systems need to resolve private AWS names. What should you use?

A) Only private hosted zones.
B) An outbound Resolver endpoint for AWS -> on-premises and an inbound endpoint for on-premises -> AWS.
C) Public hosted zones.
D) Manual copying.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

Inbound and outbound endpoints serve different query directions. The other options are incomplete, unsuitable for private DNS or operationally impractical. Configure forwarding rules, network routes and security controls as well as the endpoints.
</details>

## Question 5

How can you prevent lateral reachability between production and development in shared hybrid connectivity?

A) One TGW route table propagating every route.
B) TGW route tables for separate domains with selective propagation.
C) Full peering.
D) A single VPC.

<details><summary><strong>Show answer</strong></summary>

**Correct answer:** B

Separate route tables control the routes available to each domain. The other options expand the blast radius. Validate both traffic directions and on-premises routing to prevent a bypass through the shared network.
</details>
