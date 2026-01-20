# 4. 钢铁模块：RMC|Steel

RUC-MENCEix-China|Steel（RMC|Steel）是RMC模型家族聚焦于钢铁工业的模块，用于分析中国钢铁工业在绿色低碳转型过程中的供需变化、技术组合、能源结构以及对特定能源商品（如氢能）的需求等。模型同样采用MESSAGEix的建模框架，地理分区包括内地31个省级行政单位，以自下而上的方式包含了钢铁领域的主要生产流程和关键技术信息，并已根据产能、产量和技术成本的实际历史数据进行校准。

## 4.1. 模型结构

<img id='4-1' src="images/01636831a66333fa0f361634bb8f919c3f5dacecad68b0410deb128fecdce5cd.jpg"/>
<p align="center">图4-1 RMC|Steel模型技术流程连接图</p>

如[图4-1](#4-1)所示，RMC|Steel 模型主要对原材料处理、生铁冶炼、粗钢冶炼进行建模，不涉及后续钢卷、钢坯等产品的加工。其中，原材料处理主要包括:
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

对于高炉炼铁、直接还原铁和转炉炼钢技术，还可附加碳捕集与封存（CCS）技术以减少碳排放；对于高炉还可进行氢气喷吹装置改造，也以附加技术的形式实现。此外，模型对氢气生产层面做了细致划分，从生产技术角度划分为煤制氢、天然气制氢、电解水制氢，并可附加相应的CCS技术。各项主要技术的输入和输出关系如[表4-1](#表4-1)所示。
<a id="表4-1"></a>
 
<p align="center">表4-1 RMC|Steel 主要技术的输入与输出</p> 

<table><tr><td>技术</td><td>输入</td><td>输出</td></tr><tr><td>高炉</td><td>焦炭,电力,铁矿石,生石灰</td><td>铁水</td></tr><tr><td>直接还原铁</td><td>氢气,铁矿石</td><td>海绵铁</td></tr><tr><td>转炉</td><td>铁水,电力,生石灰</td><td>粗钢</td></tr><tr><td>电弧炉(海绵铁)</td><td>海绵铁,电力</td><td>粗钢</td></tr><tr><td>电弧炉(废钢)</td><td>废钢、电力</td><td>粗钢</td></tr><tr><td>煤制氢</td><td>煤炭</td><td>氢气</td></tr><tr><td>天然气制氢</td><td>天然气</td><td>氢气</td></tr><tr><td>电解水制氢</td><td>水,电力</td><td>氢气</td></tr></table>


## 4.2. 主要参数设置

### 4.2.1. 投资成本

<table><tr><td>技术</td><td>投资成本</td><td>单位</td><td>来源</td></tr><tr><td>烧结/球团预处理</td><td>45.87</td><td>M$/Mtpa</td><td>Steelonthenet.com,2023</td></tr><tr><td>高温煅烧石灰石</td><td>109.6</td><td>M$/Mtpa</td><td>Chumin,2025</td></tr><tr><td>炼焦</td><td>446.2</td><td>M$/Mtpa</td><td>Reliable Plant,2008</td></tr><tr><td>高炉炼铁</td><td>211</td><td>M$/Mtpa</td><td>IEA-ETSAP,2010</td></tr><tr><td>高炉加装喷吹氢气装置改造</td><td>40</td><td>M$/Mtpa</td><td>-</td></tr><tr><td>高炉加装 CCS</td><td>80.24</td><td>M$/Mtpa</td><td>He et al.,2025;Wanget al.,2025</td></tr><tr><td>氢基直接还原铁</td><td>580</td><td>M$/Mtpa</td><td>Christoph Heinemannet al.,2024</td></tr><tr><td>转炉炼钢</td><td>100</td><td>M$/Mtpa</td><td>IEA-ETSAP,2010</td></tr><tr><td>转炉加装 CCS</td><td>80.24</td><td>M$/Mtpa</td><td>He et al.,2025</td></tr><tr><td>电弧炉(以DRI为主要原料)</td><td>143</td><td>M$/Mtpa</td><td>Steelonthenet.com,2025</td></tr><tr><td>电弧炉(以废钢为主要原料)</td><td>143</td><td>M$/Mtpa</td><td>Steelonthenet.com,2025</td></tr><tr><td>煤制氢</td><td>10692</td><td>M$/Mtpa</td><td>Energy TransitionsCommission,2023;International EnergyAgency,2020</td></tr><tr><td>煤制氢附加 CCS</td><td>444</td><td>M$/Mtpa</td><td>International EnergyAgency,2020</td></tr><tr><td>天然气制氢</td><td>3641.3</td><td>M$/Mtpa</td><td>International EnergyAgency,2020</td></tr><tr><td>天然气制氢附加 CCS</td><td>2693(2050年1488.5)</td><td>M$/Mtpa</td><td>International EnergyAgency,2020</td></tr><tr><td>电解水制氢</td><td>8296.5(2050年3583.1)</td><td>M$/Mtpa</td><td>International EnergyAgency,2020</td></tr></table>

其中，tpa为吨/年。

### 4.2.2. 固定运维成本

<table><tr><td>技术名称</td><td>运维成本</td><td>单位</td><td>参考文献</td></tr><tr><td>烧结/球团预处理</td><td>1.835</td><td>M$/Mtpa</td><td>Arasto, 2015</td></tr><tr><td>高温煅烧石灰石</td><td>8.05</td><td>M$/Mtpa</td><td>AGICO Cement Plant Equipment, 2025</td></tr><tr><td>焦化</td><td>17.18</td><td>M$/Mtpa</td><td>Gallaher, Depro and Agency, 2002</td></tr><tr><td>高炉炼铁</td><td>14.14</td><td>M$/Mtpa</td><td>Gallaher, Depro and Agency, 2002; IEA, 2013</td></tr><tr><td>富氢高炉炼铁</td><td>10</td><td>M$/Mtpa</td><td>-</td></tr><tr><td>高炉加装 CCS</td><td>4.07</td><td>M$/Mtpa</td><td>IEA, 2013</td></tr><tr><td>(氢基)直接还原铁</td><td>20</td><td>M$/Mtpa</td><td>Steelonthenet.com, 2025</td></tr><tr><td>转炉炼钢</td><td>15.45</td><td>M$/Mtpa</td><td>IEA Greenhouse Gas R&amp;D Programme, 2024</td></tr><tr><td>转炉加装 CCS</td><td>2.16</td><td>M$/Mtpa</td><td>IEA, 2013</td></tr><tr><td>电弧炉(DRI)</td><td>81.24</td><td>M$/Mtpa</td><td>Vogl, Åhman and Nilsson, 2018; Benavides et al., 2024</td></tr><tr><td>电弧炉(废钢)</td><td>81.24</td><td>M$/Mtpa</td><td>Vogl, Åhman and Nilsson, 2018; Benavides et al., 2024</td></tr><tr><td>煤制氢</td><td>433</td><td>M$/Mtpa</td><td>International Energy Agency, 2020; 邵乐 et al., 2024</td></tr><tr><td>煤制氢加装 CCS</td><td>18</td><td>M$/Mtpa</td><td>/</td></tr><tr><td>天然气制氢</td><td>454.5</td><td>M$/Mtpa</td><td>邵乐 et al., 2024</td></tr><tr><td>天然气制氢加装 CCS</td><td>50.2</td><td>M$/Mtpa</td><td>/</td></tr><tr><td>电解水制氢</td><td>182.5</td><td>M$/Mtpa</td><td>International Energy Agency, 2020</td></tr></table>

### 4.2.3. 可变运维成本

<table><tr><td>技术名称</td><td>可变成本</td><td>单位</td><td>参考文献</td></tr><tr><td>铁矿石供应</td><td>110.61</td><td>M$/Mt</td><td>Trading Economics, 2025</td></tr><tr><td>石灰石供应</td><td>19.59</td><td>M$/Mt</td><td>矿权资源网, 2025</td></tr><tr><td>煤矿供应</td><td>195.89</td><td>M$/Mt</td><td>国家统计局, 2025</td></tr><tr><td>天然气供应</td><td>694</td><td>M$/Mt</td><td>CEIC Data, 2025</td></tr><tr><td>电力供应</td><td>0.085</td><td>M$/GWh</td><td>国务院国有资产监督管理委员会, 2020; 新浪财经, 2023</td></tr><tr><td>水供应</td><td>0.676</td><td>M$/Mt</td><td>CEIC Data, 2025</td></tr><tr><td>废钢供应</td><td>349.8</td><td>M$/Mt</td><td>《中国冶金报》-中国钢铁新闻网, 2025</td></tr><tr><td>烧结/球团预处理</td><td>20</td><td>M$/Mt</td><td>Rahbari et al., 2025</td></tr><tr><td>煤制氢</td><td>434.1</td><td>M$/Mt</td><td>邵乐 et al., 2024</td></tr><tr><td>天然气制氢</td><td>338.5</td><td>M$/Mt</td><td>邵乐 et al., 2024</td></tr><tr><td>天然气制氢附加 CCS</td><td>0</td><td>M$/Mt</td><td>/</td></tr><tr><td>电解水制氢</td><td>0</td><td>M$/Mt</td><td>/</td></tr></table>

### 4.2.4. 碳排放系数

<table><tr><td>技术名称</td><td>碳排放系数</td><td>单位</td><td>参考文献</td></tr><tr><td>烧结/球团预处理</td><td>0.2</td><td>t-CO2/t-output</td><td>中国钢铁新闻网,2023;赵泽东,李嘉璇,and李原野,2025;steelonthenet,no date</td></tr><tr><td>高温煅烧石灰石</td><td>1</td><td>t-CO2/t-output</td><td>Shenlan Environmental Protection Industry Development Co.,Ltd.,2025</td></tr><tr><td>炼焦</td><td>0.794</td><td>t-CO2/t-output</td><td>Steelonthenet,2025</td></tr><tr><td>高炉炼铁</td><td>1.22</td><td>t-CO2/t-output</td><td>Steelonthenet,2025</td></tr><tr><td>富氢高炉炼铁</td><td>0.67</td><td>t-CO2/t-output</td><td>OECD,2025;Zhang et al.,2024</td></tr><tr><td>高炉加装 CCS</td><td>0.0523</td><td>t-CO2/t-output</td><td>Santos et al.,2013</td></tr><tr><td>(氢基)直接还原铁</td><td>0.04</td><td>t-CO2/t-output</td><td>Rechberger et al.,2020</td></tr><tr><td>转炉炼钢</td><td>0.181</td><td>t-CO2/t-output</td><td>European Commission. Joint Research Centre.,2022;Nancy Margolis &amp; Ross Brindle,2000;steelonthenet,n.d.</td></tr><tr><td>转炉加装 CCS</td><td>0.03</td><td>t-CO2/t-output</td><td>Butterworth,2024</td></tr><tr><td>电弧炉(DRI)</td><td>0.03</td><td>t-CO2/t-output</td><td>European Commission. Joint Research Centre.,2022</td></tr><tr><td>电弧炉(废钢)</td><td>0.03</td><td>t-CO2/t-output</td><td>European Commission. Joint Research Centre.,2022</td></tr><tr><td>煤制氢</td><td>20.1</td><td>t-CO2/t-output</td><td>IEA,2019</td></tr><tr><td>煤制氢加装 CCS</td><td>2.1</td><td>t-CO2/t-output</td><td>IEA,2019</td></tr><tr><td>天然气制氢</td><td>10.13</td><td>t-CO2/t-output</td><td>Baltac et al.,2022</td></tr><tr><td>天然气制氢加装 CCS</td><td>2.32</td><td>t-CO2/t-output</td><td>Baltac et al.,2022</td></tr></table>