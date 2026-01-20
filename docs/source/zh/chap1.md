# 1. 模型概述

## 1.1. 背景

RUC-MESSAGEix-China（简称RMC模型）是基于开源建模框架MESSAGEix（[IIASA ECEProgramme,2020](./refences.md)）开发的中国省级尺度能源-经济-环境（E3）综合评估模型，由中国人民大学应用经济学院周文戟教授（邮箱：zhouwenji@ruc.edu.cn）团队和华东理工大学任宏涛教授（邮箱：ren@ecust.edu.cn）联合开发和维护。

## 1.2. 基本原理

RMC 模型基于全球著名综合评估建模框架MESSAGEix，该框架由国际应用系统分析研究所（IIASA）开发和维护，并广泛应用于综合评估模型（Integrated Assessment Models, IAM）和能源系统模型（Energy System Models, ESM）的构建（[IIASA ECE Programme, 2020](./refences.md)）。针对不同部门的子模块（例如 RMC|Steel和 RMC|Transport）采用多种方法开发并与 RMC 主模型相连接。MESSAGEix 具有高度的灵活性，适用于构建地方、国家、多区域或全球能源系统模型，能够反映能源系统长期动态演化，并包含了丰富的技术细节。该框架通常用于分析区域级能源系统，同时也可用于单一能源部门的研究，如电力或热力部门。

作为一种优化建模框架，其总体目标函数是最小化总贴现系统成本，包括所有能源技术的投资和运营成本、可耗竭资源的开采成本和可再生能源成本、排放税以及其他支出。此外，可根据需要向模型添加约束，例如限制能源系统的总碳排放（或单个技术的碳排放）。

MESSAGEix 的更多特性和功能可参阅其在线文档[^1]以及相关文献，例如（[Huppmann et al., 2019](./refences.md)）。源代码可从 GitHub 网站获得[^2]。

## 1.3. 时空分辨率

RMC 模型目前地理分区覆盖我国内地31个省级行政区（暂不包含港澳台），考虑省级尺度的能源系统、经济系统和资源环境特征。

为评估我国双碳目标的系统性影响，RMC 模型目前校准至 2022 年，建模时间跨度为 2025 至 2060 年，以 5 年步长运行。由于 MESSAGEix 框架的灵活性，模型的时间范围和时间步长均可根据研究需求进行灵活修改。

[^1]: [MESSAGEix 文档。](https://docs.messageix.org/en/latest/index.html)
[^2]: [MESSAGEix GitHub 网站。](https://github.com/iiasa/message_ix)
