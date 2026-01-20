# 4. 钢铁模块：RMC|Steel

RUC-MESSAGEix-China|Steel（RMC|Steel）是 RMC 模型家族聚焦于钢铁工业的模块，用于分析中国钢铁工业在绿色低碳转型过程中的供需变化、技术组合、能源结构以及对特定能源商品（如氢能）的需求等。模型同样采用 MESSAGEix 的建模框架，地理分区包括内地 31 个省级行政单位，以自下而上的方式包含了钢铁领域的主要生产流程和关键技术信息，并已根据产能、产量和技术成本的实际历史数据进行校准。

## 4.1. 模型结构

```{figure} ../_static/fig_4_1.png
---
name: Fig. 4-1
align: center
---
图 4-1：RMC|Steel 模型技术流程连接图
```

如{ref}`图 4-1 <Fig. 4-1>` 所示，RMC|Steel 模型主要对原材料处理、生铁冶炼、粗钢冶炼进行建模，不涉及后续钢卷、钢坯等产品的加工。其中，原材料处理主要包括:
- 炼焦 (coking)  
- 石灰煅烧（calcin）
- 铁矿石烧结与球团（sint_pelle）

炼铁技术主要包括：
- 高炉炼铁（bf）
- 富氢高炉炼铁（bf_h2）  
- 天然气基直接还原铁（dri）  
- 氢基直接还原铁（hdri）  
- 氢基直接熔融还原（hmr）

炼钢技术主要包括：
- 氧气顶吹转炉炼钢（bof）  
- 以废钢为原料的电弧炉炼钢 (eaf_scrap)  
- 以（直接还原铁产出的）海绵铁为原料的电弧炉炼钢（eaf_spg）

对于高炉炼铁、直接还原铁和转炉炼钢技术，还可附加碳捕集与封存（CCS）技术以减少碳排放；对于高炉还可进行氢气喷吹装置改造，也以附加技术的形式实现。此外，模型对氢气生产层面做了细致划分，从生产技术角度划分为煤制氢、天然气制氢、电解水制氢，并可附加相应的 CCS 技术。各项主要技术的输入和输出关系如{ref}`表 4-1 <Table 4-1>` 所示。

```{table} 表 4-1：RMC|Steel 主要技术输入与输出
:name: Table 4-1

| 技术 | 输入 | 输出 |
| :--- | :--- | :--- |
| 高炉            | 焦炭，电力，铁矿石，生石灰 | 铁水 |
| 直接还原铁      | 氢气，铁矿石 | 海绵铁 |
| 转炉            | 铁水，电力，生石灰 | 粗钢 |
| 电弧炉（海绵铁）| 海绵铁，电力 | 粗钢 |
| 电弧炉（废钢）  | 废钢，电力 | 粗钢 |
| 煤制氢          | 煤炭 | 氢气 |
| 天然气制氢      | 天然气 | 氢气 |
| 电解水制氢      | 水，电力 | 氢气 |
```


## 4.2. 主要参数设置

```{table} 表 4-2：投资成本
:name: Table 4-2

| 技术 | 投资成本 | 单位 | 来源 |
| :--- | :--- | :--- | :--- |
| 烧结/球团预处理 | 45.87 | M$/Mtpa | [Steelonthenet, 2023](./references.md) |
| 高温煅烧石灰石 | 109.6 | M$/Mtpa | [Chumin, 2025](./references.md) |
| 炼焦 | 446.2 | M$/Mtpa | [Reliable Plant, 2008](./references.md) |
| 高炉炼铁 | 211 | M$/Mtpa | [IEA-ETSAP, 2010a](./references.md) |
| 高炉加装喷吹氢气装置改造 | 40 | M$/Mtpa | - |
| 高炉加装 CCS 改造 | 80.24 | M$/Mtpa | [He et al., 2025; Wang et al., 2025](./references.md) |
| 氢基直接还原铁 | 580 | M$/Mtpa | [Christoph Heinemann et al., 2024](./references.md) |
| 转炉炼钢 | 100 | M$/Mtpa | [IEA-ETSAP, 2010](./references.md) |
| 转炉加装 CCS 改造 | 80.24 | M$/Mtpa | [He et al., 2025](./references.md) |
| 电弧炉（海绵铁）| 143 | M$/Mtpa | [Steelonthenet.com, 2025](./references.md) |
| 电弧炉（废钢） | 143 | M$/Mtpa | [Steelonthenet.com, 2025](./references.md) |
| 煤制氢 | 10692 | M$/Mtpa | [IEA, 2020; Energy Transitions Commission, 2023](./references.md) |
| 煤制氢加装 CCS | 444 | M$/Mtpa | [IEA, 2020](./references.md) |
| 天然气制氢 | 3641.3 | M$/Mtpa | [IEA, 2020](./references.md) |
| 天然气制氢加装 CCS | 2693<br>(1488.5 in 2050) | M$/Mtpa | [IEA, 2020](./references.md) |
| 电解水制氢 | 8296.5<br>(3583.1 in 2050) | M$/Mtpa | [IEA, 2020](./references.md) |
```

```{table} 表 4-3：固定运维成本
:name: Table 4-3

| 技术 | 固定运维成本 | 单位 | 来源 |
| :--- | :--- | :--- | :--- |
| 烧结/球团预处理 | 1.835 | M$/Mtpa | [Arasto, 2015](./references.md) |
| 高温煅烧石灰石 | 8.05 | M$/Mtpa | [AGICO Cement Plant Equipment, 2025](./references.md) |
| 炼焦 | 17.18 | M$/Mtpa | [Gallaher, Depro and Agency, 2002](./references.md) |
| 高炉炼铁 | 14.14 | M$/Mtpa | [Gallaher, Depro and Agency, 2002; IEA, 2013](./references.md) |
| 高炉加装喷吹氢气装置改造 | 10 | M$/Mtpa | - |
| 高炉加装 CCS 改造 | 4.07 | M$/Mtpa | [IEA, 2013](./references.md) |
| 氢基直接还原铁 | 20 | M$/Mtpa | [Steelonthenet.com, 2025](./references.md) |
| 转炉炼钢 | 15.45 | M$/Mtpa | [IEA Greenhouse Gas R&D Programme, 2024](./references.md) |
| 转炉加装 CCS 改造 | 2.16 | M$/Mtpa | [IEA, 2013](./references.md) |
| 电弧炉（海绵铁） | 81.24 | M$/Mtpa | [Vogl, Åhman and Nilsson, 2018; Benavides et al., 2024](./references.md) |
| 电弧炉（废钢） | 81.24 | M$/Mtpa | [Vogl, Åhman and Nilsson, 2018; Benavides et al., 2024](./references.md) |
| 煤制氢 | 433 | M$/Mtpa | [Shao Le et al., 2024](./references.md) |
| 煤制氢加装 CCS | 18 | M$/Mtpa | - |
| 天然气制氢 | 454.5 | M$/Mtpa | [Shao Le et al., 2024](./references.md) |
| 天然气制氢加装 CCS | 50.2 | M$/Mtpa | - |
| 电解水制氢 | 182.5 | M$/Mtpa | [IEA, 2020](./references.md) |
```

```{table} 表 4-4：可变运维成本
:name: Table 4-4

| 技术 | 可变运维成本 | 单位 | 来源 |
| :--- | :--- | :--- | :--- |
| 铁矿石供应 | 110.61 | M$/Mt | [Trading Economics, 2025](./references.md) |
| 石灰石供应  | 19.59 | M$/Mt | [kq81.com, 2025](./references.md) |
| 煤炭供应  | 195.89 | M$/Mt | [National Bureau of Statistics of China, 2025](./references.md) |
| 天然气供应  | 694 | M$/Mt | [CEIC Data, 2025](./references.md) |
| 电力供应 | 0.085 | M$/GWh | [State-owned Assets Supervision and Administration Commission of the State Council, 2020](./references.md) |
| 水供应 | 0.676 | M$/Mt | [CEIC Data, 2025](./references.md) |
| 废钢供应  | 349.8 | M$/Mt | [CSteelNews, 2025](./references.md) |
| 烧结/球团预处理  | 20 | M$/Mt | [Rahbari et al., 2025](./references.md) |
| 煤制氢 | 434.1 | M$/Mt | [Shao Le et al., 2024](./references.md) |
| 煤制氢加装 CCS | 0 | M$/Mt | - |
| 天然气制氢 | 338.5 | M$/Mt | [Shao Le et al., 2024](./references.md) |
| 天然气制氢加装 CCS | 0 | M$/Mt | - |
| 电解水制氢 | 0 | M$/Mt | - |
```

```{table} 表 4-5：碳排放系数
:name: Table 4-5

| 技术 | 碳排放系数 | 单位 | 来源 |
| :--- | :--- | :--- | :--- |
| 烧结/球团预处理 | 0.2 | t-CO<sub>2</sub>/t-output | [CSteelNews, 2023; Steelonthenet, 2025; ZHAO Zedong, LI Jiaxuan, and LI Yuanye, 2025](./references.md) |
| 高温煅烧石灰石 | 1 | t-CO<sub>2</sub>/t-output | [Shenlan Environmental Protection Industry Development Co., Ltd., 2025](./references.md) |
| 炼焦 | 0.794 | t-CO<sub>2</sub>/t-output | [Steelonthenet, 2025](./references.md) |
| 高炉炼铁 | 1.22 | t-CO<sub>2</sub>/t-output | [Steelonthenet, 2025](./references.md) |
| 高炉加装喷吹氢气装置改造 | 0.67 | t-CO<sub>2</sub>/t-output | [Zhang et al., 2024; OECD, 2025](./references.md) |
| 高炉加装 CCS 改造 | 0.0523 | t-CO<sub>2</sub>/t-output | [Santos et al., 2013](./references.md) |
| 氢基直接还原铁 | 0.04 | t-CO<sub>2</sub>/t-output | [Rechberger et al., 2020](./references.md) |
| 转炉炼钢 | 0.181 | t-CO<sub>2</sub>/t-output | [Nancy Margolis and Ross Brindle, 2000; European Commission. Joint Research Centre., 2022; steelonthenet, 2025](./references.md) |
| 转炉加装 CCS 改造 | 0.03 | t-CO<sub>2</sub>/t-output | [Butterworth, 2024](./references.md) |
| 电弧炉（海绵铁） | 0.03 | t-CO<sub>2</sub>/t-output | [European Commission. Joint Research Centre., 2022](./references.md) |
| 电弧炉（废钢） | 0.03 | t-CO<sub>2</sub>/t-output | [European Commission. Joint Research Centre., 2022](./references.md) |
| 煤制氢 | 20.1 | t-CO<sub>2</sub>/t-output | [IEA, 2019](./references.md) |
| 煤制氢加装 CCS | 2.1 | t-CO<sub>2</sub>/t-output | [IEA, 2019](./references.md) |
| 天然气制氢 | 10.13 | t-CO<sub>2</sub>/t-output | [Baltac et al., 2022](./references.md) |
| 天然气制氢加装 CCS | 2.32 | t-CO<sub>2</sub>/t-output |[Baltac et al., 2022](./references.md) |
```
