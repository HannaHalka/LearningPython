$$
\begin{aligned}
                   & \text{equation}                                                                                   & \text{First Iteration } & \text{ Second Iteration} \\
\text{outfrom_fsm} &= (r_0 + S_15) \oplus r_1                                                                          & = 18374403900871474942  &= 12725935957224475632    \\
S_0                &= \text{alpha_mul}(S_0 \oplus S_{13} \oplus \text{alphainv_mul}(S_{11} \oplus \text{outfrom_fsm})) &= 5187521150956601601    &=                         \\
\text{fsmtmp}      &= r_1 + S_13                                                                                       &= 18374403900871474942   &=                         \\
r_1 &= T(r_0)      &= 1506115696707685439                                                                              &=                                                   \\
r_0                &= \text{fsmtmp}                                                                                    &= 18374403900871474942   &=                         \\
 & & & \\
\end{aligned}
$$
