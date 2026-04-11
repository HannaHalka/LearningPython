# Strumok

Strumok is the stream symmetric cipher. Encryption in this cipher we can divide into three main parts: `Initialization`, `Next strim`, and `Gamma strim` functions.
Since _Strumok stream_ is symetric encyption and decyption are performed with the same algorithm. 

![scheme of operation of the stream cipher](images/strumok.png)

## Algorithm Description

- ### Initialization function

As input initialization function takes 256-bit or  512-bit key _K_ and 256-bit _IV_ (Initialization Vector). 
And as output function produces $S_{0} = (s^{(0)}, r^{(0)})$, where $s_i = s_{15}^{(i)}, s_{14}^{(i)} , ..., s_1^{(i)}$ it's shift register with linear feedback, and $r_i = (r_1^{(i)}, r_2^{(i)})$ –– two registers of a finite state machine.

Then, we constructed first initial state  from _K_ and _IV_: $S_{-33} = (s^{(-33)}, r^{(-33)})$. 
We did it by filing s[0], s[1], ..., s[15], with values which derives from the _K_ and _IV_, and set r[0] and r[1] to zero.

$$
\begin{aligned}
K^{256} & & & K^{512} \\
S_{15}^{(-33)} & = \overline{K_3} & S_{15}^{(-33)} & = K_7 \\
S_{14}^{(-33)} & = K_2 & S_{14}^{(-33)} & = \overline{K_6} \\
S_{13}^{(-33)} & = \overline{K_1} & S_{13}^{(-33)} & = K_5 \\
S_{12}^{(-33)} & = K_0 & S_{12}^{(-33)} & = K_4 \\
S_{11}^{(-33)} & = K_3 & S_{11}^{(-33)} & = \overline{K_0} \\
S_{10}^{(-33)} & = \overline{K_2} & S_{10}^{(-33)} & = K_2 \\
S_9^{(-33)} & = K_1 & S_9^{(-33)} & = \overline{K_1} \\
S_8^{(-33)} & = K_0 & S_8^{(-33)} & = K_3 \oplus IV_0 \\
S_7^{(-33)} & = \overline{K_3} & S_7^{(-33)} & = \overline{K_7} \\
S_6^{(-33)} & = \overline{K_2} & S_6^{(-33)} & = K_6 \\
S_5^{(-33)} & = K_1 \oplus IV_0 & S_5^{(-33)} & = K_5 \oplus IV_1 \\
S_4^{(-33)} & = K_0 & S_4^{(-33)} & = K_4 \\
S_3^{(-33)} & = K_3 \oplus IV_1 & S_3^{(-33)} & = K_3 \oplus IV_2 \\
S_2^{(-33)} & = K_2 \oplus IV_2 & S_2^{(-33)} & = K_2 \\
S_1^{(-33)} & = K_1 & S_1^{(-33)} & = K_1 \\
S_0^{(-33)} & = K_0 \oplus IV_3 & S_0^{(-33)} & = K_0 \oplus IV_3
\end{aligned}
$$

Then for calculating $S_{-1} = Next^{32}(S_{-33}, INIT)$ we update s[i] by using `alpha_mul`, `alphainv_mul` 
and 2 full iteration update circles, which is same to 32 initialization takts.

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
 & \\
\end{aligned}
$$

**IMPORTANT:** While initialization we don't generate gamma.

And the last step is $S_0 = Next(S_{-1})$

- ### Next strim function

As input next strim function takes: $S_{i} = (s^{(i)}, r^{(i)})$ and in the next iteration function starts looking like: $S_{i+1} = (s^{(i+1)}, r^{(i+1)})$.

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

Again we use `alpha_mul` and  `alphainv_mul` for updating S[i], which we use for culculating FSM. After that we update our r[i] using FSM and function `T()`.

`T()` is nonlinear substitution function, it helps us with rearrangement of elements. This function is implementation of formula: $w_{i,j} = (u \gg i ) \oplus W_j$.

- ### Gamma strim function

- Input: $S_{i} = (s^{(i)}, r^{(i)})$
- Culculating: $Z_i = FSM(s_{15}^{(i)}, r_1^{(i)}, r_2^{(i)}) \oplus s_0^{(i)}$
- Output: $Z_i$

---

## Toy Example

```
K = [0101010101010101, (k_1)       IV = [0101010101010101, (iv_1)
     0101010101010101, (k_2)             0101010101010101, (iv_2)
     0101010101010101, (k_3)             0101010101010101, (iv_3)
     0101010101010101] (k_4)             0101010101010101] (iv_4)

```

In our example $K_i$ and $IV_i$ are 0101010101010101. 

* $\overline{0101010101010101} = 18374403900871474942$
* $0101010101010101 \oplus 0101010101010101 = 0$

Let's fill $S_i$ with our results.

$$
\begin{aligned}
S_0^{(-33)}  &= K_0 \oplus IV_3 = 0 \\
S_1^{(-33)}  &= K_1 = 72340172838076673 \\
S_2^{(-33)}  &= K_2 \oplus IV_2 = 0 \\
S_3^{(-33)}  &= K_3 \oplus IV_1 = 0 \\
S_4^{(-33)}  &= K_0 = 72340172838076673 \\
S_5^{(-33)}  &= K_1 \oplus IV_0 = 0 \\
S_6^{(-33)}  &= \overline{K_2} = 18374403900871474942 \\
S_7^{(-33)}  &= \overline{K_3} = 18374403900871474942 \\
S_8^{(-33)}  &= K_0 = 72340172838076673 \\
S_9^{(-33)}  &= K_1 = 72340172838076673 \\
S_{10}^{(-33)} &= \overline{K_2} = 18374403900871474942 \\
S_{11}^{(-33)} &= K_3 = 72340172838076673 \\
S_{12}^{(-33)} &= K_0 = 72340172838076673 \\
S_{13}^{(-33)} &= \overline{K_1} = 18374403900871474942 \\
S_{14}^{(-33)} &= K_2 = 72340172838076673 \\
S_{15}^{(-33)} &= \overline{K_3} = 18374403900871474942
& \\
r_0 & = 0 \\
r_1 & = 0 \\
\end{aligned}
$$

Than $S_{-1} = Next^{32}(S_{-33}, INIT)$:

$$
\begin{aligned}
\text{ } & \text{ First Iteration } & \text{ Second Iteration} \\
\text{outfrom-fsm} &= 18374403900871474942 &= 13502859933282840622 \\
S_0 &= 72340172838076673 &= 14040194842892972740 \\
\text{fsmtmp} &= 18374403900871474942 &= 7941926138657232970 \\
r_1 &= 1506115696707685439 &= 11731257164208147182 \\
r_0 &= 18374403900871474942 &= 7941926138657232970 \\
 & & \\
\text{outfrom-fsm} &= 5916051783401092032 &= 13555609679604231892 \\
S_1 &= 14040194842892972740 &= 17058527258369831625 \\
\text{fsmtmp} &= 1578455869545762112 &= 3693081700074742078 \\
r_1 &= 16665820752838714284 &= 1975793898266594287 \\
r_0 &= 1578455869545762112 &= 3693081700074742078 \\
 & & \\
\text{outfrom-fsm} &= 4578045079454278568 &= 330988681113870312 \\
S_2 &= 8109529650045969320 &= 9447414631137934454 \\
\text{fsmtmp} &= 16593480580000637610 &= 3242316435590973959 \\
r_1 &= 3812727338100688720 &= 2685957453715003781 \\
r_0 &= 16593480580000637610 &= 3242316435590973959 \\
 & & \\
\text{outfrom-fsm} &= 7078321316971757826 &= 10762630311299997688 \\
S_3 &= 7078321316971757826 &= 11913252476948580299 \\
\text{fsmtmp} &= 9000248489057290321 &= 15411893410939479413 \\
r_1 &= 69278904888565184 &= 11232052509867135957 \\
r_0 &= 9000248489057290321 &= 15411893410939479413 \\
 & & \\
\text{outfrom-fsm} &= 16128708309420168339 &= 16201188757777514133 \\
S_4 &= 8849065300760631725 &= 7783867504455278423 \\
\text{fsmtmp} &= 14109473747781537924 &= 9843835694527415966 \\
r_1 &= 15518682930402391927 &= 9646457503453439289 \\
r_0 &= 14109473747781537924 &= 9843835694527415966 \\
 & & \\
\text{outfrom-fsm} &= 16843588257224006982 &= 8177753334294184140 \\
S_5 &= 16064797001155962607 &= 14481248189037522862 \\
\text{fsmtmp} &= 5181468506738809631 &= 647128060881822127 \\
r_1 &= 2114762163733915410 &= 6603830037754715532 \\
r_0 &= 5181468506738809631 &= 647128060881822127 \\
 & & \\
\text{outfrom-fsm} &= 4287639131270948124 &= 9968522499958934737 \\
S_6 &= 11443748788648833779 &= 11436021319205981162 \\
\text{fsmtmp} &= 9193083480705673236 &= 70338440993744215 \\
r_1 &= 8757858304511764177 &= 17805012663289383991 \\
r_0 &= 9193083480705673236 &= 70338440993744215 \\
 & & \\
\text{outfrom-fsm} &= 7489178481638604246 &= 7545448658154536310 \\
S_7 &= 13950560777361581639 &= 16327042210080188670 \\
\text{fsmtmp} &= 17606923605272395902 &= 7142136094035110798 \\
r_1 &= 15617645847032314323 &= 18229292116310075961 \\
r_0 &= 17606923605272395902 &= 7142136094035110798 \\
 & & \\
\text{outfrom-fsm} &= 7876711077485141782 &= 13350975840476036789 \\
S_8 &= 16935647933600994748 &= 15611174156846857623 \\
\text{fsmtmp} &= 13235698774478725314 &= 14263796231638047207 \\
r_1 &= 10310849613021241592 &= 9709705906751872087 \\
r_0 &= 13235698774478725314 &= 14263796231638047207 \\
 & & \\
\text{outfrom-fsm} &= 3288006930486056582 &= 1740352476428749609 \\
S_9 &= 694713819378071528 &= 16104584334850059192 \\
\text{fsmtmp} &= 3307854327960523755 &= 2698983152248301633 \\
r_1 &= 16056798977435419607 &= 4274972387463320182 \\
r_0 &= 3307854327960523755 &= 2698983152248301633 \\
 & & \\
\text{outfrom-fsm} &= 16816105790372694020 &= 4584789479672234383 \\
S_{10} &= 3238036691905935866 &= 16505351027166186094 \\
\text{fsmtmp} &= 11560615681087449630 &= 2155270523833957236 \\
r_1 &= 7597844401211552806 &= 1325927434767392959 \\
r_0 &= 11560615681087449630 &= 2155270523833957236 \\
 & & \\
\text{outfrom-fsm} &= 11830860389210689598 &= 1193871254501565789 \\
S_{11} &= 7787521429173517556 &= 18375669707894439276 \\
\text{fsmtmp} &= 6086748261102995938 &= 16937101591614250582 \\
r_1 &= 7060359577295745066 &= 5260443889786087660 \\
r_0 &= 6086748261102995938 &= 16937101591614250582 \\
 & & \\
\text{outfrom-fsm} &= 11632834563660314364 &= 11750159425686598446 \\
S_{12} &= 11967225168290275958 &= 3843383999044373852 \\
\text{fsmtmp} &= 7755073396673816594 &= 2918284150926595236 \\
r_1 &= 15208853463984278491 &= 16229686729242446484 \\
r_0 &= 7755073396673816594 &= 2918284150926595236 \\
 & & \\
\text{outfrom-fsm} &= 14025086273952219475 &= 13613584858059745428 \\
S_{13} &= 4017494428287851491 &= 7325485466196597851 \\
\text{fsmtmp} &= 146082180662741 &= 14288293682699080962 \\
r_1 &= 2872636155479203759 &= 11167589560675139309 \\
r_0 &= 146082180662741 &= 14288293682699080962 \\
 & & \\
\text{outfrom-fsm} &= 1160839771106967063 &= 12756637356166811568 \\
S_{14} &= 10408568609576146512 &= 4079698603764182093 \\
\text{fsmtmp} &= 10660157584652721315 &= 11096515194860026969 \\
r_1 &= 15379215330163846075 &= 17107865075787086930 \\
r_0 &= 10660157584652721315 &= 11096515194860026969 \\
 & & \\
\text{outfrom-fsm} &= 17370053930525055304 &= 4609406386520528116 \\
S_{15} &= 1266522537324379672 &= 3079818744787083110 \\
\text{fsmtmp} &= 8899696424744570417 &= 2504505001121909166 \\
r_1 &= 3924431710369381479 &= 2400880894753671819 \\
r_0 &= 8899696424744570417 &= 2504505001121909166 \\
 & & \\
\end{aligned}
$$

$S_0 = Next(S_{-1})$

$$
\begin{aligned}
\text{out-stream}_0 &= 1634536220360670029 \\
\text{out-stream}_1 &= 12787038715280713708 \\
\text{out-stream}_2 &= 9097779104846760658 \\
\text{out-stream}_3 &= 6154163245762047471 \\
\text{out-stream}_4 &= 997757395239562531 \\
\text{out-stream}_5 &= 14666318655515091306 \\
\text{out-stream}_6 &= 7926949760597382923 \\
\text{out-stream}_7 &= 8847959440695055559 \\
\text{out-stream}_8 &= 17235655114145593377 \\
\text{out-stream}_9 &= 4900401458970558239 \\
\text{out-stream}_{10} &= 14176030799782379947 \\
\text{out-stream}_{11} &= 3044710789191076093 \\
\text{out-stream}_{12} &= 13914785489432113698 \\
\text{out-stream}_{13} &= 5074552048776352284 \\
\text{out-stream}_{14} &= 2076101186604161492 \\
\text{out-stream}_{15} &= 7502607990159354905 \\
\end{aligned}
$$

Trunslate uint-64 to bytees ``uint64s_to_bytes():`` $|| ^{n-1}_{i=0} BE_8(x_i \text{ mod } 2^{64})$

``` 
gamma.hex() = "16af0a08431b7b4db174aff6817967ec7e41cde4cd5ccad25567fadda9696def"
    "0dd8bf108b45ed23cb893b1c98a9616a6e022ecef8c6570b7aca443b99b154c7"
    "ef31590205caf8214401b929dabeff1fc4bb60e7920681ab2a40fc54c98888fd"
    "c11b3fadcf5c7222466c6e33c58b921c1ccfcb07914ed9d4681e9e376e74ac19" 
```
