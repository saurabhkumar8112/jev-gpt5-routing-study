# Companion thread

1/3 Tested Jev + GPT-5 routing on Banking77: 500 tune cases, then 500 evaluation cases. Real API outputs; routing evaluated offline. A frozen confidence gate sent 35% of evaluation requests to GPT-5.

2/3 Evaluation accuracy / API cost per million:
Jev: 83.2% / $71
GPT-5: 86.4% / $2,247
Cascade: 86.0% / $1,183
The cascade cut cost 47.3%, but missed our accuracy-parity criterion by 2 answers out of 500. Equal quality was not established.

3/3 Escalated GPT-5 calls were 41% more expensive than average. Use per-request fallback costs, not fallback rate × average cost. This is one reused public sample, not a production guarantee or evidence of 50× equal-quality savings.
