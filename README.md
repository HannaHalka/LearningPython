$$
\begin{aligned}
\text{outfrom-fsm} &= (r_0 + S_15) \oplus r_1 \\
S_0                &= \text{alpha-mul}(S_0 \oplus S_{13} \oplus \text{alphainv-mul}(S_{11} \oplus \text{outfrom-fsm})) \\
\text{fsmtmp}      &= r_1 + S_13 \\
r_1                &= T(r_0) \\
r_0                &= \text{fsmtmp} \\
 & & \\
\text{outfrom-fsm} &= (r_0 + S_{15}) \oplus r_1 \\
S_1                &= \text{alpha-mul}(S_1 \oplus S_{14} \oplus \text{alphainv-mul}(S_{12} \oplus \text{outfrom-fsm})) \\
\text{fsmtmp}      &= r_1 + S_14 \\
r_1                &= T(r_0) \\
r_0                &= \text{fsmtmp} \\
 & & \\
\text{outfrom-fsm} &= (r_0 + S_1) \oplus r_1 \\
S_2                &= \text{alpha-mul}(S_2 \oplus S_{15} \oplus \text{alphainv-mul}(S_{13} \oplus \text{outfrom-fsm})) \\
\text{fsmtmp}      &= r_1 + S_15 \\
r_1                &= T(r_0) \\
r_0                &= \text{fsmtmp} \\
 \text{ ... } & \text{ ... } \\
 \text{ ... } & \text{ ... } \\
 \text{ ... } & \text{ ... } \\
\text{outfrom-fsm} &= (r_0 + S_{14}) \oplus r_1 \\
S_{15}             &= \text{alpha-mul}(S_{15} \oplus S_{12} \oplus \text{alphainv-mul}(S_{10} \oplus \text{outfrom-fsm})) \\
\text{fsmtmp}      &= r_1 + S_12 \\
r_1                &= T(r_0) \\
r_0                &= \text{fsmtmp} \\
 & & \\
\end{aligned}
$$
