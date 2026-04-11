``def next_stream()``:

$$
\begin{aligned}
S_0                 &= \text{alpha-mul}(S_0 \oplus S_{13} \oplus \text{alphainv-mul}(S_{11})) \\
\text{fsmtmp}       &= r_1 + S_{13} \\
r_1                 &= T(r_0) \\
r_0                 &= \text{fsmtmp} \\
\text{out-stream}_0 &= r_0 + S_0 \oplus r_1 \oplus S_1  \leftarrow \text{FSM()}\\
& & \\
S_1                &= \text{alpha-mul}(S_1 \oplus S_{14} \oplus \text{alphainv-mul}(S_{12})) \\
\text{fsmtmp}      &= r_1 + S_{14} \\
r_1                &= T(r_0) \\
r_0                &= \text{fsmtmp} \\
\text{out-stream}_1 &= r_0 + S_1 \oplus r_1 \oplus S_2 \\
 & & \\
S_2                &= \text{alpha-mul}(S_2 \oplus S_{15} \oplus \text{alphainv-mul}(S_{13})) \\
\text{fsmtmp}      &= r_1 + S_{15} \\
r_1                &= T(r_0) \\
r_0                &= \text{fsmtmp} \\
\text{out-stream}_2 &= r_0 + S_2 \oplus r_1 \oplus S_3 \\ 
 \text{ ... } & \text{ ... } \\
 \text{ ... } & \text{ ... } \\
 \text{ ... } & \text{ ... } \\
S_{15}                &= \text{alpha-mul}(S_{15} \oplus S_{12} \oplus \text{alphainv-mul}(S_{10})) \\
\text{fsmtmp}      &= r_1 + S_{12} \\
r_1                &= T(r_0) \\
r_0                &= \text{fsmtmp} \\
\text{out-stream}_{15} &= r_0 + S_{15} \oplus r_1 \oplus S_0 \\
 & \\
\end{aligned}
$$
