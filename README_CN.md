# <img src="icon.png" width="132"/> matlab_functions_verification

[English](README.md) **|** [简体中文](README_CN.md) &emsp; [GitHub](https://github.com/xinntao/matlab_functions_verification) **|** [Gitee码云](https://gitee.com/xinntao/matlab_functions_verification)

MATLAB version: R2017b (9.3.0.713579) <br>
64-bit (glnxa64)

## imresize bicubic

Recommend to use [bicubic_pytorch](https://github.com/thstkdgus35/bicubic_pytorch).

### Accuracy

| Scale  | Diff (Ours)    | Diff ratio (Ours) | Diff ([bicubic_pytorch](https://github.com/thstkdgus35/bicubic_pytorch))    | Diff ratio ([bicubic_pytorch](https://github.com/thstkdgus35/bicubic_pytorch)) |
| :------------- | :----------: |:----------: | :----------: |:----------: |
| Downsample X2 | **2** | **0.00%** | 4 | 0.01% |
| Downsample X3 | **0** | **0.00%** |1 | 0.00% |
| Downsample X4 | **0** | **0.00%** |**0** | **0.00%** |
| Upsample X2 | **86** | **0.01%** | 268 | 0.03% |
| Upsample X3 | **515** | **0.02%** | 759 | 0.04% |
| Upsample X4 | **67** | **0.00%** | 3119 | 0.08% |

### Speed

Run on CPU Intel(R) Xeon(R) CPU E5-2650 v4 @ 2.20GHz.

Average on 100 runs.

| Scale  | Time (Ours)   | Time ([bicubic_pytorch](https://github.com/thstkdgus35/bicubic_pytorch))    | Time (MATLAB) |
| :------------- | :----------: |:----------: | :----------: |
| Downsample X2 | 0.0689 | **0.0019** | 0.0017|
| Downsample X3 | 0.0475 | **0.0028** | 0.0013|
| Downsample X4 | 0.0236 | **0.0023** | 0.0014|
| Upsample X2   | 0.2146 | **0.0627** | 0.0044|
| Upsample X3   | 0.3585 | **0.1078** | 0.0099|
| Upsample X4   | 0.4949 | **0.1631** | 0.0173|

