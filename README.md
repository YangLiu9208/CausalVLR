
<div align="center">
  <div align="center">
      <a href="https://www.sysu-hcp.net/">
      <img src="Images/hcp.jpg" width="170"/>
      </a>
    <a href="">
    <img src="Images/CVLR.jpg" width="400"/>
    </a>
  </div>

  
[![PyPI](https://img.shields.io/pypi/v/0.0.1)]()
[![docs](https://img.shields.io/badge/docs-latest-blue)]()
[![badge](https://github.com/open-mmlab/mmdetection/workflows/build/badge.svg)](https://github.com/open-mmlab/mmdetection/actions)
[![license](https://img.shields.io/github/license/open-mmlab/mmdetection.svg)](https://github.com/open-mmlab/mmdetection/blob/main/LICENSE)
[![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmdetection.svg)](https://github.com/open-mmlab/mmdetection/issues)
[![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmdetection.svg)](https://github.com/open-mmlab/mmdetection/issues)

[📘Documentation]() |
[🛠️Installation]() |
[👀Model Zoo]() |
[🆕Update News]() |
[🚀Ongoing Projects]() |
[🤔Reporting Issues]()

</div>



# Introduction  
<div>
Causal-VLReasoning is a python open-source framework based on PyTorch for causal relation discovery, causal inference that implements state-of-the-art causal learning algorithms for various visual-linguistic reasoning tasks, detail see on <a hraf="">Documentation</a>.
<p> </p>
</div>

<details open>
<summary>Major features</summary>

- **Modular Design**

  We decompose the causal framework of visual-linguistic tasks into different components and one can easily construct a customized causal-reasoning framework by combining different modules.

- **Support of multiple tasks**

  The toolbox directly supports multiple visual-linguistic reasoning tasks such as **VQA**, **Image/Video Caption**, **Medical Report Generation**, **Model Generalization and Robustness** and so on.

- **State of the art**

  The toolbox stems from the codebase developed by the HCPLab team, who dedicated to solving a variety of complex logic tasks through causal reasoning, and we keep pushing it forward.

</details>



<style type="text/css" rel="stylesheet">
  .admonition_note {
  margin: 0px 0px 12px;
  padding: 6px;
  color: #404040;
  background-color: #E7F2FA;
  }
  
  .admonition_title {
  margin: -6px -6px 6px;
  padding: 3px 6px;
  color: #FFFFFF;
  background-color: #6AB0DE;
  }
</style>

<div class="admonition_note">
<p class="admonition_title">❕ Note</p>
<p>The framework is actively being developed. Feedbacks (issues, suggestions, etc.) are highly encouraged.</p>
</div>

# Framework Overview

<div align="center"><font size=4>
Framework of Causal-VLReasoning.
</font>
</div>

![Image](Images/Opensource.png)        

Our Causal-VLReasoning implements methods for visual-linguistic causal learning:

* VQA.
* Image/Video Captioning.
* Medical Report Generation.
* General causal representation learning.
* General causal discovery methods.
* Multiple utilities for building your own method, such as independence tests, score functions, graph operations, and evaluations.

# What's New

### 🔥 **2023.6.29**.
**v0.0.1** was released in 6/30/2023:

- Release Causal-VLReasoning 0.0.1 official version
- Add [Cross-Modal Causal Relational Reasoning for Event-Level Visual Question Answering](https://github.com/YangLiu9208/CMCIR) 

<style>
.tab_center
{
width: auto;
display: table;
margin-left: auto;
margin-right: auto;
}
</style>

<p align="center"><font size=2.>Performance of CMCIR</font></p>

<div class="tab_center">

| Dataset   | What | Why  | How  | When | Where | All  |
| --------- | ---- | ---  | ---- |----- |-------| ---- |
| MSVD-QA   | 33.1 | 58.9 | 84.3 | 77.5 | 42.8  | 43.7 |
| MSRVTT-QA | 32.2 | 50.2 | 82.3 | 78.4 | 38.0  | 38.9 |
</div>

<div align=center>
<img src="Images/CMCIR.gif"/>
</div>

# Getting Started
Please see Overview for the general introduction of [Causal-VLReasoning]().

For detailed user guides and advanced guides, please refer to our [documentation]().

  
![Image](Images/framework.png) 

## Installation

Please refer to Installation for [installation]() instructions.

Briefly, to use Causal-VLReasoning, we could install it using [pip](https://pypi.org/project/Causal-VLReasoning/):

```
pip install Causal-VLReasoning
```

## Running examples

For causal discovery, there are various running examples in the **‘tests’** directory.

For the implemented modules, we provide unit tests for the convenience of developing your own methods.

# Overview of Benchmark and Model Zoo

Please feel free to let us know if you have any recommendation regarding datasets with high-quality. We are grateful for any effort that benefits the development of causality community.

<div class="tab_center">

|Task | Model | Benchmark |
| --- | ----- | --------- |
| VQA |       |           |
| MRG |       |           |
</div>

# FQA

# Contribution

Please feel free to open an issue if you find anything unexpected.
We are always targeting to make our community better!

# Review Paper
[Causal Reasoning Meets Visual Representation Learning: A Prospective Study](https://link.springer.com/article/10.1007/s11633-022-1362-z)     
Machine Intelligence Research (MIR) 2022      
A Review paper for causal reasoning and visual representation learning       
![Image](Images/MIR.png)    

```
@article{liu2022causal,
  title={Causal Reasoning Meets Visual Representation Learning: A Prospective Study},
  author={Liu, Yang and Wei, Yu-Shen and Yan, Hong and Li, Guan-Bin and Lin, Liang},
  journal={Machine Intelligence Research},
  pages={1--27},
  year={2022},
  publisher={Springer}
}
```

# Citation    
If you find this project useful in your research, please consider cite:    
```
@misc{2023Causal-VLReasoning,
    title={HCPLab's Visual-Linguistic Causal Learning Open-source Framework and Benchmark},
    author={Causal-VLReasoning Contributors},
    howpublished = {\url{https://github.com/YangLiu9208/Causal-VLReasoning}},
    year={2023}
}
``` 
# License
This project is released under the [None]().
