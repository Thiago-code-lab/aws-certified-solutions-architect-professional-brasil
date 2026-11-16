# Flashcards - Hybrid Connectivity

1. When should you choose Direct Connect? When latency, throughput and predictability justify its cost and provisioning lead time.
2. When is VPN sufficient? Temporary connectivity, lower-cost requirements or backup connectivity.
3. Why combine DX and VPN? To provide a dedicated path with backup connectivity or IPsec encryption.
4. When should you use DXGW? To associate Direct Connect connectivity with VPCs or TGWs without coupling it to a single VPC.
5. When is TGW preferable to VGW? With many VPCs, accounts and centralized segmentation requirements.
6. What indicates an inbound Resolver endpoint? On-premises systems need to resolve private AWS names.
7. What indicates an outbound Resolver endpoint? AWS workloads need to resolve corporate DNS zones.
8. What does BGP provide? Dynamic route exchange and attributes used for route preference and failover.
9. What is a DX pitfall? Assuming a dedicated connection removes the need for redundancy or encryption.
10. What defines good hybrid connectivity? Controlled routes, redundant paths, predictable DNS and tested failure behavior.
